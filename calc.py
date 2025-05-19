# server.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# دعم CORS للوصول من المتصفح
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calc")
def calculate(text: str):
    try:
        result = eval(text, {"__builtins__": None}, {})
        return PlainTextResponse(str(result))
    except:
        return PlainTextResponse("خطأ في المعادلة", status_code=400)

