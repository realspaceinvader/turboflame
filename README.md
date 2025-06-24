🔥 TurboFlame

TurboFlame is a Python tool that lets you send randomly selected taunts, dad jokes, or nice compliments directly into any game or application chat (like Counter-Strike) using hotkeys.
It’s lightweight, fully configurable, and supports live reloading of text files – no restart needed.
🎯 Features

    🎮 In-Game Ready – Works with games like CS:GO / CS2 via keyboard emulation

    🔥 Team/Enemy Flames – Separate hotkeys for flaming your team or the enemy, with custom intro texts

    😂 Dad Joke Mode – Classic cringe dad jokes with toggleable intro

    💚 Nice Comments – Hotkey for compliments to balance the toxicity

    🧠 Spam Protection – Prevents the same line from repeating within 5 minutes

    💾 Live Reload – Text files auto-reload on each keypress – edit them while the script runs

    ⚙️ Full Config Support – All hotkeys and behavior in config.cfg

    🧱 Split Long Lines – Auto-splits long messages to fit into game chat limits

    🌈 Rainbow Banner – Stylish colored intro when the script starts

    📦 Version Display – Press a hotkey to show your current script version in chat

🛠️ Requirements

    Python 3.7+

    pynput

    colorama

Install dependencies via pip:

pip install pynput colorama

⚙️ Setup

    Clone or download the script.

    Create or edit the config.cfg file with your preferred hotkeys and chat settings.

    Add your lines in:

        flames.txt – General/team flames

        flames_enemy.txt – Enemy-only flames

        dad.txt – Dad jokes

        nice.txt – Compliments

    Run it:

    python turbo_flame.py

    Use the configured hotkeys in-game. The script will simulate keypresses and send the selected lines to chat.

💬 Configuration (config.cfg)

[SETTINGS]
hotkey_flame_team = f8
hotkey_flame_enemy = f9
hotkey_dad = f10
hotkey_nice = f11
hotkey_version = f4
exit_key = f12

chat_key = z
chat_key_nice = u
send_key = enter

dad_intro_enabled = true
flame_intro_team = true
flame_intro_enemy = true

dad_intro_text = Warning! Incoming Dad joke...
flame_intro_team_text = Warning! A Flame for our Team is incoming...
flame_intro_enemy_text = Warning! A Flame for Enemy-Team is incoming...

🧪 Known Limitations

    Game chat input length is capped (~127 chars), but the tool splits long lines smartly

    Works best when game is focused – doesn't hook APIs, only simulates keypresses

🧠 Tips

    Run it in the background during games

    Add meme lines, local insults, or use it as a macro spambot

    Works for other apps too (Discord, Notepad, etc.)

📜 License

MIT – Free to use and modify.
