import time

colors = [
    '38;5;160',  # red
    '38;5;166',  # orange
    '38;5;226',  # yellow
    '38;5;040',  # green
    '38;5;019',  # blue
    '38;5;021',  # light blue
    '38;5;056',  # purple
]

line_count = 10
segment_width = 15
character = '\u2588'


def print_rainbow(frame: int) -> None:
    output = ''

    for line in range(0, line_count):
        start_color = frame // segment_width
        offset = frame % segment_width
        output += f'\033[{colors[start_color]}m{character * (segment_width - offset)}'
        for color_index in range(start_color + 1, start_color + len(colors) - 1):
            output += f'\033[{colors[color_index % len(colors)]}m{character * segment_width}'

        output += f'\033[{colors[(start_color + len(colors) - 1) % len(colors)]}m{character * offset}'
        output += '\n'

    output += f'\033[{line_count + 1}A'
    print(output)


current_frame = 0

while True:
    print_rainbow(current_frame)
    current_frame = (current_frame + 1) % (segment_width * len(colors))
    time.sleep(0.1)
