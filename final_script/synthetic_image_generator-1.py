import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import disk
import random
import sys

def generate_synthetic_image(width, height, num_cells, fluorescence_level_range, size_range, shape='disk', noise_level=0.1):
    # Create an empty fluorescence image
    fluorescence_image = np.zeros((height, width), dtype=np.uint16)
    # Create an empty labeled image
    labeled_image = np.zeros((height, width), dtype=np.uint8)

    for cell_id in range(1, num_cells + 1):
        # Randomize cell properties
        cell_radius = random.randint(size_range[0], size_range[1])
        fluorescence_level = random.randint(fluorescence_level_range[0], fluorescence_level_range[1])
        cell_center = (random.randint(cell_radius, height - cell_radius),
                       random.randint(cell_radius, width - cell_radius))

        if shape == 'disk':
            # Generate cell shape (disk)
            rr, cc = disk(cell_center, cell_radius, shape=fluorescence_image.shape)
            # Update fluorescence image and labeled image
            fluorescence_image[rr, cc] += fluorescence_level
            labeled_image[rr, cc] = cell_id

    # Add random noise to the fluorescence image
    noise = np.random.poisson(fluorescence_image * noise_level).astype(np.uint16)
    fluorescence_image = np.clip(fluorescence_image + noise, 0, 2**16 - 1)

    return fluorescence_image, labeled_image

# Parameters

import argparse

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Generate synthetic image parameters.")

# Define command-line arguments with both positional and named options
parser.add_argument("--width", type=int, required=True, help="Width of the image")
parser.add_argument("--height", type=int, required=True, help="Height of the image")
parser.add_argument("--num_cells", type=int, required=True, help="Number of cells")
parser.add_argument("--fluorescence_level_range", type=int, nargs=2, required=True, 
                    help="Fluorescence level range as two values: min max")
parser.add_argument("--size_range", type=int, nargs=2, required=True, help="Cell size range as two values: min max")

# Parse the arguments
args = parser.parse_args()

# Assign arguments to variables
width = args.width
height = args.height
num_cells = args.num_cells
fluorescence_level_range = tuple(args.fluorescence_level_range)
size_range = tuple(args.size_range)

# Print to verify
print("Width:", width)
print("Height:", height)
print("Number of cells:", num_cells)
print("Fluorescence level range:", fluorescence_level_range)
print("Size range:", size_range)

# Generate synthetic images
fluorescence_image, labeled_image = generate_synthetic_image(width, height, num_cells, fluorescence_level_range, size_range)

# Display the generated images
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Fluorescence image
ax[0].imshow(fluorescence_image, cmap='hot')
ax[0].set_title('Fluorescence Image')
ax[0].axis('off')

# Labeled image
ax[1].imshow(labeled_image, cmap='nipy_spectral')
ax[1].set_title('Labeled Image')
ax[1].axis('off')

plt.tight_layout()
plt.show()
plt.savefig("synthetic_image_generator.png")
