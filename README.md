# Python + FastAPI + JWT Auth + ML

Last updated:

- 14-04-2026

# 🏠 House Price Prediction API (FastAPI + JWT + ML)

A simple machine learning API built with FastAPI that predicts house prices based on house size and number of rooms.  
The API is secured using JWT authentication and serves a trained scikit-learn model.

---

## ✨ Features

- JWT authentication (login + protected routes)
- Machine Learning model (Linear Regression)
- FastAPI REST API
- Training pipeline using CSV dataset
- Model saved with Joblib
- Swagger UI (`/docs`) for testing

---

## 🧰 Tech Stack

- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- PyJWT
- Joblib
- Python-dotenv

---

## 📁 Project Structure

- app.py → FastAPI application (API + JWT + ML)
- train.py → Model training script
- data.csv → Training dataset
- model.pkl → Saved trained model
- requirements.txt → Dependencies
- .env → Environment variables

---

## ⚙️ Installation

### 1. Clone repository
git clone <repo-url>
cd project

---

### 2. Create virtual environment (optional)
python -m venv venv

Activate:
- Windows:
  venv\Scripts\activate

- Mac/Linux:
  source venv/bin/activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Create .env file

SECRET_KEY=your_secret_key
FAKE_USERNAME=admin
FAKE_PASSWORD=1234

---

## 🧠 Train the Model

Run:

python train.py

This will:
- Load data.csv
- Train a Linear Regression model
- Save model as model.pkl

---

## 🚀 Run the API

Start server:

python app.py

Open:

http://localhost:8000
http://localhost:8000/docs

---

## 🔐 Authentication Flow

### Step 1: Login

POST /login

{
  "username": "admin",
  "password": "1234"
}

Response:

{
  "token": "your_jwt_token"
}

---

### Step 2: Authorize in Swagger

Click "Authorize 🔒" and enter:

Bearer <your_token>

---

## 🏠 Prediction Endpoint

POST /predict (protected)

Request:

{
  "size": 90,
  "rooms": 3
}

Response:

{
  "user": "admin",
  "input": {
    "size": 90,
    "rooms": 3
  },
  "predicted_price": 270000
}

---

## 🧠 How it works

- data.csv is used to train the model
- Linear Regression learns relationship between:
  - size
  - rooms
- Model is saved as model.pkl
- FastAPI loads model at startup
- JWT protects prediction endpoint

---

## 📈 Use Cases

- Learn FastAPI + ML integration
- Build secure ML APIs
- Portfolio project
- Base for production ML services

---

## 🚀 Future Improvements

- Use real datasets (Kaggle)
- Add database (PostgreSQL)
- Add user roles
- Dockerize project
- Deploy to cloud

---

## 👨‍💻 Author

Learning project combining:
FastAPI + JWT + Machine Learning

---

## 📜 License

Educational use only


# Deployment to Vercel

- Take a look at the file "vercel.json"

- Create a Project at Vercel from your repository at GitHub with the code of this FastAPI

- Create the envirement variables from .env at Vercel with Groq API Key and the Credentials for Auth

- Make a commit to your GitHub

- Go to Vercel and check that the build and deployment happened and your site is in Production