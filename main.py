import uvicorn
from fastapi import FastAPI
from routers.user import user_router
from routers.adress import address_router


app = FastAPI()

app.include_router(address_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1488)