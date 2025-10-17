# filtered_dataset.py
from ultralytics.data.dataset import YOLODataset
from custom_filters import custom_pipeline

class FilteredDataset(YOLODataset):
    """Custom YOLOv8 dataset that applies a preprocessing filter to images.
    This class overrides load_image to inject the custom_pipeline.
    """
    def load_image(self, i):
        # Call the parent to get the image, path and original shape
        im, path, shape = super().load_image(i)
        # Apply the custom filter pipeline
        im = custom_pipeline(im)
        return im, path, shape
