import asyncio
import time

async def async_sleep(t):
    for i in range(10):
        await asyncio.sleep(t)
        print(f"async sleep {t} seconds !")


loop = asyncio.get_event_loop()  
#loop.run_until_complete(main())
asyncio.ensure_future(async_sleep(4))
asyncio.ensure_future(async_sleep(1))
loop.run_forever() 
#loop.close() 