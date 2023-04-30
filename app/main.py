from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello, World!'}


@app.get('/hello')
def hello():
    return {'message': 'hello this is buchi'}
