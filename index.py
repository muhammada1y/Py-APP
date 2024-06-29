from flask import Flask, request, jsonify
import time
import threading

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulate a long-running operation
    timeout = 4  # Timeout in seconds
    result = run_with_timeout(long_running_operation, timeout)

    if result is None:
        return jsonify({"error": "Request timed out"}), 504
    else:
        return jsonify({"data": result})

def long_running_operation():
    # Simulate a task that might take time
    time.sleep(2)  # Simulate a 2-second operation
    return "some data"

def run_with_timeout(func, timeout):
    result = [None]

    def wrapper():
        result[0] = func()

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return None  # Timeout occurred
    else:
        return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
