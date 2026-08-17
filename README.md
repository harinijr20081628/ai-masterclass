# ai-masterclass
"Projects and exercises from my AI Masterclass"
## 🎥 Moving Object Detection

A real-time motion detection system built using Python and OpenCV that identifies and highlights moving objects from a live camera feed.

**Day:** 5 of AI Masterclass  
**Status:** ✅ Completed

### 🛠️ Tech Stack
- Python
- OpenCV
- imutils

### 📌 Concepts Covered
- Gaussian Blur (noise reduction)
- Frame Differencing (detecting change between frames)
- Thresholding (binary image conversion)
- Contour Detection (finding object boundaries)
- Bounding Box Visualization

### ⚙️ How It Works
1. Captures a reference frame from the camera
2. Converts each new frame to grayscale and blurs it to reduce noise
3. Computes the absolute difference between the reference and current frame
4. Applies thresholding to highlight significant changes
5. Detects contours and draws bounding boxes around objects that exceed a minimum area
6. Displays "Moving object detected" on the live feed

### ▶️ Run It
\`\`\`bash
pip install opencv-python imutils
python moving_object_detection.py
\`\`\`
