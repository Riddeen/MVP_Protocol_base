from __future__ import annotations 
from typing import Protocol

from models.model import Model

from presenters.control_presenter import ControlPresenter
from views.control_view import ControlView


class View(Protocol):
    def init_ui(self, presenter: Presenter) -> None:
        ...
        
    def get_entry(self) -> str:
        ...
        
    def set_entry(self, value: str) -> None:
        ...
        
    def mainloop(self) -> None:
        ...

class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        
    def handle_print_value_a(self, event=None) -> None:
        if self.view.get_entry() != '':
            self.view.set_entry('')
        else:
            self.view.set_entry(self.model.value_a)
            
    def init_ui(self) -> None:
        self.view.init_ui(self)
        
        self.control_view = ControlView(self.view)
        self.control_presenter = ControlPresenter(self.model, self.control_view)
        self.control_presenter.init_ui()
            
    def run(self) -> None:
        self.init_ui()
        self.view.mainloop()