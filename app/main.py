import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.spotfy_router import router


app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["Content-Type", "Authorization"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5051, log_level="debug")
