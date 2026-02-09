import os
from flask import Flask, request, jsonify
from factorial import bubble_sort, linear_search, binary_search, nested_loops
from plotter import analyze_algorithm
import time

ALGORITHMS = {
    "bubble": bubble_sort,
    "linear": linear_search,
    "binary": binary_search,
    "nested": nested_loops
}

TIME_COMPLEXITY = {
    "bubble": "O(n^2)",
    "linear": "O(n)",
    "binary": "O(log n)",
    "nested": "O(n^2)"
}
app = Flask(__name__)

@app.route("/")
def home():
    return "Analyser Running"

@app.route("/analyze", methods=["GET"])
def analyze():
    algo_name = request.args.get("algo", "").strip().lower()
    try:
        n = int(request.args.get("n", 1000))
        steps = int(request.args.get("steps", 10))

        if n <= 0 or steps <= 0:
            return {"error": "n and steps must be greater than 0"}, 400

    except ValueError:
        return {"error" : "n and steps must be a valid integer"}, 400

    if algo_name not in ALGORITHMS:
        return jsonify({
            "error": "Invalid algorithm",
            "supported_algos": ["bubble", "linear", "binary", "nested"]
        }), 400

    start_time = time.time()
    result = analyze_algorithm(ALGORITHMS[algo_name], n, steps)
    end_time = time.time()
    total_time = end_time - start_time

    return jsonify({
        "algorithm": algo_name,
        "n": n,
        "steps": steps,
        "start_time": start_time,
        "end_time": end_time,
        "total_time_ms": total_time,
        "time_complexity": TIME_COMPLEXITY[algo_name],
        "graph_base64": result["image"],
        "input_sizes": result["input_sizes"],
        "times": result["times"]
    })

if __name__ == "__main__":
    app.run(port=3000, debug=True)
