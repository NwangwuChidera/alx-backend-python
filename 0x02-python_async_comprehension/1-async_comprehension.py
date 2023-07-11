#!/usr/bin/env python3
"""Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""


import asyncio
import random

# Importing the async_generator coroutine from the previous task
async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

# Define the async_comprehension coroutine
async def async_comprehension():
    random_numbers = [num async for num in async_generator()]
    return random_numbers

# Example usage:
async def main():
    numbers = await async_comprehension()
    print(numbers)

asyncio.run(main())

