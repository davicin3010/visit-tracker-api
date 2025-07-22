import threading

class VisitCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self._count += 1
            return self._count

    def value(self):
        with self._lock:
            return self._count

visit_counter = VisitCounter()
