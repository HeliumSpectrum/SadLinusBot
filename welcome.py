import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name} Hope you have a good stay in here. Go to #bot-commands and learn how to make use of bots and have fun. Also if youre an anime fan, go to #anime and enjoy. memes is dedicated to dankmemes.'.format(member, guild)
            await guild.system_channel.send(to_send)


client = MyClient()
client.run('token')
