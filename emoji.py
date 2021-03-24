import discord
import webhook




@bot.event
async def on_message(message):
   if ":" == message.content[0] and ":" == message.content[-1]:
        emoji_name = message.content[1:-1]

        for emoji in message.guild.emojis:
            if emoji_name == emoji.name:
                pfp = requests.get(message.author.avatar_url_as(format='png', size=256)).content
                hook = await message.channel.create_webhook(name=message.author.display_name, avatar=pfp)
                await hook.send(emoji)
                await message.delete()

    await bot.process_commands(message)
