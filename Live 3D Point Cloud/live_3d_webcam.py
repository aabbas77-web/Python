import torch
import cv2
import numpy as np
import open3d as o3d
import os

# ----------------------------
# Step 1: Load MiDaS model
# ----------------------------
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
midas.eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
transform = midas_transforms.small_transform

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
midas.to(device)

# ----------------------------
# Step 2: Open webcam
# ----------------------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Cannot open webcam")

# ----------------------------
# Step 3: Prepare Open3D visualizer
# ----------------------------
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="Live 3D Point Cloud (Optimized)", width=800, height=600)
pcd = o3d.geometry.PointCloud()
vis.add_geometry(pcd)

# ----------------------------
# Step 4: Prepare output folder
# ----------------------------
output_folder = "ply_frames_optimized"
os.makedirs(output_folder, exist_ok=True)

ds_factor = 4  # downsampling factor
voxel_size = 0.01  # voxel downsampling size for smoother visualization
focal_length = 1.0
frame_idx = 0

# ----------------------------
# Step 5: Function to save colored PLY
# ----------------------------
def save_ply_color(filename, verts, colors):
    verts = verts.astype(np.float32)
    colors = (colors * 255).astype(np.uint8)
    with open(filename, 'w') as f:
        f.write("ply\nformat ascii 1.0\n")
        f.write(f"element vertex {len(verts)}\n")
        f.write("property float x\nproperty float y\nproperty float z\n")
        f.write("property uchar red\nproperty uchar green\nproperty uchar blue\n")
        f.write("end_header\n")
        for v, c in zip(verts, colors):
            f.write(f"{v[0]} {v[1]} {v[2]} {c[0]} {c[1]} {c[2]}\n")

# ----------------------------
# Step 6: Main loop
# ----------------------------
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, _ = frame.shape

        # Depth estimation
        input_batch = transform(frame_rgb).unsqueeze(0).to(device)
        with torch.no_grad():
            depth = midas(input_batch)
            depth = torch.nn.functional.interpolate(
                depth.unsqueeze(1),
                size=(h, w),
                mode="bicubic",
                align_corners=False
            ).squeeze().cpu().numpy()

        # Downsample for speed
        x, y = np.meshgrid(np.arange(0, w, ds_factor), np.arange(0, h, ds_factor))
        z = depth[::ds_factor, ::ds_factor]
        img_down = frame_rgb[::ds_factor, ::ds_factor]

        cx, cy = w / 2, h / 2
        X = (x - cx) * z / focal_length
        Y = (y - cy) * z / focal_length
        points_3d = np.stack((X, Y, z), axis=-1).reshape(-1, 3)
        colors = img_down.reshape(-1, 3) / 255.0

        # Create point cloud and apply voxel downsampling
        temp_pcd = o3d.geometry.PointCloud()
        temp_pcd.points = o3d.utility.Vector3dVector(points_3d)
        temp_pcd.colors = o3d.utility.Vector3dVector(colors)
        pcd_down = temp_pcd.voxel_down_sample(voxel_size=voxel_size)

        # Update Open3D visualizer
        pcd.points = pcd_down.points
        pcd.colors = pcd_down.colors
        vis.update_geometry(pcd)
        vis.poll_events()
        vis.update_renderer()

        # Save PLY
        ply_filename = os.path.join(output_folder, f"frame_{frame_idx:04d}.ply")
        save_ply_color(ply_filename, np.asarray(pcd_down.points), np.asarray(pcd_down.colors))
        print(f"Saved {ply_filename}")
        frame_idx += 1

except KeyboardInterrupt:
    print("Stopping capture...")

cap.release()
vis.destroy_window()
print(f"All frames saved in folder: {output_folder}")
