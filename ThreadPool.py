''' from concurrent.futures import ThreadPoolExecutor
import time

def Print_numbers(n):
    time.sleep(1)
    return(f"numbers {n}")

lst=[1,2,3,4,5]
with ThreadPoolExecutor (max_workers=3) as executor:
          result=executor.map(Print_numbers,lst)

          for i in result:
                 print(i) '''


from concurrent.futures import ProcessPoolExecutor
import time

def Print_squares(n):
    time.sleep(1)
    return(f"numbers {n*n}")

if __name__=="__main__":
    lst=[1,2,3,4,5]
    with ProcessPoolExecutor (max_workers=3) as executor:
            result=executor.map(Print_squares,lst)
            for i in result:
                    print(i)