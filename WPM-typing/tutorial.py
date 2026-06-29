import curses #helping with styling of the terminal
from curses import wrapper

def main(stdscr):
    curses.use_default_colors()  # This line tells curses that -1 means "use the terminal's natural background"
    curses.init_pair(1, curses.COLOR_GREEN, -1) # adding styling with foreground green and background white with an id 1
    curses.init_pair(2, curses.COLOR_YELLOW, -1)# Same shi with a second id
    stdscr.clear() # Clearing the screen
    stdscr.addstr("Hello World!", curses.color_pair(1)) # adding text in to the scrreen
    stdscr.refresh()# Refreshing the screen
    stdscr.getkey() # The covering in which of the o/p when we are putting the values

wrapper(main)