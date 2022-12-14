# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:55:33 2022

@author: somaa
"""

import asyncio
from time import sleep
import websockets
from time import sleep 
async def hello():
    async with websockets.connect("ws://localhost:8080") as websocket:
        m=await websocket.recv()
        print(m)
        #s=input()
        #await websocket.send(s)
        
        
            
while(True):
    asyncio.run(hello())