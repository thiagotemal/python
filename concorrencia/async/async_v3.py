import asyncio

async def dar_OI():
    print("OI")
    await asyncio.sleep(10)
    print("FIm")

async def dar_techaiu():
    print("techau")

async def main ():
  await dar_OI()

if __name__ == "__main__":
  loop = asyncio.get_event_loop()

  tarefa1 = loop.create_task(dar_OI())
  tarefa2 = loop.create_task(dar_techaiu())
  tarefas = asyncio.gather(tarefa1, tarefa2);
  loop.run_until_complete(tarefas)
  loop.close


        