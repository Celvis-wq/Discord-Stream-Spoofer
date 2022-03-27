# Discord Stream Spoofer - By Celvis#1772

# Import Moduals
from flask import Flask
from threading import Thread

# Pull
app = Flask('')

@app.route('/')
# Alert/Credit
def main():
    return "Successfully spoofed stream status!\nHave fun trolling ;)\nMade By: Celvis#1772"

# Run port
def run():
    app.run(host="0.0.0.0", port=8080)

# Keep alive
def keep_alive():
    server = Thread(target=run)
    server.start()