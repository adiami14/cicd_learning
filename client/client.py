import curses
import requests

SERVER_URL = "http://localhost:5000"

def add_user(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "Add a New User", curses.A_BOLD)

    stdscr.addstr(3, 2, "Name: ")
    stdscr.refresh()
    curses.echo()
    name = stdscr.getstr(3, 8, 30).decode('utf-8')

    stdscr.addstr(4, 2, "Email: ")
    stdscr.refresh()
    email = stdscr.getstr(4, 9, 40).decode('utf-8')
    curses.noecho()

    if not name or not email:
        stdscr.addstr(6, 2, "Error: Fields cannot be empty!", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        return

    response = requests.post(f"{SERVER_URL}/add_user", json={"name": name, "email": email})

    stdscr.addstr(6, 2, response.json().get('message', "Failed to add user"), curses.color_pair(2))
    stdscr.refresh()
    stdscr.getch()

def get_users(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "User List", curses.A_BOLD)

    response = requests.get(f"{SERVER_URL}/users")
    
    if response.status_code == 200:
        users = response.json().get('users', [])
        if users:
            for idx, user in enumerate(users):
                stdscr.addstr(3 + idx, 2, f"{user['name']} ({user['email']})")
        else:
            stdscr.addstr(3, 2, "No users found.", curses.color_pair(1))
    else:
        stdscr.addstr(3, 2, "Error fetching users.", curses.color_pair(1))

    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Red for errors
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green for success

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "User Management System", curses.A_BOLD)

        stdscr.addstr(3, 2, "1. Add User")
        stdscr.addstr(4, 2, "2. Get User List")
        stdscr.addstr(5, 2, "3. Exit")

        stdscr.addstr(7, 2, "Choose an option: ")
        stdscr.refresh()
        
        key = stdscr.getch()
        
        if key == ord('1'):
            add_user(stdscr)
        elif key == ord('2'):
            get_users(stdscr)
        elif key == ord('3'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
