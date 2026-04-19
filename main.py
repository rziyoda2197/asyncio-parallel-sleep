import asyncio

async def sleep_1_second():
    await asyncio.sleep(1)
    print("1 soniya oxirida")

async def sleep_2_seconds():
    await asyncio.sleep(2)
    print("2 soniya oxirida")

async def sleep_3_seconds():
    await asyncio.sleep(3)
    print("3 soniya oxirida")

async def main():
    await asyncio.gather(
        sleep_1_second(),
        sleep_2_seconds(),
        sleep_3_seconds()
    )

asyncio.run(main())
```

Kodni ishga tushirganda, 3 ta funksiya bir vaqtda ishga tushadi va umumiy vaqtni chop etadi.
