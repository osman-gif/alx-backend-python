#!/usr/bin/env python3
"""From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time."""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int):
    wait_n_exe_time =  wait_n(n, max_delay)
    wait_n_tot_time = 0
    for i in wait_n_exe_time:
        wait_n_tot_time + i
    
    return wait_n_tot_time
    
    