'''import time
def print_numbers():
    for i in range(5):
        print(i)


def print_letters():
    for i in ("ABCDE"):
        print(i)


t=time.time()
print(t)
time.sleep(2)
print_numbers()
time.sleep(2)
print_letters()
time.sleep(1)
finishedtime=time.time()-t
print(finishedtime)
'''

## what we do when first function is sleeping we call the second function
import threading
import time
def print_numbers():
    for i in range(5):
        print("Number",i)
        time.sleep(2)


def print_letters():
    for i in ("ABCDE"):
        print("Letters",i)
        time.sleep(2)


t=time.time()
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t1.start()
t2.start()

t1.join()
t2.join()

finishedtime=time.time()-t
print(finishedtime)