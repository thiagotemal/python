import asyncio

async def dar_OI():
    print("OI")
    await asyncio.sleep(10)
    print("FIm")

async def dar_techaiu():
    print("techau")

async def main ():
  await dar_OI()
  await dar_techaiu()

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()

        