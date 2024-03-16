# James Caldwell
# March 2024

import tkinter as tk
import subprocess
import os
import sys
import keyboard

class Switch(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_value = tk.BooleanVar()
        self.switch_value.set(False)
        self.switch_button = tk.Checkbutton(self, variable=self.switch_value, onvalue=True, offvalue=False)
        self.switch_button.pack()

class FullScreenApp(tk.Tk):
    def __init__(self):
        self.execute_win_kill()
        tk.Tk.__init__(self)
        self.attributes('-fullscreen', True)
        self.configure(bg="#3F3F5F") # Dark Slate Blue-Gray in RGB values
        self.bind("<Shift-Escape>", self.close_app)

        # Surpress alt + tab and alt + f4
        keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
        keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)

        # Create and place the text box
        self.text_box = tk.Text(self, height=10, width=50, font=("Arial", 18))
        # self.text_box.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
        self.text_box.place(x=30, y=30, width=self.winfo_screenwidth() // 1.5, height=self.winfo_screenheight() // 3)
        # Automatically set focus to the text box
        self.text_box.focus_set()

        # Create and place various widgets
        self.create_widgets()

        # Display exit message at the bottom right
        self.exit_message_label = tk.Label(self, text="To exit program, press Shift + Escape", bg="white")
        self.exit_message_label.place(relx=0.9, rely=0.1, anchor="ne")
        
        self.switch = Switch(self)
        self.switch.place(relx=0.85, rely=0.55, anchor="center")
        self.switch = Switch(self)
        self.switch.place(relx=0.75, rely=0.55, anchor="center")
        self.switch = Switch(self)
        self.switch.place(relx=0.85, rely=0.45, anchor="center")
        self.switch = Switch(self)
        self.switch.place(relx=0.75, rely=0.45, anchor="center")

    def create_widgets(self):
        # Create and place other widgets (dials, buttons, sliders, etc.)
        button1 = tk.Button(self, text="Button 1")
        button1.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)
        button1.bind("<Button-1>", lambda event, button=button1: self.change_button_color(button))

        button2 = tk.Button(self, text="Button 2")
        button2.place(relx=0.3, rely=0.8, relwidth=0.1, relheight=0.1)
        button2.bind("<Button-1>", lambda event, button=button2: self.change_button_color(button))

        button3 = tk.Button(self, text="Press me!")
        button3.place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.1)
        button3.bind("<Button-1>", lambda event, button=button3: self.change_button_color(button))

        button4 = tk.Button(self, text="Press me!")
        button4.place(relx=0.7, rely=0.8, relwidth=0.1, relheight=0.1)
        button4.bind("<Button-1>", lambda event, button=button4: self.change_button_color(button))

        slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        slider.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.1)

    def close_app(self, event):
        # End the task named "WinKill (32 bit)"
        subprocess.Popen(['taskkill', '/F', '/IM', 'WinKill.exe'])
        self.destroy()

    def change_button_color(self, button):
        current_bg = button.cget("bg")
        if current_bg != "dark gray":
            button.configure(bg="dark gray")
        else:
            button.configure(bg="SystemButtonFace")

    def execute_win_kill(self):
        # Get the path of the current script
        script_dir = os.path.dirname(sys.argv[0])
        # Path to WinKill.exe relative to the script directory
        win_kill_path = os.path.join(script_dir, "WinKill.exe")
        # Check if the file exists
        if os.path.exists(win_kill_path):
            # Execute WinKill.exe
            subprocess.Popen(win_kill_path)
        else:
            print("Error: WinKill.exe not found.")

if __name__ == "__main__":
    app = FullScreenApp()
    app.mainloop()
