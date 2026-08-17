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
## 😀 Face Detection

A real-time face detection system built using Python and OpenCV's Haar Cascade classifier, detecting faces from a live camera feed.

**Day:** 6 of AI Masterclass  
**Status:** ✅ Completed

### 🛠️ Tech Stack
- Python
- OpenCV

### 📌 Concepts Covered
- Haar Cascade Classifiers
- Grayscale Conversion
- Multi-Scale Detection
- Bounding Box Visualization

### ⚙️ How It Works
1. Loads the pre-trained Haar Cascade face detection model
2. Captures live video from the camera
3. Converts each frame to grayscale (Haar Cascades work on grayscale images)
4. Runs `detectMultiScale` to find face coordinates in the frame
5. Draws bounding boxes around detected faces
6. Exits when the `Esc` key is pressed

### ▶️ Run It
\`\`\`bash
pip install opencv-python
python face_detection.py
\`\`\`
