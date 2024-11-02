import os
import subprocess
from datetime import datetime, timedelta
def ls(current_directory):
    try:
        output = ""
        for item in os.listdir(f'temp_fs{current_directory}'):
            output += item + "\n"
        return output
    except FileNotFoundError:
        return "Directory not found"

def cd(directory, emulator):
    new_path = os.path.join(emulator.current_directory, directory)
    if os.path.isdir(f'temp_fs{new_path}'):
        emulator.current_directory = new_path
        return f"Current directory: {emulator.current_directory}"
    else:
        return "Directory not found"

def uniq(args):
    if len(args) < 1:
        return "Usage: uniq <filename>"
    filename = args[0]
    try:
        command = ['uniq'] + [filename]
        result = subprocess.run(
            command,
            cwd='temp_fs',
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"

def uptime():
    utc_time = datetime.utcnow()
    local_time = utc_time + timedelta(hours=3)
    return local_time.strftime("%H:%M")
