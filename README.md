# 🔥 TURBOFLAME

**TurboFlame** is a fun and powerful tool for sending automated, randomized in-game messages (flames, dad jokes, compliments) in games like Counter-Strike via configurable hotkeys. It is designed to be fast, customizable, and keyboard-driven — perfect for memes, trolling or just for fun with your team.

## ✨ Features

- 🔥 **Send random flames** to your team or the enemy (separate keys and message sets)
- 👨‍🦳 **Dad jokes** with customizable intro
- 👍 **Nice compliments** to boost morale
- 🌈 **Rainbow-colored terminal output** for style
- 🔁 **Live reload** of text files on every keypress — no need to restart
- 🕒 **Anti-spam**: Messages are rate-limited per type (e.g., 1 every 5 minutes)
- ✏️ Fully **configurable hotkeys, intros, and keys** via `config.cfg`
- 💬 Automatic message splitting if chat messages are too long
- 🆕 **Version output** with custom key

## 🔧 Requirements

- Python 3.7+
- Windows or Linux (Windows CMD fully supported)
- Game must allow global chat key input (Counter-Strike tested)

## 📦 Dependencies
Install via pip:
pip install pynput colorama

📁 File Structure
TurboFlame/
├── flames.txt             # Enemy flames
├── flames_enemy.txt       # Team flames
├── dad.txt                # Dad jokes
├── nice.txt               # Nice messages
├── config.cfg             # Your hotkey and behavior config
└── turbo_flame.py         # Main script

▶️ How to Run
python turbo_flame.py
