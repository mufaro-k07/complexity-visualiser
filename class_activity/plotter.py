import time
import io
import base64
import matplotlib.pyplot as plt

def analyze_algorithm(algorithm, n, steps):
    input_sizes = sorted(set(
        max(1, round(i * n / steps))
        for i in range(1, steps + 1)
    ))
    times = []

    start_total = time.time()

    for size in input_sizes:
        start = time.time()
        algorithm(size)
        end = time.time()
        times.append(end - start)

    total_time = time.time() - start_total

    # Plot
    fig, ax = plt.subplots()
    ax.plot(input_sizes, times, marker='o')
    ax.set_xlabel("Input size (n)")
    ax.set_ylabel("Execution time (seconds)")
    ax.set_title("Time Complexity Visualization")

    # Convert plot to base64
    img = io.BytesIO()
    fig.savefig(img, format="png")
    plt.close()
    img.seek(0)

    img_base64 = base64.b64encode(img.read()).decode("utf-8")

    return {
        "input_sizes": input_sizes,
        "times": times,
        "total_time": total_time,
        "image": img_base64
    }
