# Discord Bot

This is a simple Discord bot that sends a "Hello!" message to a specific channel when it is run.

## Getting Started

### Prerequisites

To run this bot, you'll need the following:

- Python 3.6 or higher installed
- The `discord.py` library installed. You can install it by running `pip install discord.py` in your terminal or command prompt.

### Creating a Discord Bot

To create a Discord bot and obtain a bot token, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your bot a name.
3. In the left sidebar, click on "Bot" and then click on "Add Bot."
4. Under the "Token" section, click on "Copy" to copy your bot token.

### Configuring the Bot

1. Open the `bot.py` file in a text editor.
2. Replace `'YOUR_TOKEN'` with the bot token you obtained in the previous step.
3. Replace `'YOUR_CHANNEL_ID'` with the ID of the channel where you want the "Hello!" message to be sent.

### Running the Bot

1. Save the `bot.py` file.
2. Open a terminal or command prompt and navigate to the directory where the `bot.py` file is located.
3. Run the bot by executing the command `python bot.py`.
4. The bot will log in to Discord, and once it's ready, it will send the "Hello!" message to the specified channel.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
