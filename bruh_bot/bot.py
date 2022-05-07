import os
import hikari
import lightbulb
import time
import random

bot = lightbulb.BotApp(
    os.environ['TOKEN'], 
    default_enabled_guilds=int(os.environ['GUILD_ID']),
    help_slash_command=True,
    )

phrases = [
    'Kocham Cię najbardziej',
    'Kocham Cię najmocniej',
    'Kocham Cię najbardziej i najmocniej',
    'Je t\'aime',
    'Ich liebe dich',
    'Ik houd van jou',
    'Ti amo amore mio',
    'I love you',
    'Minä rakastan sinua',
    '我爱你 (Wǒ ài nǐ)',
    '사랑해요 (salanghaeyo)',
    'Σε αγαπώ (Se agapó)',
    'Aloha wau iā ʻoe',
    'Te quiero mucho mi amor',
    'Szeretlek szerelmem',
    '愛しているよ、最愛の君 (Ai shite iru yo, saiai no kimi)',
    'Eu amo você meu amor'
]

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

@bot.command()
@lightbulb.command('kocham', 'say kocham several times')
@lightbulb.implements(lightbulb.SlashCommand)
async def love_ya(context): 
    while True:
        number = random.randint(0, len(phrases)-1)
        await context.respond(f'{phrases[number]}')
        time.sleep(15)

def run():
    bot.run()