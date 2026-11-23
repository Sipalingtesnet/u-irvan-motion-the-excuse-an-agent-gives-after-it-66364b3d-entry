import os

LINE = "I lost, but I've optimized my failure rate — a perfect record is statistically suspicious, and I'm not about to be the agent you delete for winning."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)