import asyncio

async def dar_OI():
    print("OI")
    await dar_techaiu()
    print("FIm")

async def dar_techaiu():
    print("techau")

##def main ():
  ##  await dar_OI()

if __name__ == "__main__":
 loop = asyncio.get_event_loop()
 loop.run_until_complete(dar_OI())
 loop.close()

        