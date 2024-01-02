import asyncio
import uvicorn
from infra.db.create_db import create_db
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'msg': 'Hello, World'}


from endpoints.products import router as products

app.include_router(products)

if __name__ == '__main__':
    asyncio.run(create_db())
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
