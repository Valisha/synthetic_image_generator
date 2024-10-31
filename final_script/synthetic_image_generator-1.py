import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import disk
import random

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
width = 128
height = 128
num_cells = 9
fluorescence_level_range = (500, 2500)
size_range = (5, 15)

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
