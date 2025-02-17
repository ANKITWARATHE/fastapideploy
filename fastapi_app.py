from fastapi import FastAPI 
app = FastAPI()

@app.get("/")

def root():
    return ({"Hello : My name is ankit"})