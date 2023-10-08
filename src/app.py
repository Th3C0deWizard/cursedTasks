import curses


def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    RED_PAIR = curses.color_pair(1)
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello World !!!", RED_PAIR)
    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
