```python
import re
from datetime import datetime

def transform_logs(logs: str) -> str:
    logs = re.sub(r'\S+@\S+\.\S+', '[HIDDEN]', logs)

    def format_timestamp(match):
        date_time = datetime.strptime(match.group(), "%d/%m/%Y %H:%M")
        return date_time.strftime("%d %B %Y, %I:%M %p").lstrip("0")

    logs = re.sub(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}', format_timestamp, logs)
    logs = logs.replace("ERROR", "🚨 ERROR")
    logs = logs.replace("WARNING", "⚠️ WARNING")
    logs = logs.replace("SUCCESS", "✅ SUCCESS")

    return logs

logs = ""

print("Enter your logs (press Enter on an empty line when finished):")

while True:
    line = input()
    if line == "":
        break
    logs += line + "\n"

print("\nTransformed Logs:")
print(transform_logs(logs))
```
