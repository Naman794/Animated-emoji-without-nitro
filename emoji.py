import discord
import requests

class EmojiBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        # Check if the message content starts and ends with a colon
        if message.content.startswith(":") and message.content.endswith(":"):
            # Extract the emoji name from the message content
            emoji_name = message.content[1:-1]

            # Search for the emoji in the guild's collection
            for emoji in message.guild.emojis:
                if emoji_name == emoji.name:
                    # Get the user's profile picture
                    pfp = requests.get(message.author.avatar_url_as(format='png', size=256)).content

                    # Create a webhook with the user's display name and profile picture
                    hook = await message.channel.create_webhook(name=message.author.display_name, avatar=pfp)

                    # Send the emoji through the webhook
                    await hook.send(emoji)

                    # Delete the webhook to avoid exceeding Discord's limit
                    await hook.delete()

                    # Delete the user's message
                    await message.delete()

                    # Exit the loop once the emoji is found and sent
                    break

        # Process other commands
        await self.process_commands(message)

# Run the bot with your token
bot = EmojiBot()
bot.run('YOUR_DISCORD_BOT_TOKEN')
