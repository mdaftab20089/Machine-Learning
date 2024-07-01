import logging
## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
            logging.FileHandler("app1.log"),
            logging.StreamHandler()   
              ]
    )

logger=logging.getLogger("ArihtmeticApp")


def add(a,b):
    result=a+b
    logger.debug(f"adding {a}+{b} gives ={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"subtracting {a}-{b} gives ={result}")
    return result


def product(a,b):
    result=a*b
    logger.debug(f"multiplying {a}*{b} gives ={result}")
    return result

def divide(a,b):
    try :
        result=a/b
        logger.debug(f"dividing {a}/{b} gives ={result}")
        return result 
    except ZeroDivisionError:
        print("denominator should not be zero")
        return None

add(15,10)
subtract(15,10)
product(15,10)
divide(15,5)    
        