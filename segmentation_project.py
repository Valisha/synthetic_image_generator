#!/usr/bin/python3

# Script to create a synthetic image generator to image and labeled image pairs of yeast cells unfer flourescence microscopy

import numpy as np
import random
import cv2

def generate_synthetic_image(width, height, num_cells, flourescence_level, cell_size, noise_level):
    """
    Generate synthetic flourescence of labeled yeast cells

    Parameters:
    -width: width of output image
    -height: height of output image
    -num_cell: number of cells to simulate
    -cell_size (tuple): Range of cell sizes (min, max) in pixrls
    -noise_level: Standard deviation of Gaussian noise

    Returns:
    flourescence image and labelles image in array format
    """

    fl_image = np.zeros((width, height), dtype=np.uint16)
    lab_image = np.zeros((width, height), dtype=np.uint8)

    for cell_id in range(1, num_cells + 1):
        # Random cell position
        # Randomize cell properties for variability
        current_cell_size = cell_size * (0.8 + 0.4 * random.random())  # Cell size with some variance
        ## the above step ensures that variability in the cell size is incorporated for each cell using scaling factors of 0.8 and 0.4
        ## this adds realistic variation, making each cell slightly different in size and brightness, which is closer to what is seen in biological samples
        x_pos = random.randint(int(np.ceil(current_cell_size / 2)), width - int(np.ceil(current_cell_size / 2)))
        y_pos = random.randint(int(np.ceil(current_cell_size / 2)), height - int(np.ceil(current_cell_size / 2)))
        # Create cell mask
        cell_mask = create_circular_cell(current_cell_size, width, height, x_pos, y_pos)
        print(x_pos, y_pos)
        # Ensure that cells do not overlap in the labeled image
        if np.all(lab_image[cell_mask > 0] == 0):
            # Add cell to flourescence image
            fl_image = cv2.add(fl_image, (flourescence_level * (0.8 + 0.4 * random.random()) * cell_mask).astype(np.uint16))

            # Add cell to label image 
            lab_image[cell_mask > 0] = cell_id
    # Add gaussian noise to simulate camera noise
    noise = np.random.normal(0, noise_level * 65535, fl_image.shape).astype(np.int16)
    fl_image = np.clip(fl_image.astype(np.int32) + noise, 0, 65535).astype(np.uint16)

    return fl_image, lab_image

def create_circular_cell(cell_size, width, height, x_center, y_center):
    # Create a circular mask for a yeast cell
    # Create a blank image to draw 
    cell_image = np.zeros((height, width), dtype=np.uint8)
    ## Draw a filtered circle 
    cv2.circle(cell_image, (x_center, y_center), int(cell_size // 2), 255, -1)

    ## Apply gaussian blur to simulate flouresence blurring
    blurred_cell = cv2.GaussianBlur(cell_image, (0, 0), sigmaX=cell_size*0.3).astype(np.float32) / 255

    return blurred_cell

# Example usage
if __name__ == "__main__":
    width, height = 128, 128
    num_cells = 9
    fluorescence_level = 1000
    cell_size = 15 
    noise_level = 0.05

    fluorescence_image, label_image = generate_synthetic_image(width, height, num_cells, fluorescence_level, cell_size, noise_level)
    
    # Save or visualize the generated images
    cv2.imwrite('fluorescence_image.png', fluorescence_image)
    cv2.imwrite('label_image.png', label_image)


