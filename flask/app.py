from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now().strftime('%d %B %Y')
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%d %B %Y')
    return render_template('index.html', today=today, tomorrow=tomorrow)

@app.route('/predict', methods=['POST'])
def predict():

    today = datetime.now()
    if today.weekday() in (4, 5):  
        return jsonify({"message": "The market is closed on weekends. No predictions available."}), 200

    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    formatted_path = parent_path.replace('\\', '/')
    formatted_path = formatted_path.replace('/', '//')

    target_path = f'{formatted_path}//notebook_model_classification//output_models.json'

    try:
        with open(target_path, 'r') as json_file:
            features = json.load(json_file)  
        return jsonify(features) 
    except FileNotFoundError:
        return jsonify({"error": "Fichier non trouvé"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Erreur lors de la lecture du fichier JSON"}), 500

if __name__ == '__main__':
    app.run(debug=True)
