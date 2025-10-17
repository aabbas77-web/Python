import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

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

def halftone_gray(img_path, block_size=8):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    output = np.zeros((h, w), dtype=np.uint8)

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = img[y:y+block_size, x:x+block_size]
            mean_intensity = np.mean(block)
            radius = int((1 - mean_intensity / 255) * (block_size / 2))
            center = (x + block_size // 2, y + block_size // 2)
            cv2.circle(output, center, radius, 255, -1)

    return output

def floyd_steinberg_dither(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    for y in range(img.shape[0]-1):
        for x in range(1, img.shape[1]-1):
            old = img[y, x]
            new = 0 if old < 128 else 255
            img[y, x] = new
            error = old - new
            img[y, x+1] += error * 7/16
            img[y+1, x-1] += error * 3/16
            img[y+1, x] += error * 5/16
            img[y+1, x+1] += error * 1/16
    return np.clip(img, 0, 255).astype(np.uint8)

def bayer_matrix(n):
    """Generate an n×n Bayer threshold matrix."""
    if n == 1:
        return np.array([[0]])
    smaller = bayer_matrix(n // 2)
    return np.block([
        [4 * smaller + 0, 4 * smaller + 2],
        [4 * smaller + 3, 4 * smaller + 1]
    ])

def bayer_dither_gray(image_path, matrix_size=8):
    """Apply Bayer (ordered) dithering to a grayscale image."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32) / 255.0  # normalize 0-1
    
    # Create Bayer matrix and normalize to 0–1
    M = bayer_matrix(matrix_size)
    M = (M + 0.5) / (matrix_size * matrix_size)
    
    # Tile matrix to image size
    tiled = np.tile(M, (img.shape[0] // matrix_size + 1, img.shape[1] // matrix_size + 1))
    tiled = tiled[:img.shape[0], :img.shape[1]]
    
    # Apply thresholding
    dithered = (img > tiled).astype(np.uint8) * 255
    return dithered

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

    halftoned = cv2.cvtColor(halftoned, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(halftoned, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("halftoned_bw_output.jpg", bw)

    # Convert to 1-bit format using Pillow
    bw_pil = Image.fromarray(bw).convert("1")  # "1" = 1-bit pixels, black and white
    # Save as monochrome
    bw_pil.save("halftoned_bw_output.bmp")

    output = halftone_gray("input.jpg")
    cv2.imwrite("halftone_gray_output.jpg", output)

    _, bw = cv2.threshold(output, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("halftone_gray_bw_output.jpg", bw)

    # Convert to 1-bit format using Pillow
    bw_pil = Image.fromarray(bw).convert("1")  # "1" = 1-bit pixels, black and white
    # Save as monochrome
    bw_pil.save("halftone_gray_bw_output.bmp")

    img = cv2.imread("input.jpg");
    output = floyd_steinberg_dither(img)
    cv2.imwrite("halftone_floyd_output.jpg", output)

    _, bw = cv2.threshold(output, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("halftone_floyd_bw_output.jpg", bw)

    # Convert to 1-bit format using Pillow
    bw_pil = Image.fromarray(bw).convert("1")  # "1" = 1-bit pixels, black and white
    # Save as monochrome
    bw_pil.save("halftone_floyd_bw_output.bmp")

    output = bayer_dither_gray("input.jpg", matrix_size=8)
    cv2.imwrite("halftone_bayer_output.jpg", output)

    _, bw = cv2.threshold(output, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("halftone_bayer_bw_output.jpg", bw)

    # Convert to 1-bit format using Pillow
    bw_pil = Image.fromarray(bw).convert("1")  # "1" = 1-bit pixels, black and white
    # Save as monochrome
    bw_pil.save("halftone_bayer_bw_output.bmp")


