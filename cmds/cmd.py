import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

boa_file_path = './datas/book_of_answer.json'

with open(boa_file_path, 'r', encoding='utf8') as file:
    boa = json.load(file)


class Cmd(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help='$延遲：查詢機器人與伺服器間的延遲')
    async def 延遲(self, ctx):
        await ctx.send(f'目前延遲為：{round(self.bot.latency * 1000)} 毫秒')

    @commands.command(help='$隨機選擇 (@成員1) ... （@成員n)：隨機選擇一名成員')
    async def 隨機選擇(self, ctx):
        await ctx.send(f'恭喜抽出：{random.choice(ctx.message.mentions).mention}')

    @commands.command(help='$疑問 (你的問題）：翻閱解答之書，給予你答案')
    async def 疑問(self, ctx):
        await ctx.send(random.choice(boa))
    
    @commands.command(help='$移動 (語音頻道名稱) (@成員1) ... （@成員n)：移動指定成員至指定頻道')
    async def 移動(self, ctx, channel: discord.VoiceChannel, *members: discord.Member):
        success_members = ''
        fail_members = ''
        for member in members:
            try:
                await member.move_to(channel)
            except:
                fail_members += member.mention + ' '
            else:
                success_members += member.mention + ' '
        if len(success_members) > 0:
            await ctx.send(f'{success_members} 已成功被 {ctx.author.mention} 移動至 {channel.name}')
        if len(fail_members) > 0:
            await ctx.send(f'{fail_members} 看起來尚未連線至任一頻道')
    
    @commands.command(help='$改名 (@成員) (暱稱)：改變該名成員的伺服器暱稱')
    async def 改名(self, ctx, member: discord.Member, nick_name: str):
        try:
            prev_name = member.display_name
            await member.edit(nick=nick_name)
            await ctx.send(f'{prev_name} 已成功被 {ctx.author.mention} 改名為 {member.mention}')
        except:
            await ctx.send(f'權限不足，無法更改 {member.mention} 的暱稱')

    @commands.command(help='$邀請Bemo (語音頻道名稱)：將Bemo邀請至指定頻道')
    async def 邀請Bemo(self, ctx, channel: discord.VoiceChannel):
        try:
            await channel.connect()
        except commands.BotMissingPermissions as error:
            await ctx.send(f"我沒有加入 {channel.name} ㄉ權限...")
        else:
            await ctx.send(f"偷偷潛入ㄌ{channel}！")

    @commands.command(help='$刪除暱稱 (@成員)：刪除該名成員的伺服器暱稱')
    async def 刪除暱稱(self, ctx, member: discord.Member):
        try:
            await member.edit(nick=None)
            await ctx.send(f'{member.mention} 已成功被 {ctx.author.mention} 刪除暱稱')
        except:
            await ctx.send(f'權限不足，無法刪除 {member.mention} 的暱稱')

def setup(bot):
    bot.add_cog(Cmd(bot))