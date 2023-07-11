#!/usr/bin/env python3
"""Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""

import asyncio
import random

# Importing the async_generator coroutine from the previous task
async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

# Importing the async_comprehension coroutine from the previous task
async def async_comprehension():
    random_numbers = [num async for num in async_generator()]
    return random_numbers

# Define the measure_runtime coroutine
async def measure_runtime():
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time

# Example usage:
async def main():
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime} seconds")

asyncio.run(main())

