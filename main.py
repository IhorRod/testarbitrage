import asyncio
import time
from bestchange_api import BestChange
import multiprocessing as mp

from config import quotes

users = ["jfdfs", "fdsfsf", "dfsgsdgds"]


def count(api: BestChange, i: str, user: str):
    for j in quotes:
        cots = api.rates().filter(
            quotes[i][0],
            quotes[j][0]
        )


def counting(api: BestChange):
    pool = mp.Pool(mp.cpu_count())
    for user in users:
        pool.starmap_async(count, [(api, i, user) for i in quotes])
    pool.close()
    pool.join()


def counting1(api: BestChange):
    for i in quotes:
        for j in quotes:
            cots = api.rates().filter(
                quotes[i][0],
                quotes[j][0]
            )


async def main():
    start_time = time.time()
    print("Start connecting")
    api = BestChange()
    print(f"---{time.time() - start_time} sec--- (api connect)")

    print("Start counting")
    start_time = time.time()
    counting(api)
    print(f"---{time.time() - start_time} sec--- (user counting)")


if __name__ == '__main__':
    # print(mp.cpu_count())
    asyncio.run(main())
