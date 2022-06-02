
from lib2to3.pgen2 import token
from multiprocessing.connection import Client
from operator import truediv
from pickle import TRUE
import queue
from time import sleep, time
import discord
from discord.ext import tasks
client=discord.Client()
Queue=[]
file1 = open('slurs.txt', 'r')
Lines = file1.readlines()
tokenfile = open('token.txt', 'r')
bottoken = tokenfile.read()
@client.event
async def on_ready():
    print('{0.user}'.format(client))
    delete.start()
@client.event
async def on_message(message):	
    global Queue  
    global Lines
    for slur in Lines:
        
        new_slur=slur[:-2].upper()
        if new_slur in message.content.upper():
            if "fa".upper() in message.content.upper():
                if "fag".upper() in message.content.upper():
                    Queue.append(message)
                    
                else:
                    break
            elif "ni".upper() in message.content.upper():
                if "nig".upper() in message.content.upper():
                    Queue.append(message)
                    
                else:
                    break
            else:
                Queue.append(message)
                
        
@tasks.loop(hours=1)
async def delete():
    global Queue
    global Queue2
    for x in Queue:
        try:
            await x.delete()
        except:
            pass
        Queue.remove(x)
        #probably would be best if we remove regardless of it succeeding or not
client.run(bottoken)
