import numpy as np

from scipy.stats import skew

from entities.measurement import Measurement


class StatisticsService:

    @staticmethod
    def calculate_errors(
        measurements: list[Measurement]
    ) -> list[float]:
        return [
            measurement.fact - measurement.nominal
            for measurement in measurements
        ]

    @staticmethod
    def calculate_statistics(errors: list[float]) -> dict:
        errors_np = np.array(errors)

        positive = sum(1 for error in errors if error > 0)
        negative = sum(1 for error in errors if error < 0)
        zero = sum(1 for error in errors if error == 0)

        return {
            "n": len(errors),
            "positive": positive,
            "negative": negative,
            "zero": zero,
            "mean": float(np.mean(errors_np)),
            "mean_abs": float(np.mean(np.abs(errors_np))),
            "variance": float(np.var(errors_np)),
            "sigma": float(np.std(errors_np)),
            "skewness": float(skew(errors_np)),
            "errors": errors
        }