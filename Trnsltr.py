import winsound
import threading
import tkinter as tk
from time import sleep
from Service import LANGUAGES, LANG_MORSE_MAPS, DOTIME, FREQUENCY


def copy_text():
    """Copies the output of the translator to clipboard."""
    win.clipboard_clear()
    to_copy = output_box.cget("text")
    win.clipboard_append(to_copy)
    win.update()


def on_focus_in_entry(event):
    """Removes the placeholder text in the input window."""
    if entry.get() == "Enter your text here...":
        entry.delete(0, tk.END)
        entry.config(fg="black")


def on_focus_out_entry(event):
    """Makes placeholder text in the input window."""
    if entry.get() == "":
        entry.insert(0, "Enter your text here...")
        entry.config(fg="grey")


def decode(msg):
    """Translates morse to language."""
    decoded = ""
    msg = msg.replace("_", "-")
    for let in msg.split():
        if let == "/":
            decoded += " "
        else:
            decoded += LANG_MORSE_MAPS[selected_language][1][let]
    return decoded


def encode(msg):
    """Translates the message to morse."""
    encoded = ""
    for let in msg:
        if let == " ":
            encoded += "/ "
        elif let in ".:!?,;'{}()":
            continue
        else:
            encoded += f"{LANG_MORSE_MAPS[selected_language][0][let.upper()]} "
    return encoded


def translate():
    """Translates the morse to alphabet and vise versa if morse is given."""
    user_input = entry.get()
    try:
        if any(x.isalnum() for x in user_input):
            output = encode(user_input)
        else:
            output = decode(user_input)
        output_box.config(text="")
        output_box.config(text=output)
    except KeyError:
        return "Please use valid English characters."


def toggle_side_menu():
    """Toggles languages menu"""
    global sidemenu_visible
    if sidemenu_visible:
        sidebar.place_forget()
        sidemenu_visible = False
    else:
        sidebar.place(x=0, y=0, relheight=1.0, width=100)
        sidebar.lift()
        sidemenu_visible = True


def on_mousewheel(event):
    """Makes it so languages menu can be scrolled up and down"""
    sidecanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def select_language(lan):
    """Selects a language from the side menu."""
    global selected_language
    selected_language = lan
    toggle_side_menu()
    toggle_btn.config(text=f"☰ {selected_language}")


def play_message():
    code = output_box.cget("text")

    if any(x not in ".- /" for x in code):
        ...
    else:

        def audio_service():
            for el in code:
                if el == "-":
                    winsound.Beep(FREQUENCY, DOTIME * 3)
                    sleep(DOTIME / 1000)
                elif el == ".":
                    winsound.Beep(FREQUENCY, DOTIME)
                    sleep(DOTIME / 1000)
                elif el == " ":
                    sleep((2 * DOTIME) / 1000)
                elif el == "/":
                    sleep((6 * DOTIME) / 1000)

        sound_sequence = threading.Thread(target=audio_service, daemon=True)
        sound_sequence.start()


def flash_morse_sequence():
    code = output_box.cget("text")
    if not code:
        return
    flash_win = tk.Toplevel(win)
    flash_win.title("Visual Flash")
    flash_win.geometry("300x300")
    flash_win.configure(bg="black")
    timeline = []
    for el in code:
        if el == ".":
            timeline.append(("white", DOTIME))
            timeline.append(("black", DOTIME))
        elif el == ",":
            timeline.append(("white", DOTIME * 3))
            timeline.append(("black", DOTIME))
        elif el == " ":
            timeline.append(("black", DOTIME * 2))
        elif el == "/":
            timeline.append(("black", DOTIME * 6))

    def process_el(ind):
        if ind < len(timeline):
            color, duration = timeline[ind]
            flash_win.configure(bg=color)
            flash_win.after(duration, lambda: process_el(ind + 1))
        else:
            flash_win.configure(bg="black")
            flash_win.after(500, flash_win.destroy)

    process_el(0)


selected_language = "English"

