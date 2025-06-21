# Minimal UI stub (Tkinter)
import tkinter as tk

def on_patch():
    print("Triggering patch agent...")

root = tk.Tk()
root.title("MythForge Runtime")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="MythForge Runtime Interface")
label.pack()

patch_btn = tk.Button(frame, text="Run Patch Agent", command=on_patch)
patch_btn.pack(pady=10)

root.mainloop()