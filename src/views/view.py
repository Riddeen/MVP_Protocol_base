import tkinter as tk
from tkinter import ttk
from typing import Protocol

TITLE = "MVP with Protocol"


class Presenter(Protocol):
    def handle_print_value_a(self, event=None) -> None:
        ...

class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(TITLE)
        self.geometry("500x300")
        
    def init_ui(self, presenter: Presenter) -> None:
        frame = ttk.Frame(self)
        frame.pack(side=tk.LEFT)
        
        self.button = ttk.Button(frame, text='Print value A')
        self.button.pack()
        self.button.bind('<ButtonRelease-1>', presenter.handle_print_value_a)
        
        self.entry_var = tk.StringVar(value='')
        self.entry = ttk.Entry(frame, textvariable=self.entry_var)
        self.entry.pack()
        
    def get_entry(self) -> str:
        return self.entry_var.get()
    
    def set_entry(self, value: str) -> None:
        self.entry_var.set(value)