# FacientAI

Real-time face mesh detection using MediaPipe and OpenCV — 468 facial landmarks overlaid on a live webcam feed, optimized for Windows.

---

## Overview

FacientAI captures live webcam frames, processes them through MediaPipe's FaceMesh model, and renders a tessellation mesh of 468 landmarks in real time. The display is mirrored for a natural selfie-like experience.

---

## Requirements

- Python 3.11
- Windows 10 or 11
- Webcam

---

## Installation

```bash
git clone https://github.com/your-username/FacientAI.git
cd FacientAI
pip install opencv-python mediapipe==0.10.14
```

---

## Usage

```bash
python face.py
```

Press `ESC` or `Q` to exit. Closing the window also stops the program.

---

## How It Works

```
Webcam → OpenCV (DirectShow) → BGR to RGB → MediaPipe FaceMesh
→ 468 landmarks detected → Tessellation drawn → Flip → Display
```

---

## Troubleshooting

| Error | Fix |
|---|---|
| `No module named 'cv2'` | `pip install opencv-python` |
| `no attribute 'solutions'` | `pip install mediapipe==0.10.14` |
| Camera not opening | Change index in line 9: `VideoCapture(1, cv2.CAP_DSHOW)` |
| PowerShell script blocked | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

---

## Configuration

Edit `face.py` to adjust:

```python
max_num_faces=1          # increase to detect multiple faces
min_detection_confidence=0.5
min_tracking_confidence=0.5
```

---

## Stack

`Python 3.11` · `OpenCV 4.9` · `MediaPipe 0.10.14` · `Windows`

---

## License

MIT © Ramkrishna
