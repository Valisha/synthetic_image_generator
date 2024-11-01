#!/usr/bin/python3

import numpy as np
import random
import cv2

def generate_synthetic_image(width, height, num_cells, fluorescence_level, cell_size_range, noise_level):
    """
    Generate synthetic fluorescence images of labeled yeast cells.

    Parameters:
    - width: Width of output image
    - height: Height of output image
    - num_cells: Number of cells to simulate
    - fluorescence_level: Maximum intensity for cell fluorescence
    - cell_size_range (tuple): Range of cell sizes (min, max) in pixels
    - noise_level: Standard deviation of Gaussian noise

    Returns:
    - fluorescence_image: Fluorescence image as a uint16 array
    - label_image: Label image as a uint8 array, where 0 is background, and cells are labeled incrementally
    """

    fl_image = np.zeros((height, width), dtype=np.uint16)
    lab_image = np.zeros((height, width), dtype=np.uint8)

    for cell_id in range(1, num_cells + 1):
        # Randomize cell properties
        current_cell_size = random.randint(*cell_size_range)
        x_pos = random.randint(current_cell_size // 2, width - current_cell_size // 2)
        y_pos = random.randint(current_cell_size // 2, height - current_cell_size // 2)

        # Create cell mask
        cell_mask = create_circular_cell(current_cell_size, width, height, x_pos, y_pos)

        # Ensure cells do not overlap in the labeled image
        if np.all(lab_image[cell_mask > 0] == 0):
            # Add cell to fluorescence image
            fl_image += (fluorescence_level * (0.8 + 0.4 * random.random()) * cell_mask).astype(np.uint16)

            # Add cell to label image
            lab_image[cell_mask > 0] = cell_id

    # Add Gaussian noise to simulate camera noise
    noise = np.random.normal(0, noise_level * 65535, fl_image.shape).astype(np.int16)
    fl_image = np.clip(fl_image.astype(np.int32) + noise, 0, 65535).astype(np.uint16)

    return fl_image, lab_image

def create_circular_cell(cell_size, width, height, x_center, y_center):
    """
    Create a circular mask for a yeast cell with Gaussian blur for fluorescence effect.

    Parameters:
    - cell_size: Diameter of the cell
    - width: Width of the image
    - height: Height of the image
    - x_center: X-coordinate of cell center
    - y_center: Y-coordinate of cell center

    Returns:
    - blurred_cell: Blurred circular cell mask as a float32 array
    """
    cell_image = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(cell_image, (x_center, y_center), cell_size // 2, 255, -1)
    blurred_cell = cv2.GaussianBlur(cell_image, (0, 0), sigmaX=cell_size * 0.3).astype(np.float32) / 255
    return blurred_cell

# Example usage
if __name__ == "__main__":
    width, height = 128, 128
    num_cells = 9
    fluorescence_level = 500
    cell_size_range = (10, 20)  # Min and max cell size in pixels
    noise_level = 0.05

    fluorescence_image, label_image = generate_synthetic_image(width, height, num_cells, fluorescence_level, cell_size_range, noise_level)
    
    # Save or visualize the generated images
    cv2.imwrite('fluorescence_image.png', fluorescence_image)
    cv2.imwrite('label_image.png', label_image)

