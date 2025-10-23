**Project Name** :- AI Healthcare Bot System Using Python

----------------------------------------------------------------
🚀 **Overview**

--------
The AI Healthcare Bot System is an intelligent web-based healthcare assistant developed using Python (Flask) and MySQL.It allows users to interact with a chatbot that provides symptom-based disease predictions, diet and workout recommendations, and precautionary advice.
The system integrates a machine learning model to predict possible diseases based on the user’s symptoms, offering a more personalized and accessible healthcare experience.

-----------------------------
🧠 **Features**


✅ **AI Chatbot Interface** – Chat with an intelligent assistant to get instant health guidance.<br>
✅ **Disease Prediction** – Predicts possible illnesses using trained ML models.<br>
✅ **Diet & Workout Plans** – Suggests healthy routines and exercises for recovery.<br>
✅ **Medication Information** – Displays medicines and usage details.<br>
✅ **Precautions & Tips** – Shares do’s and don’ts based on predicted diseases.<br>
✅ **User Authentication** – Login and registration functionality for personalization.<br>
✅ **Admin/Doctor Module** (Optional) – For data management and tracking.<br>

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
or
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
📁 **Folder Structure** <br>
chat/
│
├── app.py                     # Main Flask application <br>
├── chatbot.sql                # MySQL database<br>
├── train_model.py             # ML training script<br>
├── predict.py                 # Disease prediction logic<br>
├── data_preprocessing.py      # Data cleaning and encoding<br>
│
├── static/                    # CSS, JS, and images<br>
│   ├── feedback.css<br>
│   ├── style.css<br>
│   ├── script.js<br>
│   ├── voice.js<br>
│   └── images/<br>
│
├── templates/                 # Frontend HTML pages<br>
│   ├── index.html<br>
│   ├── aboutus.html<br>
│   ├── contactus.html<br>
│   ├── feedback.html<br>
│   ├── loginuser.html<br>
│   ├── Lab.html<br>
│   ├── reg.php<br>
│   └── connection.php<br>
│
├── datasets & models:<br>
│   ├── description.csv<br>
│   ├── diets.csv<br>
│   ├── workout_df.csv<br>
│   ├── medications.csv<br>
│   ├── precautions_df.csv<br>
│   ├── Training.csv<br>
│   ├── disease_prediction_model.pkl<br>
│   ├── feature_names.pkl<br>
│   └── label_encoder.pkl<br>
│
└── README.md                  # Documentation file<br>

---------------------------------------------------------

👩‍💻 **Author**
Sakshi Bhagat<br>
[GitHub Link](https://github.com/sakshi123456sakshi)

