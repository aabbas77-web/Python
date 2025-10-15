# 🎥 Simple Webcam Viewer (Python + OpenCV)

This is a lightweight Python application that opens your computer’s webcam, captures frames in real-time, converts them to grayscale, and displays them in a simple OpenCV window.

---

## 🧠 Features

- 📸 Live webcam streaming using OpenCV  
- 🌈 Real-time conversion to grayscale  
- ⌨️ Easy control — press **`q`** to quit  
- ⚙️ Minimal, clean, and portable design  

---

## 📦 Requirements

- Python **3.8+**
- [OpenCV](https://opencv.org/) library for Python

---

## 🧰 Installation

You can run this app inside a **virtual environment** (recommended) or directly with Python.

### 1. Clone this repository
```bash
git clone https://github.com/aabbas77-web/Python/tree/6c8196c3dc17d8802a564cd42e69871cc73dde54/01_show_webcam.git
cd 01_show_webcam
```

### 2. (Optional) Create and activate a virtual environment
```bash
# Create a virtual environment (using venv)
python -m venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install opencv-python
```

---

## ▶️ Run the App

Simply run the main Python script:

```bash
python show_webcam.py
```

You should see a window showing your webcam feed in grayscale.  
Press **`q`** at any time to close the window and exit the program.

---

## 🧩 File Structure

```
simple-webcam-viewer/
│
├── show_webcam.py       # Main script to open webcam and display frames
└── README.md           # Documentation
```

---

## 🧱 Example Output

When running, you’ll see something like this:

```
✅ Press 'q' to quit the webcam window.
```

And a grayscale video feed from your camera will appear in a window titled **“Webcam”**.

---

## 🚀 Notes

- Ensure your webcam is connected and not used by another app.
- If you have multiple cameras, change the index in:
  ```python
  cap = cv2.VideoCapture(0)
  ```
  to `1`, `2`, etc.

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
