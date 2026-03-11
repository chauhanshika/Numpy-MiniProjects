import numpy as np

image = np.array([
    [50, 80, 90, 120, 150],
    [60, 70, 100, 130, 160],
    [40, 60, 110, 140, 170],
    [30, 50, 90, 150, 180],
    [20, 40, 80, 140, 200]
])

# Increase brightness
bright_image = image + 40

print("Original Image:\n")
print(image)

print("\nBrightened Image:\n")
print(bright_image)
