import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    print(f"worker-{name}")
    # await asyncio.sleep(1)
    url = f"http://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16"
    response = await session.request(method='GET', url=url)
    value = await response.text()
    try:
        value = json.loads(value)
    except json.decoder.JSONDecodeError as e:
        print(f"Problem with {value=}")
        raise e
    if value['success'] != 'true':
        print(f"success: {value['success']}")
    return sum(value['data'])


async def main():

    async with aiohttp.ClientSession() as session:
        # response = await worker('bob', 3, session)
        # print(f"{response=}, {type(response)}")

        sums = await asyncio.gather(*(worker(f"w{i}", n, session) for i, n in enumerate(range(2, 5))))
        print(f"{sums=}, {type(sums)}")

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds.")
