
# YOLOv8 Custom Filter Project (CLAHE)

This project demonstrates how to **apply a CLAHE-based preprocessing filter** to images **automatically** during both **training** and **inference** with Ultralytics YOLOv8.  
The filter enhances contrast for better object detection performance, especially in low-light or unevenly lit images.

This setup is **modular and portable**, so you don’t need to modify the YOLOv8 source code.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Dataset Configuration](#dataset-configuration)
- [Training](#training)
- [Detection / Inference](#detection--inference)
- [Customizing the Filter](#customizing-the-filter)
- [Tips](#tips)
- [License](#license)

---

## Project Structure

```
yolov8_custom_filter_clahe/
│
├── custom_filters.py           # CLAHE + optional blur preprocessing pipeline
├── filtered_dataset.py         # YOLODataset subclass applying the filter
├── train_with_filter.py        # Training script using FilteredDataset
├── detect_with_filter.py       # Inference script applying same filter
├── data.yaml                   # Dataset config (paths, classes)
├── requirements.txt            # Python dependencies
├── README.md                   # This documentation
└── test_blank.jpg              # Placeholder image for testing
```

## Features

- Automatic CLAHE preprocessing for **both training and inference**.
- Clean, modular implementation using a **custom dataset class**.
- Works with **Ultralytics YOLOv8** Python package.
- Easy to modify or extend with additional image filters.
- Compatible with any YOLOv8 model: `yolov8n.pt`, `yolov8s.pt`, etc.

## Requirements

- Python 3.8+
- Ultralytics YOLOv8
- OpenCV (`opencv-python`)
- NumPy

## Installation

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate         # Windows (PowerShell: venv\Scripts\Activate.ps1)
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset Configuration

- Organize your dataset as follows (example):

```
datasets/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
```

- Update `data.yaml` to reflect your paths, number of classes (`nc`), and class names (`names`).

Example `data.yaml`:

```yaml
train: ./datasets/images/train
val: ./datasets/images/val

nc: 1
names: ['object']
```

## Training

Run the training script:

```bash
python train_with_filter.py
```

- The `FilteredDataset` automatically applies the CLAHE filter to all images during training.
- Output weights and logs are saved in `runs/detect/train_with_clahe/`.

## Detection / Inference

Run detection on an image:

```bash
python detect_with_filter.py path/to/your/test.jpg
```

- The same CLAHE filter is applied automatically before detection.
- Results will be displayed with bounding boxes.
- You can enable saving annotated images by editing `save=True` inside the script.

## Customizing the Filter

- Open `custom_filters.py` to modify `custom_pipeline()`:

```python
def custom_pipeline(img):
    img = clahe_filter(img)                 # CLAHE contrast enhancement
    img = cv2.GaussianBlur(img, (3, 3), 0) # Optional smoothing
    return img
```

- You can add other filters:
  - `cv2.bilateralFilter()` – edge-preserving smoothing
  - `cv2.addWeighted()` – sharpening
  - `cv2.medianBlur()` – noise removal

- Filters are applied automatically during both **training** and **inference**.

## Tips

- Always keep a backup of the original dataset; filters are applied **in-memory** and don’t overwrite images.
- To experiment with randomized filters for data augmentation, add random conditions inside `custom_pipeline()`.
- Adjust the filter parameters depending on your dataset characteristics (lighting, noise, etc.).

## Notes
- The `FilteredDataset` approach is non-destructive and portable.
- You can adjust or replace `custom_pipeline` in `custom_filters.py`
  to experiment with other filters (bilateral, sharpening, median, etc.).
- If you want the filter to be applied only sometimes (data augmentation),
  add randomness inside `custom_pipeline` or wrap it with a random condition
  in `filtered_dataset.py`.

## License

This project is **open-source** and free to use, modify, and distribute.
