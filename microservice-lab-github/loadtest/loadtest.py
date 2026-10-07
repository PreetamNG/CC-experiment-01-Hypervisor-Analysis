"""Workload test for the Student/Course API Gateway.

Runs 20 requests at each concurrency level (1, 2, 4, 8, 16) against
GET /dashboard and captures response time, throughput, failures, and
Docker CPU/memory snapshots.
"""
import requests
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor

URL = "http://localhost:5000/dashboard"
WORKLOADS = [1, 2, 4, 8, 16]
REQUESTS_PER_TEST = 20

def send_request():
    start = time.perf_counter()
    try:
        response = requests.get(URL, timeout=10)
        elapsed = time.perf_counter() - start
        return response.status_code == 200, elapsed
    except Exception:
        return False, time.perf_counter() - start

def docker_stats():
    cmd = ["docker", "stats", "--no-stream", "--format",
           "{{.Name}}|{{.CPUPerc}}|{{.MemUsage}}|{{.MemPerc}}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = {}
    for line in result.stdout.strip().splitlines():
        parts = line.split("|")
        if len(parts) == 4:
            data[parts[0]] = parts[1:]
    return data

rows = []
for concurrency in WORKLOADS:
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        results = list(executor.map(lambda _: send_request(), range(REQUESTS_PER_TEST)))
    total_time = time.perf_counter() - started
    successful = sum(ok for ok, _ in results)
    failed = REQUESTS_PER_TEST - successful
    times = [t for ok, t in results if ok]
    stats = docker_stats()
    row = {
        "workload": f"W{WORKLOADS.index(concurrency)+1}",
        "concurrency": concurrency,
        "successful": successful,
        "failed": failed,
        "avg_response_ms": round(sum(times)/len(times)*1000, 4) if times else 0,
        "throughput_rps": round(successful/total_time, 2),
    }
    for service in ["api-gateway", "student-service", "course-service"]:
        cpu, mem, mem_pct = stats.get(service, ["0%", "0MiB / 0GiB", "0%"])
        row[f"{service}_cpu_pct"] = float(cpu.strip("%"))
        row[f"{service}_memory"] = mem
        row[f"{service}_mem_pct"] = float(mem_pct.strip("%"))
    rows.append(row)
    print(row)

import csv, os
os.makedirs("results", exist_ok=True)
with open("results/results.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)
print("Saved results/results.csv")
