from fastapi import FastAPI
import uvicorn

# 1. FastAPI ka instance (app) banayein. Yeh aapka main server web application hai.
app = FastAPI(title="Mera Pehla AI Deployment Server")

# 2. Aik dummy Machine Learning Model Function (Kyunke actual model bhi sirf math calculation karta hai)
def fake_ml_predict(input_text: str):
    # Sochein yeh aapka model hai jo sentiment analysis kar raha hai
    if "good" in input_text.lower() or "amazing" in input_text.lower():
        return {"sentiment": "Positive", "confidence": 0.94}
    else:
        return {"sentiment": "Negative", "confidence": 0.81}

# 3. Ek 'Endpoint' ya Raasta banayein jahan internet se log data bhejenge
@app.post("/predict")
def predict_sentiment(text_input: str):
    """
    Yeh function tab chalega jab koi is link par POST request bhejega.
    """
    # Aapka server incoming data ko model function mein bhejega
    prediction = fake_ml_predict(text_input)
    
    # Aur result JSON format mein wapas bhej dega
    return {"status": "success", "data": prediction}

# 4. Server ko run karne ka tareeqa
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)