import sys
import os

# Ensures project directory is in sys.path so modules can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.speech import speak           # Importing the speak function
from agent.command_handler import handle_command  # Importing command handler

if __name__ == "__main__":
    speak("Hello Prabin, I am your AI agent. Ready to work!")  # Voice prompt
    command = input("Enter your command: ")                    # Take user input
    handle_command(command)                                    # Handle it

