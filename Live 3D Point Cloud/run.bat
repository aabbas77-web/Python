docker run -it \
    --device=/dev/video0:/dev/video0 \
    -e DISPLAY=host.docker.internal:0.0 \
    live3d-webcam
