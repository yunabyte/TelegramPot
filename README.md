<br> 

# 🌱 TelegramPot: Smart Plant Watering System
A smart plant care solution that combines Telegram API and Raspberry Pi 🌿  

<sub>If you'd like a detailed explanation in Korean, check out my blog! 🇰🇷</sub>  
<sub>[01: Overview and Setup](https://icecreamzoa.com/2024/47/)</sub>  
<sub>[02: Hardware and Software Details](https://icecreamzoa.com/2024/65/)</sub>  
<sub>[03: Project Implementation and Code](https://icecreamzoa.com/2024/82/)</sub>  

  <br><br>
## 🌟 Project Overview
In today’s busy lifestyle, plant care can be challenging.  
To make this easier, TelegramPot lets you:  
  
💬  Check your plant’s moisture level remotely  
🌊  Water your plant on demand or automatically  
📅  Track the last watering time for consistency  

This project uses **IoT technology** to integrate a soil moisture sensor, water pump, and relay module with a Raspberry Pi and a Telegram bot.

  <br><br>
## 💡 Features
🧑‍💻 **Real-time Plant Monitoring**: Get live updates on your plant's soil moisture level with the `/status` command.  
🌧️ **Remote Watering**: Use the `/water` command to water your plant from anywhere.  
🗂️ **Watering History**: Check the last time your plant was watered using the `/last_watered` command.  
🤖 **Daily Automatic Watering**: Every morning at 9 AM, TelegramPot checks the moisture level and waters the plant if needed.  

  <br><br>
## 📸 Circuit Diagram
![Circuit Diagram](https://icecreamzoa.com/wp-content/uploads/2024/07/image.png)  
<h3>Hardware</h3>

- **Raspberry Pi** with Grove Hat  
- **Soil Moisture Sensor** from Grove  
- **Relay Module** Controls the water pump with GPIO pins  
- **Water Pump** Delivers water to the plant when activated  
- **9V Battery** Powers the relay module and pump  

  <br><br>
## 🎥 Demo Video
[![Watch the Demo Video](https://img.youtube.com/vi/aDYlXivdQ04/0.jpg)](https://youtu.be/aDYlXivdQ04)  
<br><br>
<sub><i>This README was generated with assistance from ChatGPT</i></sub>  
<sub>© 2024 Yuna. All rights reserved.</sub>
<br><br>
