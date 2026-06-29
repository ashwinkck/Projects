import curses #helping with styling of the terminal
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE) # adding styling with foreground green and background white with an id 1
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)# Same shi with a second id
    stdscr.clear() # Clearing the screen
    stdscr.addstr("Hello World!", curses.color_pair(1)) # adding text in to the scrreen
    stdscr.refresh()# Refreshing the screen
    stdscr.getkey() # The covering in which of the o/p when we are putting the values

wrapper(main)