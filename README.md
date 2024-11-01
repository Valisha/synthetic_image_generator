# Synthetic Image Generator
### Author - Valisha Shah 
### Date - 11/01/2024

This repository has two scripts, one in python and another in matlab. (Python script is tested)
The function in the scripts are aimed to produce a synthetic flourescence image using the image descriptives as input and another labeled flourescent image. 

The main function takes several inputs which are to be provided by the user using command line 
Inputs - 
1. width 128 (numerical input)
2. height 128 (numerical input)
3. num_cells 10 (numerical input)
4. fluorescence_level_range 500 900 (range of values for the random generator to choose a flourescent level)
5. size_range 10 20 (range of values for the random generator to choose the size of the cell)


For this script I have used the functions - 
1. numpy<sup>[1]</sup>
2. matplotlib.pyplot<[2]>
3. skimage.draw - Used to generate coordinates within a circle<[3]>
4. random<[4]>
5. sys<[5]>

## References 
1. Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., & Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585(7825), 357-362. DOI: 10.1038/s41586-020-2649-2
2. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95. DOI: 10.1109/MCSE.2007.55
3. van der Walt S, Schönberger JL, Nunez-Iglesias J, Boulogne F, Warner JD, Yager N, Gouillart E, Yu T, the scikit-image contributors. 2014. scikit-image: image processing in Python. PeerJ 2:e453 https://doi.org/10.7717/peerj.453

