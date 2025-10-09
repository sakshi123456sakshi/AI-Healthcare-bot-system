# from flask import Flask, request, jsonify, render_template
# from predict import predict_disease, get_disease_description, get_diet_recommendation, get_medication_recommendation, get_precaution_recommendation, get_workout_recommendation
# import speech_recognition as sr
# import os
# from data_preprocessing import load_data
# import joblib
# import numpy as np

# app = Flask(__name__)

# # Load trained model
# model_path = os.path.join(os.path.dirname(__file__), "disease_prediction_model.pkl")
# model = joblib.load(model_path)

# # Load dataset features to map symptoms
# X, _ = load_data(os.path.join(os.path.dirname(__file__), "Training.csv"))
# symptom_columns = list(X.columns)

# # def recognize_speech():
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening for symptoms...")
# #         try:
# #             audio = recognizer.listen(source)
# #             text = recognizer.recognize_google(audio)
# #             return text
# #         except sr.UnknownValueError:
# #             return "Could not understand audio"
# #         except sr.RequestError:
# #             return "Error connecting to speech recognition service"


# def predict_disease(symptoms):
#     symptom_vector = np.zeros(len(symptom_columns))
#     found = False
#     for symptom in symptoms:
#         symptom = symptom.lower().strip()
#         if symptom in symptom_columns:
#             symptom_vector[symptom_columns.index(symptom)] = 1
#             found = True
    
#     if not found:
#         return "No matching symptoms found"
    
#     prediction = model.predict([symptom_vector])[0]
#     return prediction

# @app.route('/')
# def home():
#     return render_template("index.html")
# @app.route('/aboutus')
# def aboutus():
#     return render_template("aboutus.html")

# @app.route('/contactus')
# def contactus():
#     return render_template("contactus.html")

# @app.route('/feedback')
# def feedback():
#     return render_template("feedback.html")
    
# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     user_input = request.json.get("message")
    
#     if not user_input:
#         return jsonify({"response": "Invalid input. Please provide a message."})
    
#     user_input = user_input.strip().lower()
    
#     if "symptoms" in user_input:
#         symptoms = user_input.split(':')[-1].split(',')
#         symptoms = [s.strip() for s in symptoms]
#         disease = predict_disease(symptoms)
#         if disease == "No matching symptoms found":
#             response = "Sorry, I couldn't recognize those symptoms. Please provide valid symptoms."
#         else:
#             response = f"Based on the symptoms, you might have {disease}. Would you like to know more? (yes/no)"
    
#     elif user_input == "yes":
#         response = "What would you like to know? Options: description, diet, medications, precautions, workout."
    
#     elif "description" in user_input:
#         disease = user_input.split(':')[-1].strip()
#         response = get_disease_description(disease)
    
#     elif "diet" in user_input:
#         disease = user_input.split(':')[-1].strip()
#         response = get_diet_recommendation(disease)
    
#     elif "medications" in user_input:
#         disease = user_input.split(':')[-1].strip()
#         response = get_medication_recommendation(disease)
    
#     elif "precautions" in user_input:
#         disease = user_input.split(':')[-1].strip()
#         response = get_precaution_recommendation(disease)
    
#     elif "workout" in user_input:
#         disease = user_input.split(':')[-1].strip()
#         response = get_workout_recommendation(disease)
    
#     else:
#         response = "I'm not sure how to respond. You can ask about symptoms, disease descriptions, diet recommendations, medications, precautions, or workouts."
    
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)







from flask import Flask, request, jsonify, render_template
from predict import predict_disease, get_disease_description, get_diet_recommendation, get_medication_recommendation, get_precaution_recommendation, get_workout_recommendation
import speech_recognition as sr
import os
from data_preprocessing import load_data
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "disease_prediction_model.pkl")
model = joblib.load(model_path)

# Load dataset features to map symptoms
X, _ = load_data(os.path.join(os.path.dirname(__file__), "Training.csv"))
symptom_columns = list(X.columns)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"response": "Invalid input. Please provide a message."})

    user_input = user_input.strip().lower()

    if "symptoms" in user_input:
        symptoms = user_input.split(':')[-1].split(',')
        symptoms = [s.strip() for s in symptoms]
        disease = predict_disease(symptoms)
        if disease == "No matching symptoms found":
            response = "Sorry, I couldn't recognize those symptoms. Please provide valid symptoms."
        else:
            response = f"Based on the symptoms, you might have {disease}. Would you like to know more? (yes/no)"

    elif user_input == "yes":
        response = "What would you like to know? Options: description, diet, medications, precautions."

    elif "description" in user_input:
        disease = user_input.split(':')[-1].strip()
        response = get_disease_description(disease)

    elif "diet" in user_input:
        disease = user_input.split(':')[-1].strip()
        response = get_diet_recommendation(disease)

    elif "medications" in user_input:
        disease = user_input.split(':')[-1].strip()
        response = get_medication_recommendation(disease)

    elif "precautions" in user_input:
        disease = user_input.split(':')[-1].strip()
        response = get_precaution_recommendation(disease)

    elif "workout" in user_input:
        disease = user_input.split(':')[-1].strip()
        response = get_workout_recommendation(disease)

    else:
        response = "I'm not sure how to respond. You can ask about symptoms, disease descriptions, diet recommendations, medications, precautions."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
