import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'msg': 'Hello, World'}


from endpoints.products import router as products

app.include_router(products)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
