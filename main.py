from fastapi import FastAPI

app:FastAPI = FastAPI()


@app.get('/')
def get_data():
        return 'hello'


