# detect_with_filter.py
# Inference script that applies the same CLAHE filter before running detection.
import cv2
from ultralytics import YOLO
from custom_filters import custom_pipeline

model = YOLO('runs/detect/train_with_clahe/weights/best.pt')  # update path if needed

def detect_image(path, show=True, save=False):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f'Image not found: {path}')
    # Apply same preprocessing filter as training
    img = custom_pipeline(img)
    # Run YOLO inference (Ultralytics accepts numpy images as source)
    results = model.predict(source=img, show=show)
    if save:
        # results[0].plot() returns an image with annotated boxes (if available)
        annotated = results[0].plot()
        out_path = 'annotated_' + path.split('/')[-1]
        cv2.imwrite(out_path, annotated[:, :, ::-1])  # convert RGB->BGR for cv2
        print('Saved annotated image to', out_path)
    return results

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python detect_with_filter.py <image_path>')
    else:
        detect_image(sys.argv[1], show=True, save=False)
