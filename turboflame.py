import os
import sys
import time
import random
import configparser
from datetime import datetime, timedelta
from pynput import keyboard
from pynput.keyboard import Key, Controller
import colorama

colorama.init()

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
RAINBOW = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]

def rainbow(text):
    return ''.join(RAINBOW[i % len(RAINBOW)] + c for i, c in enumerate(text)) + RESET

for line in [
    "╔══════════════════════════════════════╗",
    "║            TURBOFLAME V0.9           ║",
    "║         © by spaceinvader.at         ║",
    "╚══════════════════════════════════════╝"
]:
    print(rainbow(line))

controller = Controller()
config = {}
texte = {}
SPERRZEIT = timedelta(minutes=5)
text_cache = {
    "flames": {},
    "flames_enemy": {},
    "dad": {},
    "nice": {}
}

def taste_von_text(taste):
    mapping = {
        'enter': Key.enter, 'space': Key.space, 'tab': Key.tab,
        'shift': Key.shift, 'ctrl': Key.ctrl, 'alt': Key.alt,
        'esc': Key.esc, 'delete': Key.delete, 'backspace': Key.backspace,
        'f1': Key.f1, 'f2': Key.f2, 'f3': Key.f3, 'f4': Key.f4,
        'f5': Key.f5, 'f6': Key.f6, 'f7': Key.f7, 'f8': Key.f8,
        'f9': Key.f9, 'f10': Key.f10, 'f11': Key.f11, 'f12': Key.f12
    }
    return mapping.get(taste.lower(), taste.lower())

def lade_config():
    global config
    pfad = os.path.join(os.path.dirname(__file__), "config.cfg")
    cfg = configparser.ConfigParser()
    cfg.read(pfad)
    s = cfg["SETTINGS"]
    config = {
        'hotkey_flame_team': s.get("hotkey_flame_team", "f8"),
        'hotkey_flame_enemy': s.get("hotkey_flame_enemy", "f9"),
        'hotkey_dad': s.get("hotkey_dad", "f10"),
        'hotkey_nice': s.get("hotkey_nice", "f11"),
        'hotkey_version': s.get("hotkey_version", "f4"),
        'exit_key': s.get("exit_key", "f12"),
        'chat_key': taste_von_text(s.get("chat_key", "z")),
        'chat_key_nice': taste_von_text(s.get("chat_key_nice", "u")),
        'send_key': taste_von_text(s.get("send_key", "enter")),
        'dad_intro_enabled': s.getboolean("dad_intro_enabled", True),
        'flame_intro_team': s.getboolean("flame_intro_team", True),
        'flame_intro_enemy': s.getboolean("flame_intro_enemy", True),
        'dad_intro_text': s.get("dad_intro_text", "Warning! Incoming Dad joke......"),
        'flame_intro_team_text': s.get("flame_intro_team_text", "Warning! A Flame for our Team is incoming..."),
        'flame_intro_enemy_text': s.get("flame_intro_enemy_text", "Warning! A Flame for Enemy-Team is incoming...")
    }

    print(f"{CYAN}[INFO] Hotkeys: Team-Flame={config['hotkey_flame_team']}, Enemy-Flame={config['hotkey_flame_enemy']}, Dad={config['hotkey_dad']}, Nice={config['hotkey_nice']}, Version={config['hotkey_version']}, Exit={config['exit_key']}{RESET}")
    print(f"{CYAN}[INFO] Chat-Key Normal={config['chat_key']}, Chat-Key Nice={config['chat_key_nice']}, Send-Key={config['send_key']}{RESET}")

def lade_txt_datei(dateiname):
    try:
        with open(os.path.join(os.path.dirname(__file__), dateiname), "r", encoding="utf-8", errors="ignore") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{RED}[FEHLER] Datei {dateiname} konnte nicht geladen werden: {e}{RESET}")
        return []

def tippe(text, chatkey, maxlen=127):
    teile = []
    while len(text) > maxlen:
        split_at = text.rfind(" ", 0, maxlen)
        if split_at == -1:
            split_at = maxlen
        teile.append(text[:split_at])
        text = text[split_at:].lstrip()
    teile.append(text)

    for teil in teile:
        controller.press(chatkey)
        controller.release(chatkey)
        time.sleep(0.1)
        for char in teil:
            controller.press(char)
            controller.release(char)
            time.sleep(0.015)
        controller.press(config['send_key'])
        controller.release(config['send_key'])
        time.sleep(0.35)

def sende_text(_, typ):
    texte[typ] = lade_txt_datei(f"{typ}.txt")
    now = datetime.now()
    gültig = [t for t in texte[typ] if t not in text_cache[typ] or now - text_cache[typ][t] > SPERRZEIT]
    if not gültig:
        text_cache[typ] = {}
        gültig = texte[typ]
    if not gültig:
        print(f"{RED}[WARNUNG] Keine gültigen Einträge für {typ}{RESET}")
        return

    text = random.choice(gültig)
    text_cache[typ][text] = now

    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    color = {"flames": RED, "flames_enemy": RED, "dad": YELLOW, "nice": GREEN}.get(typ, RESET)
    label = {"flames": "[TEAM-FLAME]", "flames_enemy": "[ENEMY-FLAME]", "dad": "[DADJOKE]", "nice": "[NICE]"}.get(typ, "[TEXT]")

    print(f"{color}[{timestamp}] {label} {text}{RESET}")

    if typ == "dad" and config["dad_intro_enabled"]:
        text = f"{config['dad_intro_text']} {text}"
    elif typ == "flames" and config["flame_intro_team"]:
        text = f"{config['flame_intro_team_text']} {text}"
    elif typ == "flames_enemy" and config["flame_intro_enemy"]:
        text = f"{config['flame_intro_enemy_text']} {text}"

    if typ == "flames":
        chatkey = config['chat_key_nice']
    elif typ == "flames_enemy":
        chatkey = config['chat_key']
    elif typ == "nice":
        chatkey = config['chat_key_nice']
    else:
        chatkey = config['chat_key']

    tippe(text, chatkey)

def version_anzeigen():
    version = "TURBOFLAME V0.9 by spaceinvader.at"
    print(rainbow(f"[INFO] {version}"))
    tippe(version, config['chat_key'])

def on_press(key):
    try:
        key_str = str(key).lower()
        if str(config['hotkey_flame_team']).lower() in key_str:
            sende_text("", "flames")
        elif str(config['hotkey_flame_enemy']).lower() in key_str:
            sende_text("", "flames_enemy")
        elif str(config['hotkey_dad']).lower() in key_str:
            sende_text("", "dad")
        elif str(config['hotkey_nice']).lower() in key_str:
            sende_text("", "nice")
        elif str(config['hotkey_version']).lower() in key_str:
            version_anzeigen()
        elif str(config['exit_key']).lower() in key_str:
            print(f"{CYAN}[INFO] Exit-Key gedrückt – beende TurboFlame.{RESET}")
            return False
    except Exception as e:
        print(f"{RED}[FEHLER] Tastenerkennung: {e}{RESET}")

def starte_listener():
    print(f"{CYAN}[INFO] Lausche auf Hotkeys...{RESET}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    lade_config()
    global texte
    texte = {
        "flames": [],
        "flames_enemy": [],
        "dad": [],
        "nice": []
    }
    starte_listener()

if __name__ == "__main__":
    main()
