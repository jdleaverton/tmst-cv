import image_processing
import data_analysis
import additional_analysis
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Define the path to the folder containing the images
    folder_path = 'images'

    # Process the images to generate histograms and calculate standard deviations
    image_processing.process_images(folder_path)

    # Analyze the standard deviation data
    data_analysis.analyze_data()

    # Perform additional analysis on the images
    additional_analysis.process_images_additional(folder_path)

if __name__ == "__main__":
    main()
