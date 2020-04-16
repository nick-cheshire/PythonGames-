import curses
import time


menu = ['Pong', 'Snake', 'Exit']





def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)
    while 1:
        screen = curses.initscr()
        title = "Nick's Arcade"
        z, i = stdscr.getmaxyx()
        s = i // 2 - len(title) // 2
        h = z // 4
        screen.addstr(h, s, title, curses.A_BOLD)
        screen.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, '{}'.format(menu[current_row]))
            stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                quit()
            if current_row == 1:
                import Snake 
            if current_row == 0:
                import Pong
        print_menu(stdscr, current_row)


curses.wrapper(main)

    

    