# Root Window
win = tk.Tk()
win.resizable(False, False)
win.title("MorseWave")
win.geometry("500x250")
win.configure(bg="#F0EEE9")
entry = tk.Entry(win, fg="#c4c3c0")
entry.insert(0, "Enter your text here...")
entry.bind("<FocusIn>", on_focus_in_entry)
entry.bind("<FocusOut>", on_focus_out_entry)
name = tk.Text(
    win,
    width=500,
    height=1,
    wrap="word",
    font=("Arial", 20),
    bg="#F0EEE9",
    borderwidth=5,
)
name.tag_configure("center", justify="center")
name.insert(tk.END, "MorseWave Translator", "center")
name.config(state="disabled", fg="#00422b")
version = tk.Text(
    win,
    width=100,
    height=1,
    wrap="word",
    font=("Arial", 8),
    bg="#f0f0f0",
    borderwidth=0,
)
version.insert(tk.END, "v1.0", "left")
version.config(fg="#a0a0a0", state="disabled")
version.place(y=230)
tr_btn = tk.Button(win, text="Convert", command=translate, bg="#dedcd7", fg="#00422b")
tr_btn.bind("<Enter>", lambda x: tr_btn.config(bg="#c4c3c0"))
tr_btn.bind("<Leave>", lambda x: tr_btn.config(bg="#dedcd7"))
output_box = tk.Message(win, text="", width=320, fg="#043222")
copy_btn = tk.Button(win, text="Copy", command=copy_text, bg="#dedcd7", fg="#00422b")
copy_btn.bind("<Enter>", lambda x: copy_btn.config(bg="#c4c3c0"))
copy_btn.bind("<Leave>", lambda x: copy_btn.config(bg="#dedcd7"))
copy_btn.place(x=190, y=170)
play_btn = tk.Button(win, text="Play", command=play_message, bg="#dedcd7", fg="#00422b")
play_btn.bind("<Enter>", lambda x: play_btn.config(bg="#c4c3c0"))
play_btn.bind("<Leave>", lambda x: play_btn.config(bg="#dedcd7"))
play_btn.place(x=235, y=170)
flash_btn = tk.Button(win, text="Flash", command=flash_morse_sequence, bg="#dedcd7", fg="#00422b")
flash_btn.bind("<Enter>", lambda x: flash_btn.config(bg="#c4c3c0"))
flash_btn.bind("<Leave>", lambda x: flash_btn.config(bg="#dedcd7"))
flash_btn.place(x=275, y=170)

# Side menu section
sidebar = tk.Frame(win, bg="#dedcd7", width=80)
sidecanvas = tk.Canvas(sidebar, bg="#dedcd7", highlightthickness=0, width=40)
scrollbar = tk.Scrollbar(sidebar, orient="vertical", command=sidecanvas.yview)
scrollframe = tk.Frame(sidecanvas, bg="#dedcd7")
scrollframe.bind(
    "<Configure>", lambda x: sidecanvas.configure(scrollregion=sidecanvas.bbox("all"))
)
sidecanvas.create_window((0, 0), window=scrollframe, anchor="nw")
sidecanvas.configure(yscrollcommand=scrollbar.set)
sidecanvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
sidecanvas.bind_all("<MouseWheel>", on_mousewheel)
sidemenu_visible = False
for lang in LANGUAGES:
    tk.Button(
        scrollframe,
        text=lang,
        command=lambda x=lang: select_language(x),
        bg="#dedcd7",
        fg="#00422b"
    ).pack(fill="x", padx=5, pady=2)
toggle_btn = tk.Button(
    win, text=f"☰ {selected_language}", command=toggle_side_menu, bg="#dedcd7", fg="#00422b"
)
toggle_btn.bind("<Enter>", lambda x: toggle_btn.config(bg="#c4c3c0"))
toggle_btn.bind("<Leave>", lambda x: toggle_btn.config(bg="#dedcd7"))
toggle_btn.place(x=10, y=10)

# Root Pack Section
name.pack(pady=1)
output_box.pack(pady=10)
entry.pack(pady=10)
tr_btn.pack(pady=10)
output_box.pack(pady=10)
win.mainloop()
