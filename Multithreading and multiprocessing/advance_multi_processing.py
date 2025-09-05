##Multiprocessing with processpoolececutor

from concurrent.futures import ProcessPoolExecutor
import time

def square(i):
    time.sleep(1)
    print(f'square: {i*i}')

numbers=[2,3,4,5,6]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square,numbers)

    t=time.time()

    for result in results:
        print(result)

    finished_time=time.time()-t
    print(finished_time)