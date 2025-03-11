from flask import Flask, jsonify
import psutil
import multiprocessing
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/')
def server_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    return jsonify({
        "cpu_percent": cpu_percent,
        "memory": {
            "total": mem.total,
            "used": mem.used,
            "free": mem.free,
            "percent": mem.percent,
        }
    })

def run_flask():
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port, debug=False)

def run_bot():
    subprocess.run([sys.executable, "bot.py"])

if __name__ == '__main__':
    flask_process = multiprocessing.Process(target=run_flask)
    bot_process = multiprocessing.Process(target=run_bot)
    
    flask_process.start()
    bot_process.start()
    
    flask_process.join()
    bot_process.join()
