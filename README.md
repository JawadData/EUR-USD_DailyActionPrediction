# EUR/USD Stock Prediction Project
This project predicts daily actions for the EUR/USD stock market using deep learning models. It includes API integration, model training, and a web interface with Flask for visualization.
---

## Project Architecture
![Project Architecture](architecture-diagram.png)
---

### Overview

This architecture diagram outlines the workflow of the EUR/USD stock prediction project. Below is a breakdown of the key components:

1. **Data Source**: Market data is retrieved from Yahoo Finance in Parquet format using Python for efficient storage and processing.
2. **Data Processing**: The data is transformed and prepared for training both regression and classification models.
3. **Model Training**:
   - **Regression Models**: These models analyze historical stock data to predict key price points (open, close, high, low).
   - **Classification Model**: This model classifies the predicted actions (Buy/Sell) based on features generated from the regression results.
4. **First Output**: Predictions from the regression models are saved in JSON format for easy access and further analysis.
5. **Additional Data Processing**: The regression model predictions are incorporated into the original Parquet file to generate new features, which are then used to train the classification model.
6. **Second Output**: Predictions from the classification model (Buy/Sell actions) are also saved in JSON format for easy access.
7. **Web Interface**: A Flask-based web application displays the predictions to users through an interactive interface.

---



## Project Overview
- **Languages:** Python, Jupyter (for Colab)
- **Tools/Technologies:** Flask, Colab, Google Drive, Deep Learning models

## Requirements
1. Google Drive account linked to Google Colab.
2. Python 3.x installed locally for running the Flask app.
3. Colab access for running Jupyter notebooks.

## Setup Instructions




### Overview
The architecture diagram illustrates the workflow of the EUR/USD stock prediction project. Here’s a breakdown of the components:
1. **Data Source**: Data is fetched from Yahoo Finance.
2. **Data Processing**: The data is converted into Parquet format for efficient storage and processing.
3. **Model Training**:
   - **Regression Models**: These models analyze historical data to predict stock trends.
   - **Classification Model**: This model classifies the predicted actions (Buy/Sell).
4. **Results**: The predictions are saved in JSON format for easy access.
5. **Web Interface**: A Flask application presents the predictions to users.

## Future Improvements
- Automate the retraining process using Airflow and Docker.
- Deploy the app via a cloud provider (e.g., Heroku, AWS).
