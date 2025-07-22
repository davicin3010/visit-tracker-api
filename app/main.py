from fastapi import FastAPI
from app.counter import visit_counter
from app.utils import get_system_stats
import time

app = FastAPI()
start_time = time.time()

@app.post("/visit")
async def visit():
    count = visit_counter.increment()
    return {"visits": count}

@app.get("/stats")
async def stats():
    return get_system_stats(start_time, visit_counter.value())
