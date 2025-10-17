from ultralytics import YOLO
from ultralytics.data.dataset import YOLODataset
from custom_filters import custom_pipeline
import cv2

class FilteredDataset(YOLODataset):
    def load_image(self, i):
        img, info = super().load_image(i)
        img = custom_pipeline(img)
        return img, info

# Patch YOLO’s dataset loader
YOLODataset = FilteredDataset

# Now train
model = YOLO("yolov8n.pt")
model.train(data="./datasets/data.yaml", epochs=50, imgsz=640)
