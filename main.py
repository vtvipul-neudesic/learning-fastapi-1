from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message":"Hello world"}

@app.get("/greet/{name}")
def greeting(name:str):
    return {"message":f"Hello {name}"}