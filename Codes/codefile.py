
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30, justify="right", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            ]

        self.buttons = []
        for i, text in enumerate(button_texts):
            row = i // 4 + 1
            col = i % 4
            button = tk.Button(master, text=text, width=7, height=2, font=("Arial", 11),
                               command=lambda text=text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

        clear_button = tk.Button(master, text="AC", width=15, height=2, font=("Arial", 11),
                                 command=lambda: self.clear())
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        equals_button = tk.Button(master, text="=", width=7, height=2, font=("Arial", 11),
                                  command=lambda: self.equals())
        equals_button.grid(row=5, column=2, padx=5, pady=5)

    def button_click(self, text):
        self.display.insert(tk.END, text)

    def clear(self):
        self.display.delete(0, tk.END)

    def equals(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except (SyntaxError, ZeroDivisionError):
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
