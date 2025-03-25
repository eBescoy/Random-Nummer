import random
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Nummer generator")
    root.geometry("400x500")
    
    result_label = tk.Label(
        root,
        text="Drücken um zu starten!",
        font=("Roboto Condensed", 24),
        fg="black"
    )
    result_label.pack(pady=20)

    def generate_number():
        random_number = random.randint(1, 100)
        result_label.config(text=f"{random_number}")

    button = tk.Button(
        root,
        text="Nummer generieren",
        width=17,
        height=7,
        bg="Orange",
        fg="Black",
        font=("Oswald", 20),
        command=generate_number
    )
    button.pack()
    button.pack()
    root.mainloop()
    root.mainloop()

