from discord.ext import commands
from core.classes import Cog_Extension
import json

text_channel_file_path = './datas/text_channel_id.json'

with open(text_channel_file_path, 'r', encoding='utf8') as file:
    text_channel_id_list = json.load(file)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(text_channel_id_list['一般']))
        await channel.send('{member} 加入ㄌ!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(text_channel_id_list['一般']))
        await channel.send('{member} 滾ㄌ!')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.bot.user:
            return
        
        if ('有夠爛' in message.content) or ('機器人' in message.content):
            await message.delete()
            await message.channel.send(f'{message.author.display_name} 已被管理員史丹利(relaxing234)永久禁言！')
        elif message.content == '嗨':
            await message.channel.send(f'嗨 {message.author.display_name}！')


def setup(bot):
    bot.add_cog(Event(bot))