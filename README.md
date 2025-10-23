**Project Name** :- AI Healthcare Bot System Using Python

----------------------------------------------------------------
🚀 **Overview**

--------
The AI Healthcare Bot System is an intelligent web-based healthcare assistant developed using Python (Flask) and MySQL.It allows users to interact with a chatbot that provides symptom-based disease predictions, diet and workout recommendations, and precautionary advice.
The system integrates a machine learning model to predict possible diseases based on the user’s symptoms, offering a more personalized and accessible healthcare experience.

-----------------------------
🧠 **Features**

-----------------
✅ **AI Chatbot Interface** – Chat with an intelligent assistant to get instant health guidance.
✅ **Disease Prediction** – Predicts possible illnesses using trained ML models.
✅ **Diet & Workout Plans** – Suggests healthy routines and exercises for recovery.
✅ **Medication Information** – Displays medicines and usage details.
✅ **Precautions & Tips** – Shares do’s and don’ts based on predicted diseases.
✅ **User Authentication** – Login and registration functionality for personalization.
✅ **Admin/Doctor Module** (Optional) – For data management and tracking.

--------------------------

⚙️ **Installation & Setup**
Follow these steps to set up and run the project on your system:

**Step 1: Clone or Download the Project**
git clone https://github.com/yourusername/ai-healthcare-bot-system.git
Or download the ZIP file and extract it.

**Step 2: Navigate to the Project Folder**
cd ai-healthcare-bot-system/chat

**Step 3: Create a Virtual Environment**
python -m venv venv
venv\Scripts\activate       # For Windows
# or
source venv/bin/activate    # For macOS/Linux

**Step 4: Install Dependencies**
pip install flask pandas numpy scikit-learn mysql-connector-python

**Step 5: Setup MySQL Database**
- Open XAMPP Control Panel
- Start Apache and MySQL services.
- Visit phpMyAdmin in your browser:
- http://localhost/phpmyadmin

**Step 6: Retrain the ML Model**
If you wish to retrain or update the model:
python train_model.py

**Step 7: Run the Flask Application**
- python app.py
- You’ll see a message like:
   Running on http://127.0.0.1:5000/
------------------------
📁 **Folder Structure**
chat/
│
├── app.py                     # Main Flask application
├── chatbot.sql                # MySQL database
├── train_model.py             # ML training script
├── predict.py                 # Disease prediction logic
├── data_preprocessing.py      # Data cleaning and encoding
│
├── static/                    # CSS, JS, and images
│   ├── feedback.css
│   ├── style.css
│   ├── script.js
│   ├── voice.js
│   └── images/
│
├── templates/                 # Frontend HTML pages
│   ├── index.html
│   ├── aboutus.html
│   ├── contactus.html
│   ├── feedback.html
│   ├── loginuser.html
│   ├── Lab.html
│   ├── reg.php
│   └── connection.php
│
├── datasets & models:
│   ├── description.csv
│   ├── diets.csv
│   ├── workout_df.csv
│   ├── medications.csv
│   ├── precautions_df.csv
│   ├── Training.csv
│   ├── disease_prediction_model.pkl
│   ├── feature_names.pkl
│   └── label_encoder.pkl
│
└── README.md                  # Documentation file

---------------------------------------------------------

👩‍💻 **Author**
Sakshi BHAGAT
[GitHub Link](https://github.com/sakshi123456sakshi)

