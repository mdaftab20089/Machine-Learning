import time
import multiprocessing

def square():
    for i in range(6):
        time.sleep(1)
        print(f"sqaure : {i*i} ")

def cube():
    for i in range(6):
        time.sleep(1.5)
        print(f"cube : {i*i*i} ")
    


if __name__ == '__main__':
        p1=multiprocessing.Process(target=square)
        p2=multiprocessing.Process(target=cube)
 
        p1.start()
        p2.start()
## wait for the process to complete
        p1.join()
        p2.join()






