"""
56. Write a Python program to get height and the width of console window.
"""


def terminal_size():
    import fcntl
    import termios
    import struct
    th, tw, hp, wp = struct.unpack('HHHH',
                                   fcntl.ioctl(0, termios.TIOCGWINSZ,
                                               struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th


print('Number of columns and Rows: ', terminal_size())
