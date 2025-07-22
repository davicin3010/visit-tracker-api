import time
from datetime import datetime

def get_system_stats(start_time: float, visits: int):
    uptime = time.time() - start_time
    return {
        "uptime_seconds": round(uptime, 2),
        "total_visits": visits,
        "current_time": datetime.utcnow().isoformat() + "Z"
    }
