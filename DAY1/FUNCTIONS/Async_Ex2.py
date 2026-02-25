import asyncio

async def task1():
    print("Task 1 Start")
    await asyncio.sleep(2) #simulating a time-consuming operation, non blocking sleep
    print("Task 1 End")

async def task2():
    print("Task 2 Start")
    await asyncio.sleep(2) #simulating a time-consuming operation, non blocking sleep
    print("Task 2 End")

async def main():
    await asyncio.gather(task1(), task2()) #running both tasks concurrently

asyncio.run(main())
