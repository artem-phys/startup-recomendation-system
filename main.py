from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

#services_filename = '/content/drive/MyDrive/Colab Notebooks/Объекты-сервисы и потребности.xlsx'
#services = pd.read_excel(services_filename, sheet_name=None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello world"}


@app.get("/vc/")
def recommend_vc(
    user_stage: str, user_market: str
):
    return {"Stage": user_stage, "Market": user_market}
