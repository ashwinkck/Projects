import curses #helping with styling of the terminal
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear() # Clearing the screen
    stdscr.addstr("Welcome to the speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!") # adding text in to the scrreen
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    stdscr.clear() # Clearing the screen
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # adding styling with foreground green and background white with an id 1
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)# Same shi with a second id
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)
    

wrapper(main)