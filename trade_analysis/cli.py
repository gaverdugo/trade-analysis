from rich.console import Console
from typing_extensions import Annotated
from typing import Optional
import typer


from trade_analysis.core import TradeFile

console = Console()

def main(
    pathfile: str,
    ticker: Annotated[Optional[str], typer.Option()] = None,
    date: Annotated[Optional[str], typer.Option()] = None
    ):
    '''
    Main function for application, gets total buy and sell volume for each ticker, average stock price per ticket and
    possible discrepancies. If ticker and date are set, also gets trades for that ticker on the set date.

    Parameters:
        pathfile(str): pathfile to csv to be analyzed
        ticker(str [optional, default=None]): ticker to be used for ticker and date search
        date(str [optional, default=None]): date to be used for ticker and date search
    '''
    try:
        if ticker is not None or date is not None:
            if ticker is None:
                console.log('[bold red]Error:[/bold red] Missing value for ticker!')
                raise typer.Exit(1)
            
            if date is None:
                console.log('[bold red]Error:[/bold red] Missing value for date!')
                raise typer.Exit(1)

        trade_file = TradeFile(pathfile)
        table = trade_file.get_buy_sell_volume()
        console.print(table)

        table = trade_file.get_daily_average()
        console.print(table)

        table = trade_file.get_discrepancies()
        console.print(table)

        if ticker is not None and date is not None:
            table = trade_file.get_trades_per_date(ticker, date)
            console.print(table)
    except(FileNotFoundError):
        console.print('[bold red]Error:[/bold red] File not found!')
        raise typer.Exit(1)