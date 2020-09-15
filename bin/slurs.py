from texttable import Texttable
import discord
from discord.ext import commands

from bin.users import Users
from bin.words import Words
from bin.scores import Scores

class SlurCounter(commands.Bot):
    
    def __init__(self, token, logging, usermod, wordmod) -> None:
        super().__init__(command_prefix='!')
        self.logging = logging
        self.usr = usermod
        self.wrd = wordmod
        # logging.info(f'Using token {token}')
        print(f'registering cogs')
        self.add_cog(Scores(self, logging, usermod, wordmod))
        print(f'Using token {token}')
        self.run(token)

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        self.logging.info(f'{self.user.name} has connected to Discord!')

    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.')