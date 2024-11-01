# Synthetic Image Generator
### Author - Valisha Shah 
### Date - 11/01/2024

This repository has two scripts in the final_scripts directory, one in python and another in matlab in the final_script folder. (Python script is tested)
The function in the scripts are aimed to produce a synthetic flourescence image using the image descriptives as input and another labeled flourescent image. 

## Description of the main function

The main function takes several inputs which are to be provided by the user using command line 
Inputs - 
1. width 128 (numerical input)
2. height 128 (numerical input)
3. num_cells 10 (numerical input)
4. fluorescence_level_range 500 900 (range of values for the random generator to choose a flourescent level)
5. size_range 10 20 (range of values for the random generator to choose the size of the cell)


For this script I have used the libraries - 
1. numpy<sup>[1]</sup>
2. matplotlib.pyplot<sup>[2]</sup>
3. skimage.draw - Used to generate coordinates within a circle<sup>[3]</sup>
4. random
5. sys

## Additional factors that can affect a flourescence microscopy image 

1. <b>Photbleaching</b> - over time a flourescence microscopy image might loose intensity, due to flurophores being destroyed or losing their ability to fluroesce after prolonged exposure to the light. This can be corrected by relative flourescence effect. We can take into account how old the image, and set the flouresence threshold according to that. and also, consider relative flourescence in reference to the background
2. <b>Autoflouresce</b> - background flourescence from the preparation liquid or leakage. This can again be overcome by treating with relative flourescence and keeping a threshold of difference in the flourescence of the detected cell and the background flouresence if any.
3. <b>Optical Aberrations</b> - Imperfections in the imaging system, such as spherical or chromatic abberations, can cause blurring or distortions in the image, affecting its clariy and detail. This can be overcome by locating the center of the cell, and creating a probable circular cell using the radius and camera noise

*PS - I am more comfortable so, I was able to completely test the Python code and make changes, and convert the same code to a matlab code. But, I did not have enough time to completely test the matlab code*

## Experience doing this project
I really enjoyed working on this project. It was initially challenging because I had to grasp the specific requirements. However, once I understood what was needed and which libraries I could use, it became much easier. 
It might have been a bit more difficult if there had been an additional task to read an input fluorescence image and generate a labeled image from it. 
While I have some experience in this area, I haven’t tackled a project like this that required me to write a function to create synthetic images. It’s an exciting concept, and it has sparked several ideas for implementation in my current projects.

## References 
1. Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., & Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585(7825), 357-362. DOI: 10.1038/s41586-020-2649-2
2. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95. DOI: 10.1109/MCSE.2007.55
3. van der Walt S, Schönberger JL, Nunez-Iglesias J, Boulogne F, Warner JD, Yager N, Gouillart E, Yu T, the scikit-image contributors. 2014. scikit-image: image processing in Python. PeerJ 2:e453 https://doi.org/10.7717/peerj.453

