import multiprocessing
import time

def square():
    for i in range(5):
        square=i*i
        time.sleep(2)
        print(f'Square of {i} is {square}')


def cube():
    for i in range(5):
        cube=i*i*i
        time.sleep(2)
        print(f'Cube of {i} is {cube}')

if __name__== "__main__":
    
    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)
    t=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)