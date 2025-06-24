import re
from dataclasses import dataclass

@dataclass(frozen=True)
class CPF:
    value: str
    
    def __post_init__(self):
        if not self._is_valid_cpf(self.value):
            raise ValueError(f"CPF inválido: {self.value}")
        self.value = ''.join(re.findall(r'\d', self.value)); 
    
    def _is_valid_cpf(self, cpf: str) -> bool:
        pattern = r'^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$'
        return re.match(pattern, cpf) is not None
    
    def __str__(self) -> str:
        return self.value
    
    def get_CpfWithMask(self) -> str:
        return re.sub(r'^(\d{3})(\d{3})(\d{3})(\d{2})$', r'\1.\2.\3-\4', self.value)
    
        