#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve
written and write an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency"""


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    result: list = []
    i: int = 0
    for i in range(n):
        i = await task_wait_random(max_delay)

        result.append(i)
    return sorted(result)
