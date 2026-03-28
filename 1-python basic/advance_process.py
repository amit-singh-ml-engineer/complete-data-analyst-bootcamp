from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"Numbers:{number*number}"
number=[1,2,3,4,5,6,7,8,9,1,2,3]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        result=executor.map(square_numbers,number)
        for results in result:
            print(results)
    