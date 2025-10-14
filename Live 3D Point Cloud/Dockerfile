# Base image with PyTorch and CUDA (optional GPU support)
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV and Open3D GUI
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-opencv \
    libgl1-mesa-glx \
    libgtk-3-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy your Python script
COPY live_3d_webcam.py /app/live_3d_webcam.py

# Install Python dependencies
RUN pip install --no-cache-dir \
    open3d \
    opencv-python \
    numpy \
    torchvision \
    torch --upgrade \
    && pip cache purge

# Set environment for X11 GUI forwarding
ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Command to run
CMD ["python3", "live_3d_webcam.py"]
