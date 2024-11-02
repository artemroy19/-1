import tarfile
from commands import ls, cd, uniq, uptime
import tkinter as tk


class Emulator:
    def __init__(self, fs_path):
        self.fs_path = fs_path
        self.current_directory = '/'
        self.extract_filesystem()
        self.root = tk.Tk()
        self.root.title("Shell Emulator")
        self.entry = tk.Entry(self.root)
        self.entry.bind("<Return>", self.on_enter)
        self.entry.pack()
        self.text_box = tk.Text(self.root)
        self.text_box.pack()

    def extract_filesystem(self):
        with tarfile.open(self.fs_path) as tar:
            tar.extractall(path='temp_fs')

    def run(self):
        self.root.mainloop()

    def on_enter(self, event):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        output = self.execute_command(command)
        self.text_box.insert(tk.END, output + "\n")

    def execute_command(self, command):
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == 'ls':
            return ls(self.current_directory)
        elif cmd == 'cd':
            return cd(args[0], self)
        elif cmd == 'uniq':
            return uniq(args)
        elif cmd == 'uptime':
            return uptime()
        elif cmd == 'exit':
            return exit()
        else:
            return "Unknown command"

