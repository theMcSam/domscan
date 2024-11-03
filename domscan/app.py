from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def webroot():
    return {"msg": "Web root"}
