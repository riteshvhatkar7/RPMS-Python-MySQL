from datetime import datetime

class ActivityLogService:

    LOG_FILE = "activity_log.txt"

    def log(self, message: str):
        with open(self.LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} | {message}\n")
