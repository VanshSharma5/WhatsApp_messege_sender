import tkinter as tk
from pywhatkit import sendwhatmsg_instantly
from tkinter import messagebox
from time import sleep
from pyautogui import write,press,keyDown,keyUp

def main():

    def insert_emoji():
        emoji = emoji_var.get()
        text_box.insert('end', emoji)

    def go_bro():
        try:
            mobile_number = mobile_number_entry.get()
            country_code = country_code_var.get()
            iterations = int(iterations_entry.get())
            messege = text_box.get("1.0", "end-1c")

            # Implement your message sending logic here
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            sleep(2)
            sendwhatmsg_instantly(country_code+mobile_number,messege,12)
            for i in range(iterations):
                for word in messege:
                    if word=='\n':
                        keyDown('shift')
                        keyDown('enter')
                        keyUp('shift')
                        keyUp('enter')
                    else:
                        write(word)
                press('enter')



# main function start 

    root = tk.Tk()
    root.resizable(0, 0)

    root.title("WATSUPMESSEGESENDER")

    country_code_label = tk.Label(root, text="Country Code")
    country_code_label.pack()
    country_code_var = tk.StringVar(root)
    country_code_var.set("Select Country Code") # default value
    country_code_options = ["+1", "+91", "+44", "+61", "+81"] # add more country codes as needed
    country_code_menu = tk.OptionMenu(root, country_code_var, *country_code_options)
    country_code_menu.pack()

    mobile_number_label = tk.Label(root, text="Mobile Number")
    mobile_number_label.pack()
    mobile_number_entry = tk.Entry(root)
    mobile_number_entry.pack()

    text_message_label = tk.Label(root, text="Text Message")
    text_message_label.pack()
    text_box = tk.Text(root, height=10, width=50)
    text_box.pack()

    emoji_var = tk.StringVar(root)
    emoji_var.set("Select Emoji") # default value
    emoji_options = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾"]
    emoji_menu = tk.OptionMenu(root, emoji_var, *emoji_options, command=lambda _: insert_emoji())
    emoji_menu.pack()

    iterations_label = tk.Label(root, text="Number of messeges send")
    iterations_label.pack()
    iterations_entry = tk.Entry(root)
    iterations_entry.pack()

    go_bro_button = tk.Button(root, text="ATTACK", command=go_bro)
    go_bro_button.pack()

    root.mainloop()
if __name__=='__main__':
    main()