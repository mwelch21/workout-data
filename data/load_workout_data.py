import pandas as pd
from typing import Optional


class ExcelData:
    """Simple class to warehouse excel interactions"""

    @staticmethod
    def load_dataframe_from_excel_sheet(file_path: str, sheet_name: Optional[str] = None) -> pd.DataFrame:
        data = pd.read_excel(file_path, sheet_name)
        return data

    @staticmethod
    def load_dataframe_from_excel_all(file_path: str) -> pd.DataFrame:
        data = pd.read_excel(file_path)
        return data


if __name__ == '__main__':
    from database.sql_alchemy_manager import BaseEngine
    path = r"/Users/mwelch/Documents/ScrapData/Workout App Scrap.xlsx"
    data = ExcelData.load_dataframe_from_excel_all(file_path=path)

    db_manager = BaseEngine(
        user='postgres',
        password='1321',
        host='127.0.0.1',
        database='workout-dev'
    )
    test = db_manager.get_connection()

    # load data to db
    # data.to_sql('tags', test, if_exists='replace', index=False)

