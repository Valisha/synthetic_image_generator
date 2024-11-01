#! /bin/python3


# Adjusting the segmentation script to generate synthetic images with customized fluorescence and color-coded labeling

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

# Function from segmentation_project-4.py
def generate_synthetic_images(image_size, num_cells, fluorescence_level, cell_size_range, camera_noise):
    height, width = image_size
    synthetic_image = np.zeros((height, width), dtype=np.uint16)
    label_image = np.full((height, width, 3), (0, 0, 255), dtype=np.uint8)  # Set background to blue
    
    # Random intensities for cells based on fluorescence level
    cell_labels = random.sample(range(1, 256), num_cells)  # Ensure unique labels between 1 and 255
    
    for i in range(num_cells):
        # Random position for the cell within bounds
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        # Random cell size
        cell_radius = random.randint(cell_size_range[0], cell_size_range[1])
        # Random intensity with given fluorescence level
        intensity = random.randint(int(fluorescence_level * 0.8), int(fluorescence_level * 1.2))
        
        # Draw cell on synthetic image with grayscale fluorescence intensity
        cv2.circle(synthetic_image, (x, y), cell_radius, intensity, -1)
        
        # Determine the color of the cell based on the intensity
        blue = max(0, 255 - int(intensity * 0.1))  # Blue decreases as intensity increases
        green = min(255, int(intensity * 0.1))  # Green increases as intensity increases
        red = min(255, int(intensity * 0.05))  # Red component for added variation
        cell_color = (blue, green, red)
        
        # Draw cell on label image with a color based on intensity
        cv2.circle(label_image, (x, y), cell_radius, cell_color, -1)
    
    # Add Gaussian noise to synthetic image to simulate camera noise
    noise = np.random.normal(0, camera_noise * 5000, (height, width)).astype(np.int16)  # Adjusted noise level for better control
    synthetic_image = cv2.add(synthetic_image, noise, dtype=cv2.CV_16U)
    synthetic_image = np.clip(synthetic_image, 0, 65535)  # Ensure intensity limits
    
    # Convert synthetic image to 8-bit grayscale for display purposes
    synthetic_image_8bit = ((synthetic_image / 65535) * 255).astype(np.uint8)
    synthetic_colored = cv2.cvtColor(synthetic_image_8bit, cv2.COLOR_GRAY2BGR)
    synthetic_colored[:, :, 1] = synthetic_image_8bit  # Set green channel for yellowish tint
    synthetic_colored[:, :, 2] = synthetic_image_8bit  # Set red channel for yellowish tint

    return synthetic_colored, label_image

synthetic_image, label_image = generate_synthetic_images(image_size=(124,124), num_cells=10, fluorescence_level=5000, cell_size_range=(2, 10), camera_noise=0.05)

    # Adjusting the output so that one version is in grayscale
plt.figure(figsize=(10, 5))

    # Display the synthetic grayscale image with yellowish tint
plt.subplot(1, 2, 1)
plt.title(f'Yellowish Synthetic Image')
plt.imshow(synthetic_image)
plt.colorbar()
plt.savefig(f"synthetic_image_gray.png")

    # Display the labeled image with blue background and intensity-based colors
plt.subplot(1, 2, 2)
plt.title(f'Instance Segmentation Labeled Image')
plt.imshow(label_image)
plt.savefig(f"instance_segmentation.png")
plt.show()

