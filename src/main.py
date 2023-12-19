from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def router_welcome():
    return {
        'title': 'Welcome API commerce',
        'description': 'This API is open sources',
        'version': ['0.0.1'],
        'teams': ['Carlos', 'Santiago', 'Gerzon', 'Sebastian'],
    }
