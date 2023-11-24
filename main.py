import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('home0.jpeg')
gray = cv2.imread('home0.jpeg', cv2.IMREAD_GRAYSCALE)

# Define Shi-Tomasi corner detection parameters
max_corners = 150
quality_level = 0.05
min_distance = 15

# Detect corners using Shi-Tomasi
corners = cv2.goodFeaturesToTrack(gray, max_corners, quality_level, min_distance)

# Check if corners are found
if corners is not None:
    # Convert corners to integers
    corners = np.int0(corners)

    # Draw circles at detected corner locations
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 6, 255, -1)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Shi-Tomasi Corners")
    plt.show()
else:
    print("No corners found.")
