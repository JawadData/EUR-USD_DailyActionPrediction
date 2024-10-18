# EUR/USD Stock Prediction Project
This project predicts daily actions for the EUR/USD stock market using deep learning models. It includes API integration, model training, and a web interface with Flask for visualization.
---

## Requirements
1. Google Drive account linked to Google Colab.
2. Python installed locally for running the Flask app.
3. Colab access for running Jupyter notebooks.
---
l
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
