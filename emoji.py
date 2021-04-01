import discord
import webhook




@bot.event
async def on_message(message):
   if ":" == message.content[0] and ":" == message.content[-1]: #[0]-[-1] are the strings for the message content to detect the nature of the message and work according to it.
        emoji_name = message.content[1:-1] #describing the bot to function the commands for the emoji only / where it can be used for messages also !

        for emoji in message.guild.emojis: # providing limitation to the emoji rendering to the guilds the bot is in.
            if emoji_name == emoji.name:
                pfp = requests.get(message.author.avatar_url_as(format='png', size=256)).content #defining the body of the webhook
                hook = await message.channel.create_webhook(name=message.author.display_name, avatar=pfp)
                await hook.send(emoji)
                await hook.delete()  #this will delete the webhook for integrations as per the discord limit of 10 webhooks per channel
                await message.delete() #this will delete the user message strating with ":" and ending wtih ":", so that the bot get clear commands of what to do !

    await bot.process_commands(message) # letting bot to process other commands too.
