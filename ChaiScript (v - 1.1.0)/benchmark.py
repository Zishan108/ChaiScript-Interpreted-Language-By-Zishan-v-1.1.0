import time
import subprocess
import matplotlib.pyplot as plt

# Function to run command and measure execution time
def run_and_time(command, input_text=None, runs=5):
    times = []
    for _ in range(runs):
        start = time.time()
        process = subprocess.run(command, input=input_text, text=True, shell=True)
        end = time.time()
        times.append(end - start)
    avg_time = sum(times) / runs  # Compute average
    min_time = min(times)  # Min execution time
    max_time = max(times)  # Max execution time
    return avg_time, min_time, max_time

# Running benchmarks
runs = 5  # Number of times each command runs
chai_avg, chai_min, chai_max = run_and_time('python shell.py', 'run("test.chai")\n', runs)
python_avg, python_min, python_max = run_and_time("python test.py", runs=runs)
js_avg, js_min, js_max = run_and_time("node test.js", runs=runs)
java_avg, java_min, java_max = run_and_time("java Test", runs=runs)

# Data for plotting
languages = ["ChaiScript", "Python", "JavaScript", "Java"]
avg_times = [chai_avg, python_avg, js_avg, java_avg]
error_bars = [(avg - min_t, max_t - avg) for avg, min_t, max_t in zip(avg_times, [chai_min, python_min, js_min, java_min], [chai_max, python_max, js_max, java_max])]

# Plot results
plt.figure(figsize=(8, 5))
colors = ["blue", "green", "red", "purple"]
bars = plt.bar(languages, avg_times, color=colors, yerr=list(zip(*error_bars)), capsize=5)

# Add text labels
for bar, time in zip(bars, avg_times):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02, f"{time:.4f} sec", ha="center")

# Graph settings
plt.xlabel("Programming Language")
plt.ylabel("Execution Time (sec)")
plt.title("Benchmark Execution Times (Average of 5 Runs)")
plt.savefig("benchmark_results_avg.png")
plt.show()
