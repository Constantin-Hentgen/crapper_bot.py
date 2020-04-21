import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = 'crapper ')
status = cycle(['surveiller Groll', 'surveiller Pixart', 'surveiller Thomas', 'surveiller Mateleo', 'surveiller Dkyete'])

@client.event
async def on_ready():
    change_status.start()
    print('Crapper ready')
    
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

def is_it_my_father(ctx):
    return ctx.author.id == myID

@client.command()
@commands.check(is_it_my_father)
async def CRAPPER(ctx):
    await ctx.send(f'A votre service, père, maître et dieu {ctx.author}')

@client.command()
@commands.check(is_it_my_father)
async def vire(ctx, member : discord.Member, * , reason=None): 
    await member.kick(reason=reason)
    
@client.event
async def on_member_join(member):
    await ctx.send(f'Coucou {member}!')

@client.event
async def on_member_remove(member):
    await ctx.send(f'Oh bah non {member}...')

@client.command()
async def crapper(ctx):
    await ctx.send(f'je suis là!')
    
@client.command()
async def nettoye(ctx, amount=10):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=["j'ai dit"])
async def bonjour(ctx):
    await ctx.send('Coucou')

@client.command(aliases=['question'])
async def _8ball(ctx, *, question):
    responses = ['a','b','c']
    await ctx.send(f'Question : {question}\n Réponse : {random.choice(responses)}')

@client.command()
async def calcule(ctx, *, question):
    nombre =  ''
    nombre1 =  ''
    i = 0
    new = 0
    result = 0
    operation = ''
    for lettre in question:
    
        if new == 1  and str.isdigit(lettre) == True:
            nombre1 += lettre
        
        elif str.isdigit(lettre) == True and str.isdigit(question[i]) == True:     
            nombre += lettre      
            i += 1     
        
        elif str.isdigit(lettre) == False:
            new = 1        
            if lettre ==  "*" or lettre == 'x':
                operation = 'mult'
            elif lettre ==  "-":
                operation = 'sub'
            elif lettre ==  "+":
                operation = 'add'
            elif lettre ==  "/":
                operation = 'div'
        
    if operation == 'mult':
        result = int(nombre)*int(nombre1)
    elif operation == 'sub':
        result = int(nombre)-int(nombre1)
    elif operation == 'add':
        result = int(nombre)+int(nombre1)
    elif operation == 'div':
        result = int(nombre)/int(nombre1)    
        
    await ctx.send(f'Euhhhhhh {question} = {result} ?')

client.run('TOKEN')
