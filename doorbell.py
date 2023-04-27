import telebot
from gpiozero import Button
import subprocess
import time
import vlc

# Telegram Bot Token and chat ID
bot_token = '6071565366:AAGrMCR5ZzDITok_Kw8b24qrPZ47OxofSEE'
chat_id = '5210179664'

# Initialize the Telegram Bot
bot = telebot.TeleBot(bot_token)

# Initialize the push button
button = Button(17)  # GPIO pin 4

# Define a function to send the image to Telegram
def send_image():
    print("sending picture")
    photo = open('image.jpg', 'rb')
    bot.send_photo(chat_id, photo)
    photo.close()

# Define a function to capture image from webcam
def capture_image():
    print("taking picture")
    subprocess.call(['fswebcam', '-r', '640x480', '--jpeg', '85', '-D', '1', 'image.jpg'])

# Define a function to handle voice message
# Handle the incoming message with audio file
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    # Get the file ID and download the voice message
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Save the voice message as an OGG file
    with open('voice.wav', 'wb') as f:
        f.write(downloaded_file)

    # Play the voice message using vlc
    time.delay(10)
    subprocess.call(['cvlc', '--play-and-exit', 'voice.wav'])

    # Send a reply message to confirm the receipt of the audio file
    bot.reply_to(message, 'Received the audio file!')

# Define a function to handle button press event
def button_pressed():
    capture_image()
    send_image()

# When the button is pressed, capture an image and send it to Telegram
button.when_pressed = button_pressed

# Start the bot
bot.polling()