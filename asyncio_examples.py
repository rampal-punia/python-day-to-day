import asyncio
import aiohttp

# Example: 1
# use async keyword in front of a function definition


async def async_func():
    print("My async function")

# async function with wait keyword


async def main():
    await async_func()

# calling main function with asyncio.run
# This function runs the passed coroutine, taking care of
# managing the asyncio event loop and finalizing asynchronous
# generators.
asyncio.run(main())

# Example: 2


async def func_1():
    await asyncio.sleep(1)
    print("func 1")


async def func_2():
    await asyncio.sleep(2)
    print("func 2")


async def main():
    await asyncio.gather(func_1(), func_2())

asyncio.run(main())


# Example: 3
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

asyncio.run(main())
