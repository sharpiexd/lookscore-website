from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from PIL import Image
import io
import base64
import json
import numpy as np

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates'
)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get the uploaded images
        front_image = request.files.get('frontImage')
        side_image = request.files.get('sideImage')

        if not front_image or not side_image:
            return jsonify({'error': 'Both front and side images are required'}), 400

        # Process front image
        front_img = Image.open(front_image)
        # Process side image
        side_img = Image.open(side_image)

        # Perform analysis (your existing analysis code here)
        analysis_results = perform_analysis(front_img, side_img)
        
        return jsonify(analysis_results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def perform_analysis(front_img, side_img):
    # Your existing analysis code here
    # This is a placeholder that returns dummy data
    return {
        'scores': {
            'eyes': 8.5,
            'nose': 7.8,
            'lips': 8.0,
            'jawline': 8.2,
            'cheekbones': 8.4,
            'symmetry': 8.6
        },
        'measurements': {
            'interpupillaryDistance': 63,
            'canthalTilt': 4,
            'nasalProjection': 34,
            'jawAngle': 130
        },
        'shapes': {
            'face': 'Oval',
            'eyes': 'Almond'
        }
    }

if __name__ == '__main__':
    # Use environment variable for port with a default value
    port = int(os.environ.get('PORT', 5000))
    # In production, disable debug mode
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
