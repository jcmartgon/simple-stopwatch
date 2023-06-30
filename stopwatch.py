# Jesus Carlos Martinez Gonzalez
# 29/06/2023
# Simple Stopwatch App

# This app was made following this (https://www.youtube.com/watch?v=QBYUws70A7M&ab_channel=AlinaChudnova) tutorial made by youtuber Alina Chudnova

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch")
        self.geometry("300x250")

        self.time = 0  # Time value
        self.running = False  # Whether the clock is running or not

        # Themes
        self.style = ThemedStyle()
        self.style.set_theme("breeze")

        button_style = ttk.Style()
        button_style.configure("TButton", font=("Helvetica", 14))

        # Time label
        self.label = ttk.Label(
            self, text="00:00:00", padding="20", font=("Helvetica", 35)
        )
        self.label.pack()

        # Start button
        self.start_button = ttk.Button(
            self,
            text="Start",
            width=10,
            padding="10",
            command=self.start,
        )
        self.start_button.pack()

        # Stop button
        self.stop_button = ttk.Button(
            self,
            text="Stop",
            width=10,
            padding="10",
            command=self.stop,
        )
        self.stop_button.pack()

        # Reset button
        self.reset_button = ttk.Button(
            self,
            text="Reset",
            width=10,
            padding="10",
            command=self.reset,
        )
        self.reset_button.pack()

    # Functionality
    def start(self):
        self.running = True
        self.count()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

    def count(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(
                text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            )
            self.after(1000, self.count)


if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.mainloop()
