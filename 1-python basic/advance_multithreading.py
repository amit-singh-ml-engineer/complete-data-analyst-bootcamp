from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Numbers:{number}"
number=[1,2,3,4,5,6,7,8,9,1,2,3]
with ThreadPoolExecutor(max_workers=3) as executor:
    result=executor.map(print_numbers,number)

for results in result:
    print(results)
    