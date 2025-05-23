from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "VELONX11-GODMODE ONLINE"}