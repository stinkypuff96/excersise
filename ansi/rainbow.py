import os
import time
from no_echo import disable_echo

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
frame_count = segment_width * color_count


def print_rainbow(frame: int) -> None:
    output = '\033[999A\r'
    t_width, t_height = os.get_terminal_size()
    for line in range(0, t_height):
        line_frame = (frame + line) % frame_count
        start_color = line_frame // segment_width
        offset = line_frame % segment_width
        output += f'\033[{colors[start_color]}m{character * (segment_width - offset)}'
        for color_index in range(start_color + 1, start_color + color_count - 1):
            output += f'\033[{colors[color_index % color_count]}m{character * segment_width}'

        output += f'\033[{colors[(start_color + color_count - 1) % color_count]}m{character * offset}'
        output += '\n'

    output = output[0:-1]

    print(output, end='', flush=True)


current_frame = 0
try:
    disable_echo(enabled=False)
    print('\033[?25l\033[?1049h\033[2J', end='', flush=True)
    while True:
        print_rainbow(current_frame)
        current_frame = (current_frame + 1) % frame_count
        time.sleep(0.1)
except KeyboardInterrupt:
    disable_echo(enabled=True)
    print(f'\033[?25h\033[?1049l', end='', flush=True)
