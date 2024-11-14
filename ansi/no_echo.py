import sys
import termios


def disable_echo(enabled: bool) -> None:
    fd = sys.stdin.fileno()
    iflag, oflag, cflag, lflag, ispeed, ospeed, cc = termios.tcgetattr(fd)
    if enabled:
        lflag |= termios.ECHO
    else:
        lflag &= ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, [iflag, oflag, cflag, lflag, ispeed, ospeed, cc])
