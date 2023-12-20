# File principle

from fastapi import FastAPI

app = FastAPI()


# Decorador

@app.get('/')
async def server():
    return "Hola"

@app.get('/carlos')
async def carlos_get():
    return "Hola soy carlos y estoy con sebastian"
