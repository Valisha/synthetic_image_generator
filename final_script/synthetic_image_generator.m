function [fluorescence_image, labeled_image] = generateSyntheticImage(width, height, num_cells, fluorescence_level_range, size_range, shape, noise_level)
    if nargin < 6
        shape = 'disk';
    end
    if nargin < 7
        noise_level = 0.1;
    end

    % Initialize fluorescence and labeled images
    fluorescence_image = zeros(height, width, 'uint16');
    labeled_image = zeros(height, width, 'uint8');

    for cell_id = 1:num_cells
        % Randomize cell properties
        cell_radius = randi(size_range);
        fluorescence_level = randi(fluorescence_level_range);
        cell_center = [randi([cell_radius + 1, height - cell_radius - 1]), ...
                       randi([cell_radius + 1, width - cell_radius - 1])];

        if strcmp(shape, 'disk')
            % Generate disk shape for the cell
            [rr, cc] = meshgrid(1:height, 1:width);
            mask = sqrt((rr - cell_center(1)).^2 + (cc - cell_center(2)).^2) <= cell_radius;
            
            % Update images
            fluorescence_image(mask) = fluorescence_image(mask) + fluorescence_level;
            labeled_image(mask) = cell_id;
        end
    end

    % Add random noise to fluorescence image
    noise = uint16(poissrnd(double(fluorescence_image) * noise_level));
    fluorescence_image = min(fluorescence_image + noise, 2^16 - 1);

    % Display results
    figure;
    subplot(1, 2, 1);
    imagesc(fluorescence_image);
    colormap('hot');
    title('Fluorescence Image');
    axis off;

    subplot(1, 2, 2);
    imagesc(labeled_image);
    colormap('nipy_spectral');
    title('Labeled Image');
    axis off;

    % Save the figure
    saveas(gcf, 'synthetic_image_generator.png');
end

% Parameters
width = 128;
height = 128;
num_cells = 9;
fluorescence_level_range = [500, 2500];
size_range = [5, 15];
shape = 'disk';
noise_level = 0.1;

% Generate synthetic images
[fluorescence_image, labeled_image] = generateSyntheticImage(width, height, num_cells, fluorescence_level_range, size_range, shape, noise_level);

