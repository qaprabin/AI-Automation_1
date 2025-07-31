from automation.rdtest_runner import run_rd_test
from utils.speech import speak

def handle_command(command):
    command = command.lower()

    if "rd test" in command or "run rd" in command:
        speak("Running the RD test automation script.")
        run_rd_test()

    else:
        speak("Sorry, I don't understand that command.")
