from dataclasses import dataclass


@dataclass
class Measurement:
    id: int
    nominal: float
    fact: float