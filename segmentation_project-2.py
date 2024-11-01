#! /bin/python3


import cv2
import numpy as np
import random

def generate_synthetic_images(image_size=(128, 128), num_cells=9, fluorescence_level=5000, cell_size_range=(1, 20), camera_noise=0.05):
    height, width = image_size
    # Initialize black background for synthetic and labeled images
    synthetic_image = np.zeros((height, width), dtype=np.uint16)
    label_image = np.zeros((height, width), dtype=np.uint16)

    for i in range(1, num_cells + 1):  # Unique label per cell (start from 1 to differentiate background)
        # Random position for the cell within bounds
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        # Random cell size
        cell_radius = random.randint(cell_size_range[0], cell_size_range[1])
        # Random intensity with given fluorescence level
        intensity = random.randint(int(fluorescence_level * 0.8), int(fluorescence_level * 1.2))

        # Draw cell on synthetic image with fluorescence intensity
        cv2.circle(synthetic_image, (x, y), cell_radius, intensity, -1)
        # Draw cell on label image with unique label value
        cv2.circle(label_image, (x, y), cell_radius, i, -1)

    # Add Gaussian noise to synthetic image to simulate camera noise
    noise = np.random.normal(0, camera_noise * 65535, (height, width)).astype(np.uint16)
    synthetic_image = cv2.add(synthetic_image, noise)
    synthetic_image = np.clip(synthetic_image, 0, 65535)  # Ensure intensity limits

    # Convert synthetic image to 8-bit for display purposes
    synthetic_image_8bit = cv2.normalize(synthetic_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    label_image_8bit = cv2.normalize(label_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    return synthetic_image_8bit, label_image_8bit

# Example usage:
synthetic_image, label_image = generate_synthetic_images()
cv2.imwrite("synthetic_image-1.png", synthetic_image)
cv2.imwrite("label_image-1.png", label_image)

