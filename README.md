# Dominant Color Detection in Images with OpenCV + NumPy

This project implements a **computer vision pipeline** to analyze an image and **determine its dominant color**, using **OpenCV**, **NumPy**, and **Matplotlib** for image processing and visualization.

---

## Project Overview

The objective is to load an image and compute the **average RGB color** of all its pixels to classify the image’s **dominant color** using a custom rule-based analysis.

1. **Image Loading & Conversion**  
   The input image (`flower.jpg`) is loaded with OpenCV and converted from BGR to RGB for correct visualization and processing.

2. **Pixel-wise RGB Analysis**  
   The image is reshaped into a 2D array of RGB values, and the **mean color** is computed from all pixels.

3. **Color Classification**  
   A custom function uses the mean RGB values to determine whether the image's dominant tone is **vibrant red**, **grayish white**, **navy blue**, etc., based on intensity, saturation, and color dominance thresholds.

4. **Color Visualization**  
   A synthetic color square is generated to visually display the dominant color result.

---

## Key Features

1. **Rule-Based Color Classification**  
   The project defines heuristic rules for recognizing achromatic and chromatic colors (e.g., white, gray, red, green, blue, yellow) based on pixel intensity and saturation.

2. **Visual Feedback**  
   Uses `matplotlib` to show the input image and a color patch of the detected dominant tone.

3. **Simple, Fast, and Extendable**  
   Designed for easy experimentation and can be extended to more advanced image segmentation or clustering techniques (e.g., k-means for dominant color detection).

---

## File Outputs

- Console print of the image resolution and average RGB values  
- Textual label for the detected dominant color (e.g., `[COLOR] The dominant color is: Vibrant green`)  
- A 100x100 synthetic image displaying the average color  

---

## Libraries Used

- `opencv-python` (`cv2`) – for image I/O and processing  
- `numpy` – for numerical operations and color computations  
- `matplotlib` – for image and color visualization  

---

## Conclusion

This project demonstrates a **lightweight approach** to dominant color analysis using basic image statistics and color theory.  
It serves as a solid foundation for more advanced image understanding tasks such as **color clustering**, **palette extraction**, or **scene classification**.

---
