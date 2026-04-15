import datetime
import os

import uvicorn
import jwt
import joblib

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

import pandas as pd

# -----------------------------
# INIT APP
# -----------------------------
app = FastAPI(
    title="FastAPI + JWT + ML (Lazy Loaded Model)",
    description="15-04-2026 - House Price Prediction API with lazy-loaded ML model.",
    version="1.0.0",
)

# -----------------------------
# ENV
# -----------------------------
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
FAKE_USERNAME = os.getenv("FAKE_USERNAME")
FAKE_PASSWORD = os.getenv("FAKE_PASSWORD")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is missing in environment variables")

# -----------------------------
# AUTH
# -----------------------------
bearer = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    try:
        decoded = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return decoded["username"]

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

# -----------------------------
# LAZY LOADED MODEL
# -----------------------------
model = None


def get_model():
    global model
    if model is None:
        model = joblib.load("model.pkl")
    return model


# -----------------------------
# REQUEST MODELS
# -----------------------------
class LoginRequest(BaseModel):
    username: str
    password: str


class PredictionRequest(BaseModel):
    size: float
    rooms: int


# -----------------------------
# ROUTES
# -----------------------------
@app.post("/login")
def login(req: LoginRequest):
    if req.username == FAKE_USERNAME and req.password == FAKE_PASSWORD:
        payload = {
            "username": req.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return {"token": token}

    raise HTTPException(status_code=401, detail="Bad credentials")


@app.get("/")
def root():
    return {"message": "FastAPI + JWT + ML (Lazy Loading) is running"}


@app.post("/predict")
def predict(
    data: PredictionRequest,
    username: str = Depends(verify_token)
):
    model = get_model()
    
    # 14-04-2026 - Updated to use DataFrame input for better compatibility
    # prediction = model.predict([[data.size, data.rooms]])[0]
    df_input = pd.DataFrame([[data.size, data.rooms]], columns=["size", "rooms"])
    prediction = model.predict(df_input)[0]

    return {
        "user": username,
        "input": {
            "size": data.size,
            "rooms": data.rooms
        },
        "predicted_price": round(float(prediction), 2)
    }


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)