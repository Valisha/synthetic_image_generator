import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import disk
import random

def generate_synthetic_image(width, height, num_cells, fluorescence_level_range, size_range, shape='disk', noise_level=0.1):
    if num_cells > 255:
        print("Supported cell numbers <= 255, input value exceeded: "+str(num_cells))
    fluorescence_image = np.zeros((height, width), dtype=np.uint16)
    labeled_image = np.zeros((height, width), dtype=np.uint8)

    for cell_id in range(1, num_cells + 1):
        cell_radius = random.randint(size_range[0], size_range[1])
        fluorescence_level = random.randint(fluorescence_level_range[0], fluorescence_level_range[1])
        cell_center = (random.randint(cell_radius, height - cell_radius),
                       random.randint(cell_radius, width - cell_radius))

        if shape == 'disk':
            rr, cc = disk(cell_center, cell_radius, shape=fluorescence_image.shape)
            fluorescence_image[rr, cc] += fluorescence_level
            labeled_image[rr, cc] = cell_id

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

## Generate the flourescence and the labeled image
fluorescence_image, labeled_image = generate_synthetic_image(width, height, num_cells, fluorescence_level_range, size_range)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Display the fluorescence image with colorbar
img1 = ax[0].imshow(fluorescence_image, cmap='hot')
ax[0].set_title('Fluorescence Image')
ax[0].axis('off')
cbar1 = plt.colorbar(img1, ax=ax[0], fraction=0.046, pad=0.04)
cbar1.set_label('Fluorescence Intensity')

# Display the labeled image with colorbar
img2 = ax[1].imshow(labeled_image, cmap='nipy_spectral')
ax[1].set_title('Labeled Image')
ax[1].axis('off')
cbar2 = plt.colorbar(img2, ax=ax[1], fraction=0.046, pad=0.04)
cbar2.set_label('Cell ID')

plt.tight_layout()
plt.savefig("synthetic_image_generator.png")
plt.show()

