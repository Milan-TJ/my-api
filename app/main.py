from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/add")
def add(a: int, b: int) -> dict:
    return {"result": a + b}

@app.post("/sub")
def sub(a: int, b: int) -> dict:
    return {"result": a - b}