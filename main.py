import discord
from discord.ext import commands
import json
import os

setting_file_path = './datas/setting.json'
with open(setting_file_path, 'r', encoding='utf8') as file:
    setting_file_data = json.load(file)

intents = discord.Intents.default()
intents.members = True

Bemo = commands.Bot(command_prefix= '$', intents=intents)

@Bemo.event
async def on_ready():
    print(f'Logged on as {Bemo.user}!')
    game = discord.Game('當個人類感覺真好')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await Bemo.change_presence(status=discord.Status.online, activity=game)


@Bemo.command()
async def 載入(ctx, extension):
    Bemo.load_extension(f'cmds.{extension}')
    await ctx.send(f'已載入 {extension} 模組')

@Bemo.command()
async def 卸載(ctx, extension):
    Bemo.unload_extension(f'cmds.{extension}')
    await ctx.send(f'已卸載 {extension} 模組')

@Bemo.command()
async def 重載(ctx, extension):
    Bemo.reload_extension(f'cmds.{extension}')
    await ctx.send(f'已重載 {extension} 模組')

for file_name in os.listdir('./cmds'):
    if file_name.endswith('.py'):
        Bemo.load_extension(f'cmds.{file_name[:-3]}')

for file_name in os.listdir('./events'):
    if file_name.endswith('.py'):
        Bemo.load_extension(f'events.{file_name[:-3]}')

if __name__ == '__main__':
    Bemo.run(setting_file_data['TOKEN'])