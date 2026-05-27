from scipy.stats import shapiro


class NormalityService:

    @staticmethod
    def check_normality(errors: list[float]) -> dict:
        statistic, p_value = shapiro(errors)

        return {
            "shapiro_w": float(statistic),
            "shapiro_p": float(p_value),
            "is_normal": p_value > 0.05
        }