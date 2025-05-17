#!/usr/bin/env python3
import subprocess, sys, os, getpass
from dotenv import load_dotenv
import openai

ϕ_HEADER = """
ϕ MIA Environment Setup — Phi True Initialization
"""

REQUIRED_PKGS = ["openai==0.28", "python-dotenv", "psutil"]

def check_python_version():
    if sys.version_info < (3, 8):
        sys.exit("[ϕ] Python 3.8+ required.")

def create_venv():
    if not os.path.exists("mia_env"):
        print("[ϕ] Creating virtual environment...")
        subprocess.run(["python3", "-m", "venv", "mia_env"], check=True)
    else:
        print("[ϕ] Virtual environment already exists.")
    print("[ϕ] Installing required packages in virtual environment...")
    subprocess.run(["mia_env/bin/pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run(["mia_env/bin/pip", "install"] + REQUIRED_PKGS, check=True)

def setup_api_key():
    if not os.path.exists(".env"):
        api_key = getpass.getpass("Enter your OpenAI API Key: ").strip()
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key}\n")
        print("[ϕ] API Key saved securely in .env.")
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        openai.Model.list()
        print("[ϕ] API key validated.")
    except Exception as e:
        sys.exit(f"[!] API key validation failed: {e}")

def verify_structure():
    dirs = ["core", "loop", "uix", "memory", "trace", "oracle_entry", "rituals", "docs"]
    for d in dirs:
        if not os.path.isdir(d):
            os.makedirs(d, exist_ok=True)
            print(f"[ϕ] Created missing directory: {d}")
    print("[ϕ] Directory structure verified.")

def main():
    print(ϕ_HEADER)
    check_python_version()
    create_venv()
    setup_api_key()
    verify_structure()
    print("[ϕ] MIA setup complete. Phi is True.")

if __name__ == "__main__":
    main()
