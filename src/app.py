import curses
from database.JsonAdapter import JsonAdapter
from database.DBAdapter import DBAdapter


def main(stdscr, db: DBAdapter):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    RED_PAIR = curses.color_pair(1)
    CYAN_PAIR = curses.color_pair(2)
    GREEN_PAIR = curses.color_pair(3)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "To Do List:", CYAN_PAIR)
        tasks = db.read_record(-1)
        for i, task in enumerate(tasks):
            stdscr.addstr(
                i + 1,
                0,
                f"{i}: {task.get('content')}",
                GREEN_PAIR if task.get("done", False) else RED_PAIR,
            )
        stdscr.refresh()
        key = stdscr.getkey()
        if key == "q":
            break
        elif key == "a":
            db.create_record({"id": len(tasks), "content": "New Task", "done": False})
        elif key == "d":
            db.delete_record(len(tasks) - 1)


if __name__ == "__main__":
    db = JsonAdapter("src/storage/database.json")
    db.connect()
    curses.wrapper(main, db)
    db.close()
