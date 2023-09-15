import pandas as pd
from rich.table import Table
from typing import Union

def df_to_table(df: pd.DataFrame, table_name: str, empty_message: str = 'No results!') -> Union[str, Table]:
    '''
    Transform Pandas DataFrame to Rich Table for printing on console

    Parameters:
        df(pd.Dataframe): DataFrame to be transformed
        table_name(str): Name of the table
        empty_message(str [optional, default="No results!"]): Message to be displayed when DataFrame is empty

    Returns:
        rich.Table | str: Rich Table for printing or empty message string
    '''

    if len(df) == 0:
        return f'[bold red]{empty_message}[/bold red]'
    
    table = Table(table_name)
    table.add_row(df.to_string(index=False, float_format=lambda _: '{:.2f}'.format(_)))
    return table