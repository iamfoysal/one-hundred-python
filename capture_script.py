import time
import pyautogui
import keyboard

# Global variable to track script termination
terminate_script = False

def capture_screenshot():
    # Get the current timestamp
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    # Save the screenshot with a timestamped filename
    filename = f'screenshot_{timestamp}.png'
    screenshot.save(filename)
    print(f'Screenshot captured: {filename}')

def on_keypress(event):
    global terminate_script
    # Check if the key combination Ctrl + U was pressed
    if event.name == 'u' and keyboard.is_pressed('ctrl'):
        terminate_script = True
        print('Script termination requested.')

# Register the keypress event handler
keyboard.on_press(on_keypress)
# Set the interval in seconds (1 minutes = 60 seconds)
interval = 30
# Capture screenshots until termination requested
while not terminate_script:
    # Capture a screenshot
    capture_screenshot()
    # Wait for the specified interval
    time.sleep(interval)
# Unregister the keypress event handler
keyboard.unhook_all()



