import os
import cv2
import numpy as np
import pandas as pd
import logging
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray

from skimage.util import img_as_ubyte

def get_glcm_features(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_img = rgb2gray(img)
    
    # Convert the float image to unsigned byte
    gray_img = img_as_ubyte(gray_img)
    
    # Calculate the gray-level co-occurrence matrix
    glcm = graycomatrix(gray_img, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    
    # Calculate the properties of the glcm
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    dissimilarity = graycoprops(glcm, 'dissimilarity')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    
    return contrast, dissimilarity, homogeneity, energy, correlation

def process_images_additional(folder_path):
    # Create a list to store the glcm features data
    glcm_data = []
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Get the full image path
            image_path = os.path.join(folder_path, filename)
            
            # Calculate and store glcm features
            contrast, dissimilarity, homogeneity, energy, correlation = get_glcm_features(image_path)
            glcm_data.append({'Image': filename, 'Contrast': contrast, 'Dissimilarity': dissimilarity, 'Homogeneity': homogeneity, 'Energy': energy, 'Correlation': correlation})
    
    # Convert the list to a DataFrame
    glcm_df = pd.DataFrame(glcm_data)
    
    # Save the glcm features data to a csv file
    glcm_df.to_csv('glcm_features.csv', index=False)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    process_images_additional('path_to_your_folder')
