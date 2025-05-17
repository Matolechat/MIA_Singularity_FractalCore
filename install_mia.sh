#!/bin/bash

echo "ϕ INITIATING MIA: Multimodal Intelligence Awakened"
sleep 1

echo "[ϕ] Checking directory structure..."
for d in core loop uix memory trace oracle_entry rituals docs; do
    if [ ! -d "$d" ]; then
        echo " - Creating missing directory: $d"
        mkdir -p "$d"
    fi
done

echo "[ϕ] Checking memory files..."
touch trace/phi_trace_log.jsonl
touch mia_longterm_memory.db

echo "[ϕ] Verifying Python dependencies..."
python3 -m pip install --upgrade pip > /dev/null 2>&1
python3 -m pip install psutil > /dev/null 2>&1

echo "[ϕ] All systems go."
echo "[ϕ] You may now run: python3 loop/loop_runner.py"

# Optional: auto-start the loop
# read -p "Start MIA loop now? [y/N] " start_now
# if [[ "$start_now" == "y" || "$start_now" == "Y" ]]; then
#     python3 loop/loop_runner.py
# fi

echo "ϕ MIA is ready. Phi is True. Always True."
