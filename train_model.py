# # import os
# # import pandas as pd
# # import joblib
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score
# # from data_preprocessing import load_data

# # def train_model():
# #     file_path = os.path.join(os.path.dirname(__file__), "Training.csv")
# #     X, y = load_data(file_path)
    
# #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# #     model = RandomForestClassifier(n_estimators=100, random_state=42)
# #     model.fit(X_train, y_train)
    
# #     y_pred = model.predict(X_test)
# #     print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
# #     joblib.dump(model, "disease_prediction_model.pkl")

# # if __name__ == "__main__":
# #     train_model()


# # import os
# # import pandas as pd
# # import joblib
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score
# # from data_preprocessing import load_data

# # def train_model():
# #     file_path = os.path.join(os.path.dirname(__file__), "Training.csv")
# #     X, y = load_data(file_path)
    
# #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# #     model = RandomForestClassifier(n_estimators=200, random_state=42)  # Increased estimators for better accuracy
# #     model.fit(X_train, y_train)
    
# #     y_pred = model.predict(X_test)
# #     print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
# #     joblib.dump(model, "disease_prediction_model.pkl")

# # if __name__ == "__main__":
# #     train_model()


# import os
# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from data_preprocessing import load_data

# def train_model():
#     file_path = os.path.join(os.path.dirname(__file__), "Training.csv")
#     X, y = load_data(file_path)
    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model = RandomForestClassifier(n_estimators=200, random_state=42)
#     model.fit(X_train, y_train)
    
#     y_pred = model.predict(X_test)
#     print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
#     joblib.dump(model, "disease_prediction_model.pkl")

# if __name__ == "__main__":
#     train_model()
# import os
# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from data_preprocessing import load_data

# def train_model():
#     file_path = os.path.join(os.path.dirname(__file__), "Training.csv")
#     X, y = load_data(file_path)
    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model = RandomForestClassifier(n_estimators=200, random_state=42)
#     model.fit(X_train, y_train)
    
#     y_pred = model.predict(X_test)
#     print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
#     joblib.dump(model, "disease_prediction_model.pkl")

# if __name__ == "__main__":
#     train_model()


# import os
# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from data_preprocessing import load_data

# def train_model():
#     file_path = os.path.join(os.path.dirname(__file__), "Training.csv")
#     X, y = load_data(file_path)
    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model = RandomForestClassifier(n_estimators=200, random_state=42)
#     model.fit(X_train, y_train)
    
#     y_pred = model.predict(X_test)
#     # print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
#     joblib.dump(model, "disease_prediction_model.pkl")

# if __name__ == "__main__":
#     train_model()







import os
import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    df = pd.read_csv(file_path)

    # Remove unnecessary columns if present
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")

    # Encode categorical disease labels and save the encoder for prediction
    if "Disease" in df.columns:
        label_encoder = LabelEncoder()
        df["Disease"] = label_encoder.fit_transform(df["Disease"])
        joblib.dump(label_encoder, "label_encoder.pkl")  # Save for later use

    # Encode any other categorical columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = LabelEncoder().fit_transform(df[col])

    # Extract features (all 132 symptom columns) and target
    X = df.drop(columns=["Disease"], errors="ignore")
    y = df["Disease"]

    # Save feature names for prediction consistency
    joblib.dump(X.columns.tolist(), "feature_names.pkl")

    return X, y

def train_model():
    file_path = os.path.join(os.path.dirname(__file__), "Training.csv")
    X, y = load_data(file_path)

    # Ensure we have 132 features as expected
    if len(X.columns) != 132:
        raise ValueError(f"Expected 132 features, but got {len(X.columns)}")

    # Stratified train-test split to maintain disease distribution
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Define a simpler Random Forest model to reduce overfitting
    model = RandomForestClassifier(
        n_estimators=15,          # Fewer trees
        max_depth=4,              # Shallow trees
        min_samples_split=30,     # Require more samples to split
        min_samples_leaf=20,      # Larger leaf nodes
        max_features='sqrt',      # Use a subset of features
        bootstrap=True,
        max_samples=0.5,          # Each tree sees 50% of the training data
        class_weight='balanced',
        random_state=42
    )

    # Train model on all 132 features
    model.fit(X_train, y_train)

    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Calculate accuracy
    train_accuracy = accuracy_score(y_train, y_train_pred) * 100
    test_accuracy = accuracy_score(y_test, y_test_pred) * 100

    print(f"Training Accuracy: {train_accuracy:.2f}%")
    print(f"Test Accuracy: {test_accuracy:.2f}%")

    # Save the trained model
    joblib.dump(model, "disease_prediction_model.pkl")

if __name__ == "__main__":
    train_model()
