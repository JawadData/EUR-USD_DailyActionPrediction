# EUR/USD Stock Prediction Project
This project predicts daily actions for the EUR/USD stock market using deep learning models. It includes API integration, model training, and a web interface with Flask for visualization.
---

## Project Architecture
![Project Architecture](architecture-diagram.png)
---

### Overview
The architecture diagram illustrates the workflow of the EUR/USD stock prediction project. Below is a breakdown of the key components:

1. **Data Source**: Market data is retrieved from Yahoo Finance.
2. **Data Processing**: The data is transformed into Parquet format for efficient storage and processing.
3. **Model Training**:
   - **Regression Models**: These models analyze historical data to predict stock price trends.
   - **Classification Model**: This model classifies the predicted actions (Buy/Sell) based on the generated features.
4. **First Result**: Predictions from the regression models are saved in JSON format for easy access and further use.
5. **Further Data Processing**: The results from the regression models are added back to the original Parquet file for reprocessing and the creation of new features for the classification model.
6. **Second Result**: Predictions from the classification model (Buy/Sell actions) are also saved in JSON format for easy access.
7. **Web Interface**: A Flask-based web application is used to present the predictions to the users via an interactive interface.
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
