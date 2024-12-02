import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pywhatkit import sendwhatmsg_instantly
from time import sleep
from pyautogui import hotkey, press
from pyperclip import copy

def send_message():
    country_code = country_code_var.get()
    phone_number = phone_number_entry.get()
    message = message_text.get("1.0", tk.END)
    iterations = iterations_entry.get()
    if not phone_number or not message or not iterations:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return
    try:
        iterations = int(iterations)
        num = int(phone_number)
        if iterations <= 0:
            raise ValueError
        messagebox.showinfo("Success", f"Message will be sent {iterations} time(s)!")
    except ValueError:
        messagebox.showerror("Input Error", "Iterations must be a positive integer!")
    else:
        copy(message)
        sleep(2)
        sendwhatmsg_instantly(country_code+phone_number,message,12)
        sleep(1)
        for i in range(iterations - 1):
            hotkey('ctrl', 'v')
            press('enter')







def insert_emoji(emoji):
    """Insert the selected emoji into the message text area."""
    message_text.insert(tk.END, emoji)

def change_theme(theme):
    if theme == "Light":
        root.style.theme_use("clam")
    elif theme == "Dark":
        root.style.theme_use("alt")
    else:
        root.style.theme_use("default")

# Root Window
root = tk.Tk()
root.title("WATSUPMESSEGESENDER-3.0")
root.geometry("510x610")
root.resizable(False,False)
root.configure(bg="#f5f5f5")

# Style
root.style = ttk.Style()
root.style.theme_use("clam")

# Header Frame
header_frame = ttk.Frame(root)
header_frame.pack(fill=tk.X, padx=10, pady=5)

# Main Header Label
header_label = ttk.Label(header_frame, text="WATSUPMESSEGESENDER", font=("Arial", 16, "bold"))
header_label.pack(side=tk.LEFT, anchor=tk.W)
'''
# Theme Dropdown
theme_var = tk.StringVar(value="Default")
theme_dropdown = ttk.OptionMenu(header_frame, theme_var, "Default", "Light", "Dark", command=change_theme)
theme_dropdown.pack(side=tk.RIGHT, anchor=tk.E)
'''




'''# Theme Selection Dropdown
theme_var = tk.StringVar(value="Default")
theme_dropdown_label = ttk.Label(root, text="Select Theme:", background="#f5f5f5")
theme_dropdown_label.pack(anchor=tk.NE, pady=(10, 0), padx=10)
theme_dropdown = ttk.OptionMenu(root, theme_var, "Default", "Light", "Dark", command=change_theme)
theme_dropdown.pack(anchor=tk.NE, pady=(0, 10), padx=10)'''

# Country Code and Phone Number Frame
phone_frame = ttk.Frame(root)
phone_frame.pack(fill=tk.X, padx=10, pady=5)

# Country Code Dropdown
country_code_var = tk.StringVar(value="+1")
country_code_label = ttk.Label(phone_frame, text="Country Code:")
country_code_label.pack(side=tk.LEFT, padx=(0, 5))
country_code_dropdown = ttk.Combobox(phone_frame, textvariable=country_code_var, state="readonly", width=6)
country_code_dropdown['values'] = ["+1", "+44", "+91", "+61", "+81", "+86"]  # Add more codes as needed
country_code_dropdown.pack(side=tk.LEFT, padx=(0, 10))

# Phone Number Input
phone_number_label = ttk.Label(phone_frame, text="Phone Number:")
phone_number_label.pack(side=tk.LEFT)
phone_number_entry = ttk.Entry(phone_frame)
phone_number_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Message Text Area
ttk.Label(root, text="Message:", background="#f5f5f5").pack(anchor=tk.W, padx=10, pady=(10, 0))
message_text = tk.Text(root, height=6, wrap=tk.WORD)
message_text.pack(fill=tk.BOTH, padx=10, pady=5)

# Emoji Frame (Scrollable)
emoji_frame = ttk.Frame(root)
emoji_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Canvas and Scrollbar
canvas = tk.Canvas(emoji_frame, bg="#f5f5f5", highlightthickness=0)
scrollbar = ttk.Scrollbar(emoji_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", )
canvas.configure(yscrollcommand=scrollbar.set,height=120)

# Pack Canvas and Scrollbar
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Emoji Options
emoji_options = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
    "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚",
    "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸",
    "🤩", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️",
    "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡",
    "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓",
    "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄",
    "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵"
]

# Create a 7x4 Emoji Grid
columns = 8  # Number of emojis per row
for i, emoji in enumerate(emoji_options):
    row, col = divmod(i, columns)
    emoji_button = ttk.Button(scrollable_frame, text=emoji, width=4, command=lambda e=emoji: insert_emoji(e))
    emoji_button.grid(row=row, column=col, padx=5, pady=5)

# Iterations Input
ttk.Label(root, text="Iterations:", background="#f5f5f5").pack(anchor=tk.W, padx=10, pady=(10, 0))
iterations_entry = ttk.Entry(root)
iterations_entry.pack(fill=tk.X, padx=10, pady=5)

# Send Button
send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Run Application
root.mainloop()