# custom_filters.py
import cv2
import numpy as np

def clahe_filter(img):
    """Enhance contrast using CLAHE (adaptive histogram equalization).
    Expects a BGR image (as OpenCV uses BGR).
    """
    # Convert to LAB color space
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    # Apply CLAHE to the L-channel
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l2 = clahe.apply(l)
    lab = cv2.merge((l2, a, b))
    img_clahe = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return img_clahe

def custom_pipeline(img):
    """Chain of filters applied to each image before YOLO sees it.
    Currently: CLAHE -> slight Gaussian blur to reduce noise.
    Modify this function to add/remove filters as needed.
    """
    if img is None:
        return img
    img = clahe_filter(img)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    return img
