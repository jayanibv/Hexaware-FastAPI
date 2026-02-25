import asyncio

async def async_func():
    print("Async function")
    await asyncio.sleep(2) #simulating a time-consuming operation, non blocking sleep
    print("Async function completed")

asyncio.run(async_func())
print("Program completed")
