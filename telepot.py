import logging
from RPi import GPIO
from grove.adc import ADC
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime
import time
import schedule
import threading

# Telegram Bot setup
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
GROUP_CHAT_ID = 'YOUR_GROUP_CHAT_ID'
bot = Bot(token=TOKEN)

# GPIO setup
GPIO.setmode(GPIO.BCM)
relay_pin = 17
GPIO.setup(relay_pin, GPIO.OUT)

# ADC setup for soil moisture sensor
adc = ADC()
soil_sensor_channel = 0
SOIL_MOISTURE_THRESHOLD = 300

# Define file paths
last_watered_file = "last_watered.txt"
log_file = "watering_log.txt"

# Functions
def status(update: Update, context: CallbackContext):
    if update.effective_chat.id != GROUP_CHAT_ID:
        return
    soil_moisture = adc.read(soil_sensor_channel)
    soil_moisture_percentage = (soil_moisture / 950.0) * 100
    update.message.reply_text(f"Soil moisture: {soil_moisture_percentage:.1f}%")

def water(update: Update, context: CallbackContext):
    if update.effective_chat.id != GROUP_CHAT_ID:
        return
    try:
        GPIO.output(relay_pin, GPIO.HIGH)
        update.message.reply_text("Watering the plant...")
        time.sleep(10)
        GPIO.output(relay_pin, GPIO.LOW)
        update.message.reply_text("Watering complete.")
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(last_watered_file, "w") as file:
            file.write(current_time)
        with open(log_file, "a") as log:
            log.write(f"{current_time} - Watered\n")
    except IOError:
        update.message.reply_text("Error occurred during watering.")

def last_watered(update: Update, context: CallbackContext):
    if update.effective_chat.id != GROUP_CHAT_ID:
        return
    try:
        with open(last_watered_file, "r") as file:
            last_watered_time = file.read()
        update.message.reply_text(f"Last watered: {last_watered_time}")
    except FileNotFoundError:
        update.message.reply_text("No watering record found.")

def auto_water_check():
    soil_moisture = adc.read(soil_sensor_channel)
    if soil_moisture < SOIL_MOISTURE_THRESHOLD:
        water(None, None)

def schedule_daily_check():
    schedule.every().day.at("09:00").do(auto_water_check)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Set up Telegram command handlers
updater = Updater(token=TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("status", status))
updater.dispatcher.add_handler(CommandHandler("water", water))
updater.dispatcher.add_handler(CommandHandler("last_watered", last_watered))

# Start daily check in a separate thread
threading.Thread(target=schedule_daily_check).start()

# Start bot
updater.start_polling()
updater.idle()