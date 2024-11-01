function generate_synthetic_image(width, height, num_cells, fluorescence_level_range, size_range, noise_level)
    if num_cells > 255
        fprintf('Supported cell numbers <= 255, input value exceeded: %d\n', num_cells);
        return;
    end

    fluorescence_image = zeros(height, width, 'uint16');
    labeled_image = zeros(height, width, 'uint8');

    for cell_id = 1:num_cells
        cell_radius = randi(size_range);
        fluorescence_level = randi(fluorescence_level_range);
        cell_center = [randi([cell_radius, height - cell_radius]), randi([cell_radius, width - cell_radius])];

        % Create a disk shape for the cell
        [X, Y] = ndgrid((1:height) - cell_center(1), (1:width) - cell_center(2));
        mask = sqrt(X.^2 + Y.^2) <= cell_radius;

        fluorescence_image(mask) = min(fluorescence_image(mask) + fluorescence_level, 2^16 - 1);
        labeled_image(mask) = cell_id;
    end

    % Add noise
    noise = poissrnd(double(fluorescence_image) * noise_level);
    fluorescence_image = min(double(fluorescence_image) + noise, 2^16 - 1);
    
    % Display images
    figure;

    % Fluorescence image
    subplot(1, 2, 1);
    imshow(fluorescence_image, [], 'InitialMagnification', 'fit');
    title('Fluorescence Image');
    colorbar;
    colormap('hot');

    % Labeled image
    subplot(1, 2, 2);
    imshow(labeled_image, [], 'InitialMagnification', 'fit');
    title('Labeled Image');
    colorbar;
    colormap('jet'); % or 'nipy_spectral'

    % Save the figure
    saveas(gcf, 'synthetic_image_generator.png');
end

% Example of how to call the function
% generate_synthetic_image(512, 512, 100, [1, 255], [5, 20], 0.1);

