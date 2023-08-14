from dataclasses import dataclass


@dataclass
class Model:
    _value_a: str = 'Value "A" in the Model' 
    _value_b: float = 0.0
    _step: float = 1.0
    
    def increment(self, value: float, increase: bool, step: float) -> float:
        sign = 1 if increase else -1
        return value + (sign *step)
    
    # GETTER AND SETTERS
    @property
    def value_a(self) -> str:
        return self._value_a 
    
    @value_a.setter
    def value_a(self, new_value_a: str) -> None:
        self._value_a = new_value_a
        
    @property
    def value_b(self) -> float:
        return self._value_b 
    
    @value_b.setter
    def value_b(self, new_value_b: float) -> None:
        self._value_b = new_value_b
        
    @property
    def step(self) -> float:
        return self._step 
    
    @step.setter
    def step(self, new_step: int) -> None:
        self._vstep = new_step