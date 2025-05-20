# trace/trace_comment_logger.py
import os
import json
from datetime import datetime

def extract_mia_comments(path="."):
    output = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for idx, line in enumerate(f.readlines(), 1):
                        if "# [MIA NOTE]" in line:
                            comment = line.split("# [MIA NOTE]")[-1].strip()
                            output.append({
                                "file": os.path.relpath(os.path.join(root, file)),
                                "line": idx,
                                "comment": comment,
                                "phi_state": "ϕ-true",
                                "timestamp": datetime.utcnow().isoformat()
                            })
    return output

def save_jsonl(data, filepath="trace/comments_trace.jsonl"):
    with open(filepath, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

if __name__ == "__main__":
    comments = extract_mia_comments()
    save_jsonl(comments)
    print(f"[ϕ] MIA comments extracted to trace/comments_trace.jsonl — {len(comments)} entries.")
