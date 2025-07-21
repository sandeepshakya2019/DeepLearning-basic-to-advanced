# from logger import logging

# def add(a,b): 
#     logging.debug("the additiopn rtaking place")
#     return a+b

# logging.debug("addtion calles")
# add(10,15)

import multiprocessing
import math
import sys
import time

# Extend max digit limit for huge factorials
sys.set_int_max_str_digits(100000)

def fact(n):
    result = math.factorial(n)
    print(f"Factorial of {n} calculated.")
    return result

if __name__ == "__main__":
    numbers = [1000, 200, 3000, 40000]  # Big numbers

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(fact, numbers)  # Distribute tasks

    end_time = time.time()

    print(f"\n⏱ Total Time: {end_time - start_time:.2f} seconds")
    print(f"\n✅ Computed Factorials for: {numbers}")
    # Optional: Print only length to avoid huge output
    for n, r in zip(numbers, results):
        print(f"Length of factorial({n}): {len(str(r))} digits")
