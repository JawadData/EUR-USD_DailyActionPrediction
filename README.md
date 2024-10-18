# EUR/USD Stock Prediction Project
This project predicts daily actions for the EUR/USD stock market using deep learning models. It includes API integration, model training, and a web interface with Flask for visualization.
---

## Requirements

1. A Google Drive account linked to Google Colab for data storage and notebook execution.
2. Python installed locally to run the Flask web application.
---

## Project Architecture
![Project Architecture](architecture-diagram.png)
---

### Overview

This architecture diagram outlines the workflow of the EUR/USD stock prediction project. Below is a breakdown of the key components:

1. **Data Source**: Market data is retrieved from Yahoo Finance in Parquet format using Python, ensuring efficient storage and processing.
2. **Data Processing**: The data is transformed and prepared for the training of both regression and classification models.
3. **Model Training**:
   - **Regression Models**: These models analyze historical stock data to predict key price points (open, close, high, low).
   - **Classification Model**: This model classifies the predicted actions (Buy/Sell) based on rules derived from key price points.
4. **First Output**: Predictions from the regression models are stored in JSON format for easy access and further analysis.
5. **Additional Data Processing**: The predictions from the regression models are integrated into the original Parquet file to generate new rules for the next day's predictions, which are then used as input for the classification model.
6. **Second Output**: Predictions from the classification model (Buy/Sell actions) are also stored in JSON format for easy access.
7. **Web Interface**: A Flask-based web application provides users with an interactive interface to view the predictions.
---

## Setup Instructions

1. **Repository Location**: Upload the repository to the "My Drive" section of your Google Drive account. Ensure that you are using the same account you log in to Google Colab with.

2. **Notebook Execution**: Import the notebook named "run_me" into Colab and execute it. This will train the models and automatically save the results.

3. **Export the Repository**: After executing the notebook, the modifications will be automatically saved to the repository on your Google Drive. You can then export this repository.

4. **Run the Application**: Using a terminal, navigate to the extracted repository, then enter the "flask" directory. Run the following command to start the application:  
   ```bash
   python app.py



## Future Improvements
- Automate the retraining process using Airflow.
- Deploy the app via a cloud provider (e.g., Heroku, AWS).
