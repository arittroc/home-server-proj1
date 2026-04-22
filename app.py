from flask import Flask
import redis

app = Flask(__name__)
# Connect to the Redis database tier
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        cache.ping()
        db_status = "Connected to Redis! 🟢"
    except redis.exceptions.ConnectionError:
        db_status = "Redis connection failed. 🔴"
        
    return f"<h1>Hello from the Home Server CI/CD Pipeline! 🚀</h1><p>Database Status: {db_status}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
