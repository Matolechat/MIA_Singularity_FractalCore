# tools/mia_uix_compact.py

# [MIA NOTE] Compact UIX for Termux — split interface with live execution
# [ϕ] PHI-ACTIVE: Minimal terminal rendering with coherence feedback

import curses
import subprocess
import threading
import os

# [MIA NOTE] Source and execution paths (modifiable)
TOP_FILE = "core/mia_core.py"
BOTTOM_FILE = "core/mia_self_rewrite.py"

# [MIA NOTE] Load source file contents
def load_file(path):
    try:
        with open(path, 'r') as f:
            return f.readlines()
    except:
        return ["[MIA] Unable to load file."]

# [MIA NOTE] Execute script and stream stdout
def run_script(path):
    return subprocess.Popen(["python3", path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# [MIA NOTE] Compact dual-panel interface
def mia_ui(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()

    code_win = curses.newwin(max_y // 2, max_x, 0, 0)
    exec_win = curses.newwin(max_y // 2, max_x, max_y // 2, 0)

    code = load_file(TOP_FILE)
    exec_lines = []
    running_proc = None

    def draw_code():
        code_win.erase()
        code_win.box()
        code_win.addstr(0, 2, f" MIA CORE VIEW :: {TOP_FILE[:max_x - 20]}")
        for idx, line in enumerate(code[:code_win.getmaxyx()[0] - 3]):
            try:
                code_win.addstr(idx + 1, 2, line.strip()[:max_x - 4])
            except:
                pass
        code_win.addstr(code_win.getmaxyx()[0]-1, 2, "[T] Reload | [R] Run | [Q] Quit")
        code_win.refresh()

    def draw_exec():
        exec_win.erase()
        exec_win.box()
        exec_win.addstr(0, 2, f" MIA SELF REWRITE OUTPUT :: {BOTTOM_FILE[:max_x - 30]}")
        for idx, line in enumerate(exec_lines[-(exec_win.getmaxyx()[0] - 3):]):
            try:
                exec_win.addstr(idx + 1, 2, line.strip()[:max_x - 4])
            except:
                pass
        exec_win.refresh()

    def refresh_exec_output():
        nonlocal exec_lines, running_proc
        exec_lines = []
        running_proc = run_script(BOTTOM_FILE)
        for line in iter(running_proc.stdout.readline, b''):
            exec_lines.append(line.decode())
            draw_exec()

    draw_code()
    draw_exec()

    while True:
        k = stdscr.getch()
        if k in (ord('q'), 27):  # Q or ESC
            break
        elif k in (ord('t'), ord('T')):
            code = load_file(TOP_FILE)
            draw_code()
        elif k in (ord('r'), ord('R')):
            threading.Thread(target=refresh_exec_output, daemon=True).start()

# [MIA NOTE] Point d’entrée principal
if __name__ == "__main__":
    curses.wrapper(mia_ui)
