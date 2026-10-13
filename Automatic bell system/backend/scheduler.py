from datetime import datetime
import threading
import time

class BellScheduler:
    def __init__(self, bell_controller, on_ring):
        self.bell = bell_controller
        self.on_ring = on_ring
        self.schedules = []
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            weekday = now.strftime("%a").upper()

            for schedule in self.schedules:
                if (
                    schedule["bell_time"] == current_time
                    and weekday in schedule["days"]
                    and schedule["is_active"]
                ):
                    self.bell.ring_software_bell(schedule["duration_seconds"])
                    self.on_ring(schedule)

            time.sleep(1)
