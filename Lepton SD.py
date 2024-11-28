import os
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from leptonai.client import Client
from datetime import datetime

# Set your bot token and Lepton API token
BOT_TOKEN = "7778811622:AAHhqikV-V682t2gGeDVH0Cu919IH_HVgRg"
LEPTON_API_TOKEN = "9IYGCgqm4RbPMQonvIXOlvjyHkOVKfWZ"

# Initialize Lepton client
lepton_client = Client("https://sdxl.lepton.run", token=LEPTON_API_TOKEN)

# Folder where images will be saved
OUTPUT_FOLDER = "Output"

# Create the Output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def generate_image(prompt: str):
    """
    Generate an image using Lepton API and return the file path.
    The generated image will be saved in the Output folder with a timestamp in the filename.
    """
    try:
        image = lepton_client.run(
            prompt=prompt,
            height=1024,
            width=1024,
            guidance_scale=4,
            high_noise_frac=0.75,
            seed=1809774958,
            steps=30,
            use_refiner=True
        )

        # Get the current time and format it as a string
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        # Create a filename with the timestamp inside the Output folder
        output_path = os.path.join(OUTPUT_FOLDER, f"generated_image_{current_time}.png")

        with open(output_path, "wb") as f:
            f.write(image)

        return output_path
    except Exception as e:
        print(f"Error generating image: {e}")
        return None


# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 Welcome to Nebula Image Bot! Send a text prompt using /generate [your prompt] to create stunning AI images."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Nebula Image Bot Commands:*\n\n"
        "/start - Start the bot and get a welcome message\n"
        "/help - Show this help message\n"
        "/generate [prompt] - Generate an image from your text prompt\n"
        "/about - Learn more about the bot"
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Nebula Image Bot transforms your ideas into AI-generated visuals. Powered by Nebula AI's advanced technology."
    )


async def generate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text(
            "⚠️ Please provide a prompt after the command! Example: /generate Astronaut on Mars during sunset."
        )
        return

    prompt = ' '.join(context.args)

    # Notify the user that the generation has started
    loading_message = await update.message.reply_text("✨ Generating your image, please wait...")

    # Generate the image
    image_path = generate_image(prompt)

    if image_path:
        # Delete the loading message
        await loading_message.delete()

        # Send the generated image
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image_path, "rb"))
    else:
        # Notify the user about the error
        await loading_message.delete()
        await update.message.reply_text("❌ Sorry, there was an error generating your image. Please try again.")


# Main function
if __name__ == "__main__":
    print("Starting Nebula Image Bot...")
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("generate", generate_command))

    # Run the bot
    app.run_polling(poll_interval=3)
