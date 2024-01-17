import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import logging

def get_image_histogram(image_path):
    logging.info(f'Generating histogram for {image_path}')
    # Read the image
    img = cv2.imread(image_path)
    
    # Calculate histogram using cv2.calcHist function
    color = ('b','g','r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr, color = col)
        plt.xlim([0,256])
    
    # Create a separate folder for histograms if it doesn't exist
    if not os.path.exists('histograms'):
        os.makedirs('histograms')

    # Extract the image name from the image path
    image_name = os.path.basename(image_path)

    # Save the plot in the histograms folder
    plt.savefig(f'histograms/{image_name}_histogram.png')
    plt.close()
    logging.info(f'Histogram saved as histograms/{image_name}_histogram.png')

def get_pixel_std(image_path):
    logging.info(f'Calculating standard deviation for {image_path}')
    # Read the image
    img = cv2.imread(image_path)
    
    # Calculate standard deviation of pixel values for each channel
    std_dev = cv2.meanStdDev(img)
    
    return std_dev

def process_images(folder_path):
    logging.info(f'Processing images in {folder_path}')
    # Create a list to store the standard deviation data
    std_dev_data = []
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Get the full image path
            image_path = os.path.join(folder_path, filename)
            
            # Generate and save histogram
            get_image_histogram(image_path)
            
            # Calculate and store standard deviation
            std_dev = get_pixel_std(image_path)
            std_dev_data.append({'Image': filename, 'Blue_Channel': std_dev[1][0][0], 'Green_Channel': std_dev[1][1][0], 'Red_Channel': std_dev[1][2][0]})
    
    # Convert the list to a DataFrame
    std_dev_df = pd.DataFrame(std_dev_data)
    
    # Save the standard deviation data to a csv file
    std_dev_df.to_csv('pixel_std_dev.csv', index=False)
    logging.info('Standard deviation data saved to pixel_std_dev.csv')

if __name__ == "__main__":
    process_images('path_to_your_folder')
