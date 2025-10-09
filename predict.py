# import joblib
# import pandas as pd
# from data_preprocessing import load_data
# import os
# import numpy as np

# # Load trained model
# model_path = os.path.join(os.path.dirname(__file__), "disease_prediction_model.pkl")
# model = joblib.load(model_path)

# # Load dataset features to map symptoms
# X, _ = load_data(os.path.join(os.path.dirname(__file__), "Training.csv"))
# symptom_columns = list(X.columns)

# # Load additional datasets
# description_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "description.csv"))
# diet_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "diets.csv"))
# medications_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "medications.csv"))
# precautions_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "precautions_df.csv"))
# workout_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "workout_df.csv"))

# def predict_disease(symptoms):
#     symptom_vector = np.zeros(len(symptom_columns))
#     matched_symptoms = []

#     for symptom in symptoms:
#         symptom = symptom.lower().strip()
#         for known_symptom in symptom_columns:
#             if symptom in known_symptom:  # Partial matching
#                 symptom_vector[symptom_columns.index(known_symptom)] = 1
#                 matched_symptoms.append(known_symptom)
    
#     if not matched_symptoms:
#         return "No matching symptoms found"

#     prediction = model.predict([symptom_vector])[0]
#     return prediction

# def get_disease_description(disease):
#     result = description_df[description_df["Disease"].str.lower() == disease.lower()]["Description"]
#     return result.values[0] if not result.empty else "Description not available."

# def get_diet_recommendation(disease):
#     result = diet_df[diet_df["Disease"].str.lower() == disease.lower()]["Diet"]
#     return result.values[0] if not result.empty else "Diet recommendations not available."

# def get_medication_recommendation(disease):
#     result = medications_df[medications_df["Disease"].str.lower() == disease.lower()]["Medications"]
#     return result.values[0] if not result.empty else "Medication recommendations not available."

# def get_precaution_recommendation(disease):
#     result = precautions_df[precautions_df["Disease"].str.lower() == disease.lower()]["Precaution_1"]
#     return result.values[0] if not result.empty else "Precaution recommendations not available."

# def get_workout_recommendation(disease):
#     result = workout_df[workout_df["Disease"].str.lower() == disease.lower()]["workout"]
#     return result.values[0] if not result.empty else "Workout recommendations not available."


import joblib
import numpy as np
import pandas as pd
import os
import difflib

# Load the trained model, feature names, and label encoder saved during training
model_path = os.path.join(os.path.dirname(__file__), "disease_prediction_model.pkl")
model = joblib.load(model_path)
feature_names = joblib.load("feature_names.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Load additional datasets for recommendations
description_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "description.csv"))
diet_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "diets.csv"))
medications_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "medications.csv"))
precautions_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "precautions_df.csv"))
workout_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "workout_df.csv"))

def predict_disease(symptoms):
    # Create a symptom vector using the saved feature names (expects 132 features)
    symptom_vector = np.zeros(len(feature_names))
    matched_symptoms = []
    
    # Use fuzzy matching to map each input symptom to the closest known feature name
    for symptom in symptoms:
        symptom = symptom.lower().strip()
        matches = difflib.get_close_matches(symptom, feature_names, n=1, cutoff=0.8)
        if matches:
            best_match = matches[0]
            index = feature_names.index(best_match)
            symptom_vector[index] = 1
            matched_symptoms.append(best_match)
    
    if not matched_symptoms:
        return "No matching symptoms found"
    
    # Predict the disease using the model
    prediction_encoded = model.predict([symptom_vector])[0]
    # Convert the numeric prediction back into the original disease name
    prediction = label_encoder.inverse_transform([prediction_encoded])[0]
    
    return prediction

def get_disease_description(disease):
    result = description_df[description_df["Disease"].str.lower() == disease.lower()]["Description"]
    return result.values[0] if not result.empty else "Description not available."

def get_diet_recommendation(disease):
    result = diet_df[diet_df["Disease"].str.lower() == disease.lower()]["Diet"]
    return result.values[0] if not result.empty else "Diet recommendations not available."

def get_medication_recommendation(disease):
    result = medications_df[medications_df["Disease"].str.lower() == disease.lower()]["Medications"]
    return result.values[0] if not result.empty else "Medication recommendations not available."

def get_precaution_recommendation(disease):
    result = precautions_df[precautions_df["Disease"].str.lower() == disease.lower()]["Precaution_1"]
    return result.values[0] if not result.empty else "Precaution recommendations not available."

def get_workout_recommendation(disease):
    result = workout_df[workout_df["Disease"].str.lower() == disease.lower()]["workout"]
    return result.values[0] if not result.empty else "Workout recommendations not available."
