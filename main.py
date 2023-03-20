import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix=';', case_insensitive=True)

balls = ['mb', 'pb', 'gb', 'ub', 'prb']

@bot.event
async def on_ready():
    print('ready')

@bot.command()
async def p(ctx):
    def user_check(msg):
        embed_content_in_dict = msg.embeds[0].to_dict()
        if msg.author.id==664508672713424926 and ctx.author.name in embed_content_in_dict['description']:
            return True
        return False
    try:
        msg = await bot.wait_for('message', check=user_check,timeout=4)
        def same_user(msg):
            if msg.content.lower() in balls and msg.author.id==ctx.author.id:
                return True
            return False

        msg = await bot.wait_for('message', check=same_user,timeout=8)
        await asyncio.sleep(8)
        await ctx.send(f'{ctx.author.mention} next `;p` command is ready')
    except:
        return


@bot.command()
async def f(ctx):
    def user_check(msg):
        try:
            embed_content_in_dict = msg.embeds[0].to_dict()
            if msg.author.id==664508672713424926 and ctx.author.name in embed_content_in_dict['description']:
                return True
            return False
        except:
            return False
    try:
        msg = await bot.wait_for('message', check=user_check,timeout=4)
        await asyncio.sleep(21)
        await ctx.send(f'{ctx.author.mention} next `;fish` command is ready')
    except:
        return


@bot.command()
async def b(ctx):
    def user_check(msg):
        try:
            embed_content_in_dict = msg.embeds[0].to_dict()
            if msg.author.id==664508672713424926 and ctx.author.name in embed_content_in_dict['description']:
                return True
            return False
        except:
            return False
    try:
        msg = await bot.wait_for('message', check=user_check,timeout=4)
        await asyncio.sleep(60)
        await ctx.send(f'{ctx.author.mention} next `;battle` command is ready')
    except:
        return

@bot.command()
async def sw(ctx):
    def user_check(msg):
        try:
            embed_content_in_dict = msg.embeds[0].to_dict()
            if msg.author.id==664508672713424926 and ctx.author.name in embed_content_in_dict['description']:
                return True
            return False
        except:
            return False
    try:
        msg = await bot.wait_for('message', check=user_check,timeout=4)
        await asyncio.sleep(6)
        await ctx.send(f'{ctx.author.mention} next `;swap` command is ready')
    except:
        return

@bot.command()
async def swap(ctx):
    await sw.invoke(ctx)

@bot.command()
async def pokemon(ctx):
    await p.invoke(ctx)

@bot.command()
async def find(ctx):
    await p.invoke(ctx)

@bot.command()
async def encounter(ctx):
    await p.invoke(ctx)

@bot.command()
async def fish(ctx):
    await f.invoke(ctx)

@bot.command()
async def battle(ctx):
    await b.invoke(ctx)

bot.run('')
