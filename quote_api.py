import requests, random
FALLBACK = [
    "Small habits make big differences.",
    "Consistency is the key to achievement.",
    "Every day is a chance to be better.",
    "Discipline is freedom.",
    "Show up every day. That's the secret.",
    "You are what you repeatedly do.",
    "Success is the sum of small efforts repeated.",
    "Motivation is what gets you started. Habit keeps you going.",
    "Little by little, a little becomes a lot.",
    "Progress, not perfection.",
    "Don't count the days. Make the days count.",
    "Build the life you want, one habit at a time.",
]
def get_quote():
    try:
        r = requests.get("https://api.quotable.io/random?tags=motivational|success", timeout=3)
        if r.status_code == 200:
            d = r.json()
            return {"content": d["content"], "author": d.get("author","")}
    except Exception:
        pass
    return {"content": random.choice(FALLBACK), "author": "HabitQuest"}
