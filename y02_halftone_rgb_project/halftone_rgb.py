import cv2
import numpy as np
import matplotlib.pyplot as plt

def halftone_channel(channel, block_size=8):
    h, w = channel.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = channel[y:y+block_size, x:x+block_size]
            mean_intensity = np.mean(block)
            radius = int((1 - mean_intensity / 255) * (block_size / 2))
            center = (x + block_size // 2, y + block_size // 2)
            cv2.circle(output, center, radius, 255, -1)
    return output

def halftone_rgb(image_path, block_size=8):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img)
    r_h = halftone_channel(r, block_size)
    g_h = halftone_channel(g, block_size)
    b_h = halftone_channel(b, block_size)
    halftoned = cv2.merge([r_h, g_h, b_h])
    return img, halftoned

if __name__ == "__main__":
    input_path = "input.jpg"
    original, halftoned = halftone_rgb(input_path, block_size=8)
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis("off")
    plt.subplot(1,2,2)
    plt.title("Halftoned RGB")
    plt.imshow(halftoned)
    plt.axis("off")
    plt.show()
    cv2.imwrite("halftoned_output.jpg", cv2.cvtColor(halftoned, cv2.COLOR_RGB2BGR))
    print("Halftoned image saved as halftoned_output.jpg")
