#! /bin/python3


import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def generate_synthetic_images(image_size=(128, 128), num_cells=9, fluorescence_level=5000, cell_size_range=(1, 20), camera_noise=0.05):
    height, width = image_size
    # Initialize black background for synthetic and labeled images
    synthetic_image = np.zeros((height, width), dtype=np.uint16)
    label_image = np.zeros((height, width, 3), dtype=np.uint8)  # 3 channels for color
    
    # Random colors for each cell in the label image
    colors = [tuple(np.random.randint(0, 255, 3).tolist()) for _ in range(num_cells)]
    
    for i in range(num_cells):
        # Random position for the cell within bounds
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        # Random cell size
        cell_radius = random.randint(cell_size_range[0], cell_size_range[1])
        # Random intensity with given fluorescence level
        intensity = random.randint(int(fluorescence_level * 0.8), int(fluorescence_level * 1.2))
        
        # Draw cell on synthetic image with grayscale fluorescence intensity
        cv2.circle(synthetic_image, (x, y), cell_radius, intensity, -1)
        # Draw cell on label image with a unique color
        cv2.circle(label_image, (x, y), cell_radius, colors[i], -1)
    
    # Add Gaussian noise to synthetic image to simulate camera noise
    noise = np.random.normal(0, camera_noise * 65535, (height, width)).astype(np.uint16)
    synthetic_image = cv2.add(synthetic_image, noise)
    synthetic_image = np.clip(synthetic_image, 0, 65535)  # Ensure intensity limits
    
    # Convert synthetic image to 8-bit grayscale for display purposes
    synthetic_image_8bit = cv2.normalize(synthetic_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    return synthetic_image_8bit, label_image

# Generate the synthetic and label images
synthetic_image, label_image = generate_synthetic_images()

# Display the grayscale synthetic image
plt.figure(figsize=(6, 6))
plt.imshow(synthetic_image, cmap="gray")
plt.colorbar()
plt.title("Grayscale Synthetic Image")
plt.savefig("grayscale.png")

# Display the color instance segmentation label image
plt.figure(figsize=(6, 6))
plt.imshow(label_image)
plt.title("Instance Segmentation Labeled Image")
plt.savefig("instance_segmentation.png")

