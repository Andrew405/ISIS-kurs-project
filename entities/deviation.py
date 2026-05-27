from dataclasses import dataclass


@dataclass
class Deviation:
    value: float

    @property
    def abs_value(self) -> float:
        return abs(self.value)

    @property
    def is_positive(self) -> bool:
        return self.value > 0

    @property
    def is_negative(self) -> bool:
        return self.value < 0

    @property
    def is_zero(self) -> bool:
        return self.value == 0