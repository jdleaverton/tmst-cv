import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def analyze_data():

    logging.info('Loading the standard deviation data')
    std_dev_df = pd.read_csv('pixel_std_dev.csv')

    logging.info('Displaying the data')
    print(std_dev_df)

    logging.info('Plotting the standard deviation data')
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=std_dev_df.drop(['Image'], axis=1))
    plt.title('Standard Deviation of Pixel Values for Each Channel')
    plt.xlabel('Image Index')
    plt.ylabel('Standard Deviation')
    plt.savefig('std_dev_plot.png')
    plt.close()

    logging.info('Calculating and displaying some basic statistics')
    print("Basic Statistics:\n", std_dev_df.describe())

    logging.info('Calculating and displaying the correlation matrix')
    # Exclude 'Image' column when calculating the correlation matrix
    correlation_matrix = std_dev_df.drop('Image', axis=1).corr()
    print("Correlation Matrix:\n", correlation_matrix)

    logging.info('Plotting the correlation matrix')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Standard Deviation of Pixel Values for Each Channel')
    plt.savefig('correlation_matrix.png')
    plt.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    analyze_data()
