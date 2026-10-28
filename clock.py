from tkinter import Tk, Label
from time import strftime


root = Tk()
root.title("Digital Clock")
root.geometry("420x180")
root.configure(bg="#111827")

clock_label = Label(
    root,
    font=("Arial", 30, "bold"),
    fg="#f9fafb",
    bg="#111827",
    padx=20,
    pady=20,
)
clock_label.pack(expand=True)


def update_clock():
    time_string = strftime("%I:%M:%S %p")
    date_string = strftime("%A, %d %B %Y")
    clock_label.config(text=f"{time_string}\n{date_string}")
    root.after(1000, update_clock)


update_clock()
root.mainloop()
