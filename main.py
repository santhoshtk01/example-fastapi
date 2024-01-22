from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/login")
async def login(request: Request):
    print(request.client.host)
    return {"Message": "I got your IP :)"}


if __name__ == '__main__':
    uvicorn.run(app)
