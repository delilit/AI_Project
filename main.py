from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

# Load the model
model = joblib.load("model.pkl")

# Genre mapping
genres = {
    1: "Acoustic Folk",
    2: "Alt Music",
    3: "Blues",
    4: "Bollywood Music",
    5: "Country Music",
    6: "HipHop Music",
    7: "Indie Music",
    8: "Instrumental Music",
    9: "Metal Music",
    10: "Pop Music"
}

# Define the FastAPI app
app = FastAPI()

# Define input schema using Pydantic
class SongFeatures(BaseModel):
    Popularity: float
    danceability: float
    energy: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    valence: float
    duration_ms: float

@app.post("/predict")
def predict_genre(features: SongFeatures):
    try:
        input_data = [
            features.Popularity,
            features.danceability,
            features.energy,
            features.speechiness,
            features.acousticness,
            features.instrumentalness,
            features.valence,
            features.duration_ms
        ]

        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)
        predicted_genre = genres.get(prediction[0], "Unknown genre")

        return {"genre": predicted_genre}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
