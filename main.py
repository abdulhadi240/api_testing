from fastapi import Fastapi

app : Fastapi = Fastapi()


@app.get('/')
def get_data():
    return 'hello'


