Shi-Tomasi Corner Detector
Overview
This project demonstrates the Shi-Tomasi corner detection algorithm, a variant of the Harris corner detector. Shi-Tomasi improved upon the Harris detector by introducing a quality measure that allows for better corner point selection.

How It Works
Image Loading:

Load the target image in grayscale.
Shi-Tomasi Corner Detection:

Utilize the cv2.goodFeaturesToTrack function to detect corners in the image.
Parameters such as the maximum number of corners (max_corners), quality level (quality_level), and minimum distance between corners (min_distance) can be adjusted for customization.
Visualization:

Draw circles at the detected corner locations on the original image using cv2.circle.
The detected corners are highlighted with filled circles, providing a visual representation of key points in the image.
Display:

Display the original image with the drawn Shi-Tomasi corners using matplotlib.pyplot.imshow.
Usage
Clone this repository to your local machine.
Ensure you have the required dependencies installed (cv2, numpy, matplotlib).
Run the script that includes the Shi-Tomasi corner detection code.
Observe the output, which displays the original image with marked Shi-Tomasi corners.
Customization
Experiment with the Shi-Tomasi corner detection parameters (max_corners, quality_level, min_distance) to observe their impact on corner detection.
Replace the input image (ivy.jpg) with your own images for corner detection.
Feel free to explore and modify the code for your specific corner detection applications.

