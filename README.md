## TMST Camera Image Quality Analysis

This project aims to filter out good images from bad ones captured by the TMST camera. The quality of these images significantly impacts the accuracy of subsequent measurements. I used basic CV techniques to do this. This is meant to be helpful, but no pressure to use these.

### Techniques Used
1. Image Histograms: I generated histograms for each image to visualize the distribution of pixel intensities. This can help identify images with poor contrast or lighting conditions. The code for this is in [image_processing.py](image_processing.py) (lines 8-30).

2. Standard Deviation of Pixel Values: I calculated the standard deviation of pixel values for each color channel (Red, Green, Blue) in each image. Images with very low or very high standard deviations might be of poor quality. This is also in [image_processing.py](image_processing.py) (lines 32-40).

3. Data Analysis: I performed some basic statistical analysis on the standard deviation data and plotted it for better visualization. This is done in [data_analysis.py](data_analysis.py) (lines 6-36).

4. Gray-Level Co-occurrence Matrix (GLCM) Features: I calculated GLCM features (contrast, dissimilarity, homogeneity, energy, correlation) for each image. These features are probably the best indicators of good vs bad images. I talk about this in the slide deck I made. This is done in [additional_analysis.py](additional_analysis.py) (lines 11-31).