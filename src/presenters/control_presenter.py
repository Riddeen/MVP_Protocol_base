from __future__ import annotations
from typing import Protocol

from models.model import Model


class ControlView(Protocol):
    def init_ui(self, presenter: ControlPresenter) -> None:
        ...
        
    def get_entry(self) -> str:
        ...
        
    def set_entry(self, value: str) -> None:
        ...


class ControlPresenter:
    def __init__(self, model: Model, view: ControlView) -> None:
        self.model = model
        self.view = view
        
    def handle_inc_value_b(self, event=None) -> None:
        self.model.value_b = self.model.increment(self.model.value_b, True, self.model.step)
        self.view.set_entry(str(self.model.value_b))
        
    def handle_dec_value_b(self, event=None) -> None:
        self.model.value_b = self.model.increment(self.model.value_b, False, self.model.step)
        self.view.set_entry(str(self.model.value_b))

    def init_ui(self) -> None:
        self.view.init_ui(self)
        self.view.set_entry(str(self.model.value_b))