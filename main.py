from fastapi import FastAPI


import dataset_initialization


app = FastAPI()


@app.get("/vc/")
def recommend_vc(
    user_stage: str, user_market: str
):
    return {"Stage": user_stage, "Market": user_market}
