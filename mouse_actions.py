import pyautogui
from screeninfo import get_monitors
import logging

# Configure logging
logging.basicConfig(filename='mouse_actions.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Get a list of monitor objects
monitors = get_monitors()

# Print information about each monitor
for monitor in monitors:
    print(f"Monitor Name: {monitor.name}")
    print(f"Monitor Width: {monitor.width} pixels")
    print(f"Monitor Height: {monitor.height} pixels")
    print(f"Monitor X Position: {monitor.x} pixels from the left")
    print(f"Monitor Y Position: {monitor.y} pixels from the top")
    print("\n")



class MouseActionError(Exception):
    pass

def handle_mouse_exception(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except pyautogui.FailSafeException as e:
            raise MouseActionError(f"Musåtgärd misslyckades (FailSafeException) i funktionen: {func.__name__}. Felmeddelande: {str(e)}")
    return wrapper


class MouseConfig:
    def __init__(self, duration=0.5, scroll_amount=1):
        self.duration = duration
        self.scroll_amount = scroll_amount

    def set_duration(self, duration):
        self.duration = duration

    def set_scroll_amount(self, scroll_amount):
        self.scroll_amount = scroll_amount


# Initialize with default settings
config = MouseConfig()

def scroll(direction='up', amount=1):
    if direction == 'up':
        pyautogui.scroll(amount)  # Scroll up
    elif direction == 'down':
        pyautogui.scroll(-amount)  # Scroll down


# Usage in functions
@handle_mouse_exception
def flytta_vänster(pixels=100):
    """
    Flytta musen åt vänster.
    
    Args:
        pixels (int): Antal pixlar att flytta åt vänster (standard: 100).
    """
    pyautogui.move(-pixels, 0, duration=config.duration)
    logging.info("Flyttade musen åt vänster.")  # Log the action

@handle_mouse_exception
def flytta_höger(pixels=100):
    """
    Flytta musen åt höger.
    
    Args:
        pixels (int): Antal pixlar att flytta åt höger (standard: 100).
    """
    pyautogui.move(pixels, 0, duration=config.duration)
    logging.info("Flyttade musen åt höger.")  # Log the action

@handle_mouse_exception
def flytta_upp(pixels=100):
    """
    Flytta musen uppåt.
    
    Args:
        pixels (int): Antal pixlar att flytta uppåt (standard: 100).
    """
    pyautogui.move(0, -pixels, duration=config.duration)
    logging.info("Flyttade musen uppåt.")  # Log the action

@handle_mouse_exception
def flytta_ner(pixels=100):
    """
    Flytta musen neråt.
    
    Args:
        pixels (int): Antal pixlar att flytta neråt (standard: 100).
    """
    pyautogui.move(0, pixels, duration=config.duration)
    logging.info("Flyttade musen neråt.")  # Log the action

@handle_mouse_exception
def klicka(button='vänster'):
    """
    Utför en musklickhandling.

    Args:
        button (str): Typen av klick (vänster, höger, dubbel).

    Raises:
        MouseActionError: Om klickhandling misslyckas.
    """
    if button == 'vänster':
        pyautogui.click()
        logging.info("Vänsterklick utförd.")  # Log the action
    elif button == 'höger':
        pyautogui.rightClick()
        logging.info("Högerklick utförd.")  # Log the action
    elif button == 'dubbel':
        pyautogui.doubleClick()
        logging.info("Dubbelklick utförd.")  # Log the action