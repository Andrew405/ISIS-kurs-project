from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    n: int
    positive: int
    negative: int
    zero: int

    mean: float
    mean_abs: float
    variance: float
    sigma: float
    skewness: float

    shapiro_w: float
    shapiro_p: float

    is_normal: bool

    errors: list[float]