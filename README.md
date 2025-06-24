# Cookie-Clicker-Auto-Bot
A Python bot for automating Cookie Clicker using undetected-chromedriver and Selenium. It clicks the cookie rapidly and buys upgrades in order, switching to the next upgrade once the current one becomes more expensive. Designed to simulate human-like progression through the game.
🍪 Cookie Clicker Auto Bot
This project automates the Cookie Clicker game using Python and Selenium with stealth mode (undetected-chromedriver). The bot continuously clicks the big cookie and buys upgrades using a logical progression (Cursor → Grandma → Farm → ...), only switching to the next upgrade once the current one becomes more expensive.

🚀 Features
Automatically opens Cookie Clicker in Chrome
Rapidly clicks the cookie
Buys upgrades in progression order (e.g., Cursor until its price exceeds Grandma)
Bypasses bot detection using undetected-chromedriver
Customizable clicking speed and upgrade strategy

🔧 Requirements
Python 3.7+
Google Chrome (latest version recommended)
Internet connection

📦 Installation
1. Clone this Repository
2. Install Required Python Packages
-pip install undetected-chromedriver selenium
🛠️ How It Works
This bot uses undetected-chromedriver, a wrapper around the regular ChromeDriver that bypasses bot detection. Here's how:
Chrome is launched using stealth options
Cookie Clicker is loaded
English language is selected
The bot clicks the cookie repeatedly
Upgrades are purchased in a specific order:
Cursor is bought until its price exceeds Grandma
Then Grandma is bought until its price exceeds Farm, and so on...

📄 Main Python Script
Your main script is cookie.py. Here’s what it does:
Launches Chrome with undetected-chromedriver
Navigates to Cookie Clicker: https://orteil.dashnet.org/cookieclicker/
Selects English language
Begins auto-clicking and upgrading
▶️ How to Run
Make sure you're in the project directory, then run:
python cookie.py
The Chrome browser will open, and the bot will take over the game automatically.




