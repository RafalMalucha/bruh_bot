import os
import hikari
import lightbulb
import time
import random
import string

bot = lightbulb.BotApp(
    os.environ['TOKEN'], 
    default_enabled_guilds=int(os.environ['GUILD_ID']),
    help_slash_command=True,
    )

phrases = [
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

bad_words = ['chuj', 'dupa', 'kurwa', 'cipa']

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
    number = random.randint(0, len(phrases)-1)
    await context.respond(f'{phrases[number]}', os.environ['USER_ID'])

@bot.listen()
async def jajco(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    words = event.content.split()
    for word in words:
        if word.lower().translate(str.maketrans('', '', string.punctuation)) == 'co':
            await bot.rest.create_message(int(os.environ['CHANNEL_ID']), 'jajco')
            break

@bot.listen()
async def bruh(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    words = event.content.split()
    for word in words:
        if word.lower() == 'bruh':
            await bot.rest.create_message(int(os.environ['CHANNEL_ID']), 'bruh')
            break

@bot.listen()
async def chuj(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    words = event.content.split()
    for word in words:
        if word in bad_words:
            await bot.rest.create_message(int(os.environ['CHANNEL_ID']), 'you\'ve been banned from mickey mouse club for inappropriate behavior')
            break

def run():
    bot.run()
