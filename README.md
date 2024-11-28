# Nebula-AI-Image-Telegram-Bot

A Telegram bot that uses Lepton AI to generate AI-powered images based on text prompts. The bot interacts with users, receives prompts, generates images, and stores them in a specified folder, making it easy to organize and retrieve AI-generated visuals.

## Features

- Generate high-quality AI images from text prompts.
- Save generated images to an "Output" folder.
- Simple and easy-to-use interface for Telegram users.
- Fully functional Telegram bot for generating visuals powered by Lepton AI.

## Requirements

Before running the bot, make sure you have the following:

- Python 3.8 or higher.
- Telegram Bot Token (create a bot on Telegram using BotFather).
- Lepton API Token (you can get it by registering on Lepton's platform).
- Required Python libraries: `python-telegram-bot`, `leptonai`, `datetime`.

## Installation

### Clone the repository:

git clone https://github.com/yourusername/Nebula-AI-Image-Telegram-bot.git cd Nebula-AI-Image-Telegram-bot

shell
Copy code

### Install the dependencies:

pip install -r requirements.txt

markdown
Copy code

### Set up your bot and API tokens:

1. Get your **Telegram Bot Token** from [BotFather](https://core.telegram.org/bots#botfather).
2. Get your **Lepton API Token** by signing up on [Lepton's platform](https://lepton.ai).

Update the `BOT_TOKEN` and `LEPTON_API_TOKEN` in the `bot.py` file with your respective tokens.

## Usage

1. Start the bot by running:

python bot.py

markdown
Copy code

2. The bot will start and be available for interactions on Telegram.

### Commands

- `/start` - Start the bot and get a welcome message.
- `/help` - Display the help message with available commands.
- `/generate [prompt]` - Generate an image from your text prompt.
- `/about` - Learn more about the bot.

### Example

To generate an image, use the `/generate` command with a prompt, like so:

/generate A beautiful sunset over the ocean

markdown
Copy code

## Folder Structure

- `bot.py`: The main Python script for the bot.
- `Output/`: Folder where the generated images will be saved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Lepton AI](https://lepton.ai) for providing the AI generation service.
- [Python-Telegram-Bot](https://python-telegram-bot.readthedocs.io/en/stable/) for making it easy to interact with Telegram's Bot API.

## Support

