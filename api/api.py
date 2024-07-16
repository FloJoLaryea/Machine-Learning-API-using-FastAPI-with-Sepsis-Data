from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import joblib
from feature_transform import FeatureEngineeringTransformer
import uvicorn




# create an instance of FASTAPI
app = FastAPI(
        title="Sepsis Prediction API",
        description= "Predicts whether a patient at the ICU has the Sepssis disease or not",
        contact={
            "name": "API Support",
            "email": "florencelaryea88@gmail.com"
        }
)


# load model components
def load_ml_components():
    with open("../Model_compartments/sepsis_model_components.joblib","rb") as file:
        model_components = joblib.load(file) 
    return model_components

# call the model components
model_components = load_ml_components()

# get api status
@app.get("/")
def get_status():
    return {"status": "API is running"}


# # Create SeppssisFeatures class from pydantic BaseModel
class SepssisFeatures(BaseModel):
    Plasma_Glucose:int
    Blood_Work_Result_1: int
    Blood_Pressure: int
    Blood_Work_Result_2: int
    Blood_Work_Result_3: int
    Body_Mass_Index: float
    Blood_Work_Result_4: float
    Age: int
    Insurance: int

# # Create Endpoint for the Random Forest Classifier Pipeline
@app.post("/predict_sepsis/random_forest_classifier")
async def predict_sepsis(data:SepssisFeatures):
    try:
        # create dataframe from sepssis data
        df = pd.DataFrame([data.model_dump()])
        # call the random_forest_pipeline and encoder from the ml model
        random_forest_pipeline = model_components["random_forest_classifier"]
        encoder = model_components["encoder"]
        # make prediction
        prediction = random_forest_pipeline.predict(df)
        prediction = int(prediction[0])
        decoded_prediction = encoder.inverse_transform([prediction])[0]
        prediction_proba = random_forest_pipeline.predict_proba(df)[0].tolist()
        response = {"model_used":"Random Forest Classifier",
                    "prediction": decoded_prediction,
                    "prediction_probability":
                    {"Negative":round(prediction_proba[0],2),
                     "Positive":round(prediction_proba[1],2)}
                    }
        
        return response
    except Exception as e:
        return {"error": str(e)}

# # Create Endpoint for the Gradient Boost Model
@app.post("/predict_sepsis/gradient_boost")
async def predict_sepsis(data:SepssisFeatures):
    try:
        # create dataframe from sepssis data
        df = pd.DataFrame([data.model_dump()])
        # call the random_forest_pipeline and encoder from the ml model
        gradient_boost_pipeline = model_components["gradient_boost"]
        encoder = model_components["encoder"]
        # make prediction
        prediction = gradient_boost_pipeline.predict(df)
        prediction = int(prediction[0])
        decoded_prediction = encoder.inverse_transform([prediction])[0]
        prediction_proba = gradient_boost_pipeline.predict_proba(df)[0].tolist()

        response =  {"model_used":"Gradient Boosting Classifier",
                    "prediction": decoded_prediction,
                    "prediction_probability":
                    {"Negative":round(prediction_proba[0],2),
                     "Positive":round(prediction_proba[1],2)}
                    }
        
        return response
    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":
    uvicorn.run("api.py",reload=True)