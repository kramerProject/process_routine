from dataclasses import dataclass
from validate_docbr import CPF
from validate_docbr import CNPJ
from typing import Any

from __utils.exceptions import ValidationException


@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    @staticmethod
    def values(value: Any, prop: str):
        return ValidatorRules(value, prop)

    def required(self) -> 'ValidatorRules':
        if self.value is not None and self.value != '':
            return self

    def string(self) -> 'ValidatorRules':
        if isinstance(self.value, str):
            return self

    def boolean(self) -> 'ValidatorRules':
        return isinstance(self.value, bool)

    def float(self) -> 'ValidatorRules':
        return isinstance(self.value, float)

    def is_cpf_valid(self) -> 'ValidatorRules':
        cpf_validator = CPF()
        return cpf_validator.validate(self.value)

    def is_cnpj_valid(self) -> 'ValidatorRules':
        cnpj_validator = CNPJ()
        return cnpj_validator.validate(self.value)