#multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def square(i):
    time.sleep(1)
    print(f'square: {i*i}')

numbers=[2,3,4,5,6,7]

with ThreadPoolExecutor(max_workers=10) as executor:
    results=executor.map(square,numbers)

t=time.time()

for result in results:
    print(result)

finished_time=time.time()-t
print(finished_time)