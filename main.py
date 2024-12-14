import uvicorn
from fastapi import FastAPI

import routers.user, routers.adress

app = FastAPI()

app.include_router(routers.user.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1488)