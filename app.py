import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes.chart import router as chart_router
from routes.prompt import router as prompt_router
from routes.response import router as response_router
from routes.user import router as user_router
from routes.transcribe import router as transcribe_router

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health Check
@app.get("/", tags=["Health Check"])
async def health():
    return {"message": "OK"}


# Routes
app.include_router(user_router)
app.include_router(chart_router)
app.include_router(prompt_router)
app.include_router(response_router)
app.include_router(transcribe_router)


# Run app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
