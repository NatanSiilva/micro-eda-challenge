from typing import Any
from dataclasses import dataclass

from src.application.shared.exception import ValidationException


@dataclass(frozen=True)
class ValidatorRoles:
    value: Any
    prop: str


    @staticmethod
    def values(value: Any, prop: str):
        return ValidatorRoles(value, prop)
    

    def required(self) -> 'ValidatorRoles':
        if self.value is None or self.value == '':
            raise ValidationException(f"The {self.prop} is required")
        return self

    
    def string(self) -> 'ValidatorRoles':
        if self.value is not None and not isinstance(self.value, str):
            raise ValidationException(f"The {self.prop} must be a string")
        return self
    
    
    def integer(self) -> 'ValidatorRoles':
        if self.value is not None and not isinstance(self.value, int):
            raise ValidationException(f"The {self.prop} must be an integer")
        return self


    def max_length(self, max_length: int) -> 'ValidatorRoles':
        if self.value is not None and len(self.value) > max_length:
            raise ValidationException(f"The {self.prop} must be less than {max_length} characters")
                
        return self 


    def boolean(self) -> 'ValidatorRoles':
        if self.value is not None and self.value is not True and self.value is not False:
            raise ValidationException(f"The {self.prop} must be a boolean")
        return self

