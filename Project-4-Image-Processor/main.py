import numpy as np

image = np.array([
    [50, 80, 90, 120, 150],
    [60, 70, 100, 130, 160],
    [40, 60, 110, 140, 170],
    [30, 50, 90, 150, 180],
    [20, 40, 80, 140, 200]
])

bright_image = image + 40
inverted_image = 255 - image
threshold_image = np.where(image > 100, 255, 0)

print("Original Image:\n", image)
print("\nBrightened Image:\n", bright_image)
print("\nInverted Image:\n", inverted_image)
print("\nThreshold Image:\n", threshold_image)
