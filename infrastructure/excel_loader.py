import pandas as pd

from entities.measurement import (Measurement)


REQUIRED_COLUMNS = ["id", "nominal", "fact"]


class ExcelLoader:

    @staticmethod
    def load_measurements(file_path: str) -> list[Measurement]:
        excel = pd.ExcelFile(file_path)

        if not excel.sheet_names:
            raise Exception("Excel file has no sheets")

        df = pd.read_excel(file_path)

        for column in REQUIRED_COLUMNS:
            if column not in df.columns:
                raise Exception(
                    f"Required columns: {REQUIRED_COLUMNS}"
                )

        measurements = []

        for _, row in df.iterrows():
            measurements.append(
                Measurement(
                    id=int(row["id"]),
                    nominal=float(row["nominal"]),
                    fact=float(row["fact"])
                )
            )

        return measurements