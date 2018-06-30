import keyboard
import soco

# Set Sonos Player IP
from soco import SoCo
my_zone = SoCo('192.168.1.134')

# Define volume up/down functions
def volumeup():
    my_zone.volume = my_zone.volume +2
    return;

def volumedown():
    my_zone.volume = my_zone.volume -2
    return;

# Volume up/down assignment to hotkeys
keyboard.add_hotkey('ctrl+shift+a', lambda: volumeup())
keyboard.add_hotkey('ctrl+shift+s', lambda: volumedown())

# Blocks until you press esc.
keyboard.wait('esc')