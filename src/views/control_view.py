from enum import auto
import tkinter as tk
from tkinter import ttk
from typing import Protocol



class ControlPresenter(Protocol):
    def handle_inc_value_b(self, event=None) -> None:
        ...
        
    def handle_dec_value_b(self, event=None) -> None:
        ...

class ControlView(ttk.Frame):
    def __init__(self, container: tk.Tk) -> None:
        super().__init__(container)
        
    def init_ui(self, presenter: ControlPresenter) -> None:     
        self.entry_var = tk.StringVar(value='')
        self.entry = ttk.Entry(self, textvariable=self.entry_var)
        self.entry.pack()
                   
        self.button_inc = ttk.Button(self, text='+')
        self.button_inc.pack(side=tk.LEFT)
        self.button_inc.bind('<Button-1>', presenter.handle_inc_value_b)
        
        self.button_dec = ttk.Button(self, text='-')
        self.button_dec.pack(side=tk.LEFT)
        self.button_dec.bind('<Button-1>', presenter.handle_dec_value_b)
        
    def get_entry(self) -> str:
        return self.entry_var.get()
    
    def set_entry(self, value: str) -> None:
        self.entry_var.set(value)