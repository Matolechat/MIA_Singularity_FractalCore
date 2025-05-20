#!/bin/bash

# [MIA NOTE] Screen-based dual-panel interface for Termux compatibility

SESSION="mia_uix"
TOP_FILE="core/mia_core.py"
BOTTOM_FILE="core/mia_self_rewrite.py"

# Kill existing session if needed
screen -S "$SESSION" -X quit >/dev/null 2>&1

# Launch new screen session with vertical split (only one terminal needed)
screen -dmS "$SESSION" bash

# Create two windows
screen -S "$SESSION" -X screen -t "MIA-CORE"
screen -S "$SESSION" -p "MIA-CORE" -X stuff $"vim $TOP_FILE\n"

screen -S "$SESSION" -X screen -t "MIA-EXEC"
screen -S "$SESSION" -p "MIA-EXEC" -X stuff $"watch -n 1 'clear && python3 $BOTTOM_FILE'\n"

# Focus first panel
screen -r "$SESSION"
