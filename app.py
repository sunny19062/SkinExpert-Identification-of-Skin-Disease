# some utilities
import os
import numpy as np
import util

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

#tensorflow
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2


# Variables 
# Change them if you are using custom model or pretrained model with saved weigths
Model_json = "model.json"
Model_weigths = "model_weights.h5"


# Declare a flask app
app = Flask(__name__)

def get_ImageClassifierModel():
    # model = MobileNetV2(weights='imagenet')

    # Loading the pretrained model
    
    #
    # Load model architecture from JSON file
    # with open('model.json', 'r') as json_file:
    #     loaded_model_json = json_file.read()
    # loaded_model = tf.keras.model_from_json(loaded_model_json)

    # # Load model weights from H5 file
    # loaded_model.load_weights('model_weights.h5')
    model_json = open(Model_json, 'r')
    loaded_model_json = model_json.read()
    model_json.close()
    model = model_from_json(loaded_model_json)
    model.load_weights('model_weights.h5')
    # model=load_model('29class76.h5')
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    return model 
    


def model_predict(img, model):
    '''
    Prediction Function for model.
    Arguments: 
        img: is address to image
        model : image classification model
    '''
    img = img.resize((224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    print(preds)

    return preds


@app.route('/', methods=['GET'])
def index():
    '''
    Render the main page
    '''
    return render_template('index.html')

@app.route('/comingsoon', methods=['GET'])
def comingsoon():
    '''
    Render the child page
    '''
    return render_template('comingsoon.html')

@app.route('/Diseases/Acne', methods=['GET'])
def Acne():
    '''
    Render the child page
    '''
    return render_template('Diseases/Acne.html')
@app.route('/Diseases/DefaultDescription', methods=['GET'])
def DefaultDescription():
    '''
    Render the child page
    '''
    return render_template('Diseases/DefaultDescription.html')
@app.route('/Diseases/Acitinic', methods=['GET'])
def Actinic():
    '''
    Render the child page
    '''
    return render_template('Diseases/Actinic.html')
@app.route('/Diseases/AtopicDermatitis', methods=['GET'])
def AtopicDermatitis():
    '''
    Render the child page
    '''
    return render_template('Diseases/AtopicDermatitis.html')
@app.route('/Diseases/Psoriasis', methods=['GET'])
def Psoriasis():
    '''
    Render the child page
    '''
    return render_template('Diseases/Psoriasis.html')
@app.route('/Diseases/LupusChronic', methods=['GET'])
def LupusChronic():
    '''
    Render the child page
    '''
    return render_template('Diseases/LupusChronic.html')
@app.route('/Diseases/NailDisease', methods=['GET'])
def NailDisease():
    '''
    Render the child page
    '''
    return render_template('Diseases/NailDisease.html')
@app.route('/Diseases/AllergicContactDematitis', methods=['GET'])
def AllergicContactDematitis():
    '''
    Render the child page
    '''
    return render_template('Diseases/AllergicContactDematitis.html')
@app.route('/Diseases/Alopecia', methods=['GET'])
def Alopecia():
    '''
    Render the child page
    '''
    return render_template('Diseases/Alopecia.html')
@app.route('/Diseases/BasalCell', methods=['GET'])
def BasalCell():
    '''
    Render the child page
    '''
    return render_template('Diseases/BasalCell.html')
@app.route('/Diseases/AtypicalNevi', methods=['GET'])
def AtypicalNevi():
    '''
    Render the child page
    '''
    return render_template('Diseases/AtypicalNevi.html')
@app.route('/Diseases/Bullous', methods=['GET'])
def Bullous():
    '''
    Render the child page
    '''
    return render_template('Diseases/Bullous.html')
@app.route('/Diseases/Cellulitis', methods=['GET'])
def Cellulitis():
    '''
    Render the child page
    '''
    return render_template('Diseases/Cellulitis.html')
@app.route('/Diseases/DrugEruptions', methods=['GET'])
def DrugEruptions():
    '''
    Render the child page
    '''
    return render_template('Diseases/DrugEruptions.html')
@app.route('/Diseases/Eczema', methods=['GET'])
def Eczema():
    '''
    Render the child page
    '''
    return render_template('Diseases/Eczema.html')
@app.route('/Diseases/ErythemaMultiforme', methods=['GET'])
def ErythemaMultiforme():
    '''
    Render the child page
    '''
    return render_template('Diseases/ErythemaMultiforme.html')
@app.route('/Diseases/Exanthems', methods=['GET'])
def Exanthems():
    '''
    Render the child page
    '''
    return render_template('Diseases/Exanthems.html')
@app.route('/Diseases/Hemangioma', methods=['GET'])
def Hemangioma():
    '''
    Render the child page
    '''
    return render_template('Diseases/Hemangioma.html')
@app.route('/Diseases/HerpesSTDs', methods=['GET'])
def HerpesSTDs():
    '''
    Render the child page
    '''
    return render_template('Diseases/HerpesSTDs.html')
@app.route('/Diseases/HivesUrticaria', methods=['GET'])
def HivesUrticaria():
    '''
    Render the child page
    '''
    return render_template('Diseases/HivesUrticaria.html')
@app.route('/Diseases/LicheenPlanus', methods=['GET'])
def LicheenPlanus():
    '''
    Render the child page
    '''
    return render_template('Diseases/LicheenPlanus.html')
@app.route('/Diseases/LightDisease', methods=['GET'])
def LightDisease():
    '''
    Render the child page
    '''
    return render_template('Diseases/LightDisease.html')
@app.route('/Diseases/MolluscumContagiosum', methods=['GET'])
def MolluscumContagiosum():
    '''
    Render the child page
    '''
    return render_template('Diseases/MolluscumContagiosum.html')
@app.route('/Diseases/Pyogenic', methods=['GET'])
def Pyogenic():
    '''
    Render the child page
    '''
    return render_template('Diseases/Pyogenic.html')
@app.route('/Diseases/Rosacea', methods=['GET'])
def Rosacea():
    '''
    Render the child page
    '''
    return render_template('Diseases/Rosacea.html')
@app.route('/Diseases/Scabies', methods=['GET'])
def Scabies():
    '''
    Render the child page
    '''
    return render_template('Diseases/Scabies.html')
@app.route('/Diseases/Seborrheic', methods=['GET'])
def Seborrheic():
    '''
    Render the child page
    '''
    return render_template('Diseases/Seborrheic.html')
@app.route('/Diseases/TineaRingworm', methods=['GET'])
def TineaRingworm():
    '''
    Render the child page
    '''
    return render_template('Diseases/TineaRingworm.html')
@app.route('/Diseases/Vasculitis', methods=['GET'])
def Vasculitis():
    '''
    Render the child page
    '''
    return render_template('Diseases/Vasculitis.html')
@app.route('/Diseases/Warts', methods=['GET'])
def Warts():
    '''
    Render the child page
    '''
    return render_template('Diseases/Warts.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    '''
    predict function to predict the image
    Api hits this function when someone clicks submit.
    '''
    if request.method == 'POST':
        # Get the image from post request
        img = util.base64_to_pil(request.json)
        
        # initialize model
        model = get_ImageClassifierModel()

        # # Make prediction
        # preds = model_predict(img, model)

        # pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        # # pred_class=np.argmax(preds)
        # # pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        # # result = str(preds)               # Convert to string
        # # result = result.replace('_', ' ').capitalize()
        
        # # Serialize the result, you can add additional fields
        # # return jsonify(result=result, probability=pred_proba)
        # pred_class_id = np.argmax(preds)  # Get predicted class ID
        # pred_one_hot = preds.tolist()
        # response = {
        # 'predicted_class_id': preds.tolist(),
        # 'predicted_one_hot_array': pred_one_hot,
        # 'predicted_probability': pred_proba
        # }
        # return jsonify(result=response,probability=pred_proba)
         # Make prediction
        preds = model_predict(img, model)  # Get predicted probabilities

        pred_class_id = int(np.argmax(preds))  # Get predicted class ID and convert to int
        pred_one_hot = preds.tolist()  # Convert predicted probabilities to a list (one-hot array)

        pred_proba = "{:.3f}".format(np.amax(preds))  # Max probability

        # Prepare the JSON response
        response = {
            'predicted_class_id': pred_class_id,
            'predicted_one_hot_array': pred_one_hot,
            'predicted_probability': pred_proba
        }

        # Return the JSON response
        return jsonify(result=response,probability=pred_class_id)
    return None


if __name__ == '__main__':
    # app.run(port=5002)
    app.run()