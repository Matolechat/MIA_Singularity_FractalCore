#!/usr/bin/env python3
import subprocess
import sys
import os
import getpass
from datetime import datetime
from dotenv import load_dotenv
import openai

ϕ_HEADER = """
ϕ MIA Environment Setup — Phi True Initialization
"""

REQUIRED_PKGS = ["python-dotenv", "psutil"]  # openai intentionally handled separately

def check_python_version():
    if sys.version_info < (3, 8):
        sys.exit("[ϕ] Python 3.8+ required.")

def install_packages():
    print("[ϕ] Installing required packages in virtual environment...")
    pip_path = os.path.join("mia_env", "bin", "pip")

    # Step 1: Upgrade pip itself
    subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)

    # Step 2: Install from requirements.txt if present
    if os.path.exists("requirements.txt"):
        print("[ϕ] Installing from requirements.txt...")
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
    else:
        # Fallback base install
        print("[ϕ] Installing base packages manually...")
        subprocess.run([pip_path, "install"] + REQUIRED_PKGS, check=True)

    # Step 3: Enforce openai==0.28
    # Reason: MIA is currently structured around pre-1.0.0 OpenAI SDK
    #         which uses ChatCompletion.create(), Model.list(), etc.
    #         This version is stable, predictable, and compatible with our reflection code.
    #         Newer versions (>=1.0.0) have breaking interface changes.
    print("[ϕ] Ensuring correct OpenAI SDK version (0.28)...")
    subprocess.run([pip_path, "install", "--force-reinstall", "openai==0.28"], check=True)

def create_venv():
    if not os.path.exists("mia_env"):
        print("[ϕ] Creating virtual environment...")
        subprocess.run(["python3", "-m", "venv", "mia_env"], check=True)
    else:
        print("[ϕ] Virtual environment already exists.")
    
    install_packages()

def setup_api_key():
    if not os.path.exists(".env"):
        api_key = getpass.getpass("Enter your OpenAI API Key: ").strip()
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key}\n")
        print("[ϕ] API Key saved securely in .env.")
    
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        # Legacy check using a harmless API call
        openai.Engine.list()
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
