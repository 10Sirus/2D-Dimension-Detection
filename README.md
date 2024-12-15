# 2D Dimension Detection and Shape Classification

This project demonstrates a Python-based solution to analyze 2D images, detect shapes, and calculate dimensions using OpenCV. The script processes an image to extract contours, approximates shapes, calculates their dimensions, and labels them directly on the image.

![image](https://github.com/user-attachments/assets/0439e6ad-636c-4b87-a3cc-6c1c98f122c4)


---

## Features

- **Shape Detection**\
  Identifies common shapes such as triangles, rectangles, squares, circles, pentagons, and hexagons based on polygonal approximations.

- **Dimension Estimation**\
  Accurately calculates distances between key points of detected shapes and scales them relative to a reference dimension.

- **Contours Visualization**\
  Highlights the boundaries of detected shapes and overlays labels with shape names and dimensions on the image.

- **Noise Reduction**\
  Uses Gaussian blurring and edge detection for robust contour detection, even in noisy images.

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **OpenCV**\
  Install it using:
  ```bash
  pip install opencv-python
  ```
- **NumPy**\
  Install it using:
  ```bash
  pip install numpy
  ```

Optional (if using Google Colab):

- Use the following to display images:
  ```python
  from google.colab.patches import cv2_imshow
  ```

---

## Setup and Usage

1. **Clone the Repository**\
   Clone the project or copy the script into your development environment.

2. **Provide the Input Image**\
   Replace the path `'/content/tip (1).jpg'` with the path to your input image.

3. **Run the Script**\
   Execute the script in your environment. If you're using Google Colab, the output image will display inline.

4. **View Results**\
   Detected shapes will be outlined, and dimensions will be labeled directly on the image.

---

## How It Works

1. **Image Preprocessing**

   - Converts the image to grayscale.
   - Reduces noise using Gaussian blur.
   - Applies Canny edge detection to highlight boundaries.

2. **Contour Detection**

   - Extracts contours using OpenCV's `findContours` function.
   - Approximates contours into polygonal shapes using the Douglas-Peucker algorithm.

3. **Shape and Dimension Analysis**

   - Identifies shapes based on the number of vertices.
   - Calculates dimensions (distances) between key points and scales them relative to a reference size.

4. **Visualization**

   - Draws contours on the original image.
   - Annotates shapes with their names and dimensions.

---

## Example Output

After running the script, you will see an image with:

- Contours drawn around detected shapes.
- Labeled shape names (e.g., "triangle," "rectangle").
- Scaled dimensions displayed alongside shapes.

---

## Potential Applications

- Object measurement and inspection in 2D images.
- Shape classification for image-based data analysis.
- Preprocessing step for more complex computer vision tasks.

---

## Future Enhancements

- Support for irregular shapes with advanced curvature analysis.
- Integration of machine learning for more accurate shape detection.
- Automatic reference size detection from calibration markers.
