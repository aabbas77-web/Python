# train_with_filter.py
# Training script that uses the FilteredDataset to apply CLAHE preprocessing
# without modifying ultralytics source code.
from ultralytics import YOLO
from filtered_dataset import FilteredDataset

# Choose the YOLOv8 base model. Change to yolov8s.pt / yolov8m.pt etc as needed.
model = YOLO('yolov8n.pt')

model.train(
    data='data.yaml',             # Path to your dataset config
    epochs=50,
    imgsz=640,
    batch=16,
    dataset_class=FilteredDataset,  # Custom dataset class with filters
    name='train_with_clahe'
)
