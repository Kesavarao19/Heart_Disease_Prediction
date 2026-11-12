import pandas as pd 
import  numpy  as np 
from fastapi  import FastAPI
from pydantic import BaseModel
import joblib


model=joblib.load("heart_disease.pkl")


app=FastAPI()


class Person(BaseModel):
    Age:int
    Sex:str
    ChestPainType:str
    RestingBP:int
    Cholesterol:int
    FastingBS:int
    RestingECG:str
    MaxHR:int
    ExerciseAngina:str
    Oldpeak:int
    ST_Slope:str

@app.post("/predict")
def predict(data:Person):
    df=pd.DataFrame([data.dict()])

    prediction =model.predict(df)[0]

    result="Heart Disease" if prediction==1 else "Not Heart Disease"

    return {
        "prediction":int(prediction),
        "result": result
    }

