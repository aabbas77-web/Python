# 🎥 Enhanced Webcam Viewer (Python + OpenCV)

This Python application opens your computer’s webcam and provides an enhanced viewing experience with live FPS display, grayscale toggle, and snapshot saving functionality.

---

## 🧠 Features

- 📸 Real-time webcam streaming  
- 🌈 Toggle between color and grayscale view (`g` key)  
- ⌨️ Keyboard controls:
  - `q` → Quit  
  - `g` → Toggle grayscale  
  - `s` → Save snapshot  
- 💾 Automatic saving of snapshots to a dedicated `snapshots/` folder  
- ⚡ Displays live FPS on the video feed  

---

## 📦 Requirements

- Python **3.8+**  
- [OpenCV](https://opencv.org/) library for Python  

Install OpenCV with:
```bash
pip install opencv-python
```

---

## 🧰 Installation

1. Clone this repository:
```bash
git clone https://github.com/aabbas77-web/Python.git
cd 02_enhanced_webcam
```

2. (Optional) Create and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install opencv-python
```

---

## ▶️ Run the App

```bash
python enhanced_webcam.py
```

You will see a window titled **“Enhanced Webcam”** with your live webcam feed.  

- Press **`g`** to toggle grayscale  
- Press **`s`** to save a snapshot (saved in the `snapshots/` folder)  
- Press **`q`** to quit  

---

## 🧩 File Structure

```
02_enhanced_webcam/
│
├── enhanced_webcam.py    # Main script
├── README.md             # Documentation
└── snapshots/            # Folder where snapshots are saved
```

---

## 🪪 Notes

- Ensure your webcam is connected and not used by another application.  
- If you have multiple cameras, change the camera index:
```python
cap = cv2.VideoCapture(0)  # 0 → default camera, 1 → second camera
```

---

## 🧑‍💻 Author

**Ali Abbas**  
PhD in Computer Vision – Software Engineer  
📧 [aabbas7@gmail.com](mailto:aabbas7@gmail.com)  
🌐 [https://aabbas77-web.github.io](https://aabbas77-web.github.io)  
🔗 [LinkedIn](https://www.linkedin.com/in/ali-abbas-45799710b)

---

## 🪪 License

This project is open-source and available under the [MIT License](LICENSE).
