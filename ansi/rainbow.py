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

line_count = 10
segment_width = 15
character = '\u2588'
frame_count = segment_width * color_count

def print_rainbow(frame: int) -> None:
    output = ''

    for line in range(0, line_count):
        line_frame = (frame + line) % frame_count
        start_color = line_frame // segment_width
        offset = line_frame % segment_width
        output += f'\033[{colors[start_color]}m{character * (segment_width - offset)}'
        for color_index in range(start_color + 1, start_color + color_count - 1):
            output += f'\033[{colors[color_index % color_count]}m{character * segment_width}'

        output += f'\033[{colors[(start_color + color_count - 1) % color_count]}m{character * offset}'
        output += '\n'

    output += f'\033[{line_count + 1}A'
    print(output)


current_frame = 0
try:
    disable_echo(enabled=False)
    while True:
        print_rainbow(current_frame)
        current_frame = (current_frame + 1) % frame_count
        time.sleep(0.1)
except KeyboardInterrupt:
    disable_echo(enabled=True)
    print('\033[2K\033[B'* line_count + f'\033[{line_count}A\r', end='', flush=True)