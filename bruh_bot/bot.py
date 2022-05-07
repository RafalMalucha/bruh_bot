import os
import hikari
import lightbulb
import dotenv
import datetime

bot = lightbulb.BotApp(
    os.environ['TOKEN'], 
    default_enabled_guilds=int(os.environ['GUILD_ID']),
    help_slash_command=True,
    )

@bot.command()
@lightbulb.command('bruh', 'says brooh')
@lightbulb.implements(lightbulb.SlashCommand)
async def bruh(context):
    await context.respond('brooh')

@bot.command()
@lightbulb.option('text','thing to say')
@lightbulb.command('say', 'make bot say smth')
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(context: lightbulb.SlashCommand):
    await context.respond(context.options.text)



def run():
    bot.run()