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

def get_docker_stats():
    result = subprocess.run(
        ["docker","stats","--no-stream","--format",
         "{{.Name}}|{{.CPUPerc}}|{{.MemUsage}}|{{.MemPerc}}"],
        capture_output=True, text=True
    )
    stats = {}
    for line in result.stdout.strip().splitlines():
        p=line.split("|")
        if len(p)==4:
            stats[p[0]]={"cpu":p[1],"memory":p[2],"memory_percent":p[3]}
    return stats

print("="*70)
print("MICROSERVICE PERFORMANCE TEST")
print("="*70)

for i, concurrency in enumerate(WORKLOADS, 1):
    start=time.perf_counter()
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        results=list(ex.map(lambda _: send_request(), range(REQUESTS_PER_TEST)))
    total=time.perf_counter()-start
    successful=sum(ok for ok,_ in results)
    failed=REQUESTS_PER_TEST-successful
    times=[t for ok,t in results if ok]
    avg=sum(times)/len(times) if times else 0
    throughput=successful/total
    stats=get_docker_stats()
    print(f"\nWorkload: {concurrency} concurrent requests")
    print(f"Successful Requests : {successful}")
    print(f"Failed Requests     : {failed}")
    print(f"Average Response    : {avg:.4f} seconds")
    print(f"Throughput          : {throughput:.2f} requests/sec")
    for service in ["api-gateway","student-service","course-service"]:
        s=stats.get(service, {"cpu":"N/A","memory":"N/A","memory_percent":"N/A"})
        print(f"{service:18} CPU: {s['cpu']:>7} Memory: {s['memory']:>20} MEM%: {s['memory_percent']}")
print("\nPERFORMANCE TEST COMPLETED")
