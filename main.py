import toml
from emulator import Emulator

def main():
    config = toml.load('config.toml')
    fs_path = config['filesystem']['path']
    emulator = Emulator(fs_path)
    emulator.run()

if __name__ == "__main__":
    main()

