import asyncio
import requests
import uuid
from time import sleep

sleep_time = 0.1
req_num = 30

def post_it():
    request_id = str(uuid.uuid4())
    url = "https://example.com"
    data = "foo=bar&foobar=foobar"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-RequestID": request_id,
        "Cache-Control": "no-cache",
        "User-Agent" : "vince-async-post"
    }
    print(f"Started request {request_id}")
    resp = requests.post(url, data=data, headers=headers)
    #print(resp.headers)
    #print(resp.text)
    return resp

async def async_post():
    loop = asyncio.get_event_loop()
    for i in range(req_num):
        sleep(sleep_time)
        fut = loop.run_in_executor(None, post_it)


import argparse
parser = argparse.ArgumentParser(description='Requests to POST.')
parser.add_argument('-n', '--num', type=int, default=req_num, help="Number of requests to send (default 30).")
parser.add_argument('-t', '--tms', type=float, default=sleep_time, help="Sleep time between requests in ms (default 0.1 ms).")
args = parser.parse_args()
sleep_time = args.tms
req_num = args.num


loop = asyncio.get_event_loop()  
loop.run_until_complete(async_post())
#loop.run_forever() 
#loop.close() 