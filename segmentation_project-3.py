#! /bin/python3

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def generate_synthetic_images(image_size=(128, 128), num_cells=9, fluorescence_level=5000, cell_size_range=(1, 20), camera_noise=0.05):
    height, width = image_size
    # Initialize black background for synthetic and labeled images
    synthetic_image = np.zeros((height, width), dtype=np.uint16)
    label_image = np.zeros((height, width), dtype=np.uint8)

    for i in range(1, num_cells + 1):  # Unique label per cell (start from 1 to differentiate background)
        # Random position for the cell within bounds
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        # Random cell size
        cell_radius = random.randint(cell_size_range[0], cell_size_range[1])
        # Random intensity with given fluorescence level
        intensity = random.randint(int(fluorescence_level * 0.8), int(fluorescence_level * 1.2))

        # Draw cell on synthetic image with fluorescence intensity
        cv2.circle(synthetic_image, (x, y), cell_radius, intensity, -1)
        # Draw cell on label image with a unique grayscale value
        cv2.circle(label_image, (x, y), cell_radius, i, -1)  # Label image should use unique values for each cell

    # Add Gaussian noise to synthetic image to simulate camera noise
    noise = np.random.normal(0, camera_noise * 65535, (height, width)).astype(np.uint16)
    synthetic_image = cv2.add(synthetic_image, noise)
    synthetic_image = np.clip(synthetic_image, 0, 65535)  # Ensure intensity limits

    # Convert synthetic image to 8-bit for display purposes
    synthetic_image_8bit = cv2.normalize(synthetic_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    return synthetic_image_8bit, label_image

# Generate the synthetic and label images
synthetic_image, label_image = generate_synthetic_images()

# Display the label image with a color map to simulate the distinct labeling of each cell
plt.figure(figsize=(6, 6))
plt.imshow(label_image, cmap="nipy_spectral", interpolation="nearest")
plt.colorbar()
plt.title("Instance Segmentation Labeled Image")
# plt.show()
plt.savefig("labeled_image-3.png")


plt.figure(figsize=(6,6))
plt.imshow(synthetic_image, cmap="nipy_spectral", interpolation="nearest")
plt.colorbar()
plt.title("Flouresence image")
plt.savefig("flourescence_image-3.png")
