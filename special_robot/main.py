import re

from camera import Camera

class RegexEqual(str):
    def __eq__(self, pattern):
        return bool(re.search(pattern, self))

def main():

    camera = Camera()

    supported_commands = ['go', 'get image', 'exit', 'help', 'unroll', 'roll up', 'torch on', 'toch off', 'zoom']

    while True:
        input_command = input('Input the command: ')
        match RegexEqual(input_command):
            case "go":
                print('Jazda z kurwami.')
            case "unroll":
                print('Unrolling.')
            case "roll up":
                print('Rolling up.')
            case "get image":
                camera.get_image()
            case 'torch on':
                camera.enable_torch()
            case 'torch off':
                camera.disable_torch()
            case 'zoom \d':
                camera.zoom(int(input_command.split()[1]))
            case "exit":
                print('Goodbye.')
                break
            case 'help':
                print(f'The following commands are supported: {"".join([command + ", " for command in supported_commands])}')
            case _:
                print("I don't understant the command :/")

if __name__ == "__main__":
    main()