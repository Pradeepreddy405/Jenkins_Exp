import os

env = os.getenv("APP_ENV", "not-set")

print(f"Running application in {env} environment")
