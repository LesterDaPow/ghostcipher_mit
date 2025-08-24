#!/usr/bin/env python3
import os
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox

REPO_URL = "https://github.com/LesterDaPow/ghostcipher_mit.git"
INSTALL_DIR = os.path.join(os.getcwd(), "ghostcipher_mit")

def install_or_update():
    def task():
        try:
            if os.path.exists(INSTALL_DIR):
                subprocess.check_call(["git", "-C", INSTALL_DIR, "pull", "origin", "master"])
                msg = "GhostCipher repository updated!"
            else:
                subprocess.check_call(["git", "clone", REPO_URL, INSTALL_DIR])
                msg = "GhostCipher repository cloned!"

            subprocess.check_call(["pip", "install", "--user", "-e", INSTALL_DIR])
            messagebox.showinfo("GhostCipher Installer", f"{msg}\nGhostCipher installed successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("GhostCipher Installer", f"Installation failed:\n{e}")

    threading.Thread(target=task, daemon=True).start()  # run in background

# GUI setup
root = tk.Tk()
root.title("GhostCipher Installer")
root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text="Install or update GhostCipher", font=("Arial", 14))
label.pack(pady=20)

install_btn = tk.Button(root, text="Install/Update", font=("Arial", 12), command=install_or_update)
install_btn.pack(pady=10)

root.mainloop()
