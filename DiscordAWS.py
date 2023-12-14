
'''Importing Libraries'''

import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv


#initalizing variables

load_dotenv()
client = discord.Bot()
token = str(os.getenv('TOKEN'))

#Initializes the discord API
@client.event
async def on_ready(): #Triggers the following operation
    print("Logged in as a bot{0.user}".format(client))
    

    #Prints EC2 Data
    print(ec2_metadata.region)
    print(ec2_metadata.instance_id)
    print({ec2_metadata.public_ipv4})

#Extracting information about the discord's username, channel name, and what the usser types
@client.event
async def on_message(message):
    #Convert to string
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')
    #Setting up bot responses
    if message.author == client.user:
        return
    
    #If else statement
    #Outputs a message depending on the users input
    if channel == "bot":
        if user_message.lower() == "hello" or user_message.lower() == "sup":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye Bye {username}!')

        elif user_message.lower() == "ec2 data":
            await message.channel.send(f'Your Region: {ec2_metadata.region}\nEC2 Instance ID: {ec2_metadata.instance_id}\nIP Address: {ec2_metadata.public_ipv4}')

        else:
            await message.channel.send(f"Error, try again")

#Runs the code with the token key through AWS instance            
client.run(token)