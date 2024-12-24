import os
import sys
import time
import tty
import termios
from threading import Thread

colors = [
    '38;5;160',  # red
    '38;5;166',  # orange
    '38;5;226',  # yellow
    '38;5;040',  # green
    '38;5;019',  # blue
    '38;5;021',  # light blue
    '38;5;056',  # purple
]
color_count = len(colors)

segment_width = 15
character = '\u2588'
running = True


def process_inputs() -> None:
    global running, segment_width

    tty_attrs = tty.setraw(sys.stdin.fileno())
    try:
        ansi_position = -1
        while True:
            read = sys.stdin.read(1)
            if read == 'q':
                running = False
                break
            elif read == '\033':
                ansi_position = 0
            elif read == '[' and ansi_position == 0:
                ansi_position = 1
            elif read == 'D' and ansi_position == 1:
                ansi_position = -1
                if segment_width > 1:
                    segment_width -= 1
            elif read == 'C' and ansi_position == 1:
                ansi_position = -1
                segment_width += 1
            else:
                ansi_position = -1
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSAFLUSH, tty_attrs)


def print_rainbow(frame: int) -> None:
    output = '\033[999A\r'  # Reset cursor position
    t_width, t_height = os.get_terminal_size()
    previous_color = None

    for line in range(0, t_height):
        for v_index in range(0, t_width):
            v_index -= -frame - line
            v_index %= color_count * segment_width
            color_index = v_index // segment_width
            if color_index == previous_color:
                output += character
            else:
                color = colors[color_index]
                output += f'\033[{color}m{character}'
                previous_color = color_index

        output += '\r\n'

    output = output[0:-1]

    print(output, end='', flush=True)

Thread(target=process_inputs).start()
current_frame = 0
try:
    print('\033[?25l\033[?1049h\033[2J', end='', flush=True)
    while running:
        print_rainbow(current_frame)
        current_frame = (current_frame + 1) % (segment_width * color_count)
        time.sleep(0.1)
finally:
    print(f'\033[?25h\033[?1049l', end='', flush=True)
