# Discord Emoji Bot

This Discord bot allows users to easily use custom emojis by typing emoji names enclosed within colons (`:`) in their messages. When a message starts and ends with a colon and contains a valid emoji name, the bot replaces it with the corresponding emoji from the server's collection.

## Features

- Automatically detects emoji names enclosed within colons (`:`) in messages.
- Utilizes Discord webhooks for seamless emoji integration.
- Deletes the original user message to maintain a clean chat environment.
- Works within the limitations of Discord's webhook system (10 webhooks per channel).

## Requirements

- Python 3.x
- `discord.py` library (can be installed via pip)
- Discord Bot Token (to run the bot on Discord servers)

## Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your_username/discord-emoji-bot.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up a Discord Bot account and obtain the token.
   
4. Replace `YOUR_TOKEN_HERE` in `config.py` with your Discord Bot Token.

5. Run the bot:

    ```
    python bot.py
    ```

## Usage

Once the bot is running and added to a Discord server, users can use custom emojis by typing the emoji name enclosed within colons (`:`) in their messages. For example, `:smile:` will be replaced with the `:smile:` emoji if it exists on the server.

## Note

- The bot utilizes Discord webhooks for seamless emoji integration. Ensure that the bot has the necessary permissions to create and delete webhooks in the channels where it operates.
- This bot deletes the original user message to maintain a clean chat environment. Ensure that the bot has the necessary permissions to delete messages in the channels where it operates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of `discord.py` for providing a powerful library for building Discord bots.
- Inspired by the need for a simple solution to use custom emojis in Discord messages.
  
Feel free to customize and extend the bot according to your needs!
