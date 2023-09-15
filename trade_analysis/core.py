import pandas as pd
from rich.table import Table

from trade_analysis import utils

class TradeFile:
    def __init__(self, filepath):
        self.trade_df = pd.read_csv(filepath)

    def get_buy_sell_volume(self) -> Table:
        '''
            Calculate the total buy and sell volume for each ticker

            Returns:
                rich.Table: table with ticker, buy and sell volume
        '''

        # We create a copy to not affect the object's dataframe
        trade_df = self.trade_df.copy()
        grouped_df = trade_df.groupby(['ticker', 'trade_type'], as_index=False)['quantity']
        trade_df['buy_volume'] = grouped_df.transform('sum').where(trade_df['trade_type'] == 'BUY')
        trade_df['sell_volume'] = grouped_df.transform('sum').where(trade_df['trade_type'] == 'SELL')
        trade_df = trade_df[['ticker', 'buy_volume', 'sell_volume']].fillna(0)
        volume_df = trade_df.groupby(['ticker'], as_index=False)[['buy_volume', 'sell_volume']].max()
        volume_df.columns = ['Ticker', 'Buy Volume', 'Sell Volume']

        return utils.df_to_table(volume_df, 'Total buy and sell volume per ticker')

    def get_discrepancies(self) -> Table:
        '''
            Identify customers with more than 3 trades in the same day

            Returns:
                rich.Table | str: table with identified customers or empty message
        '''

        # We create a copy to not affect the object's dataframe
        trade_df = self.trade_df.copy()
        trade_df['daily_trades'] = trade_df.groupby(['trade_date', 'customer_id'], as_index=False)['trade_id'].transform('count')
        discrepancies_df = trade_df[trade_df['daily_trades'] > 3]
        discrepancies_df = discrepancies_df['customer_id'].drop_duplicates()
        return utils.df_to_table(discrepancies_df, 'Customers with possible discrepancies', empty_message='No customers with possible discrepancies found!')

    def get_daily_average(self) -> Table:
        '''
            Calculate the average price for each ticker on days it was traded

            Returns:
                rich.Table: table with 
        '''

        trade_df = self.trade_df
        means_df = trade_df.groupby(['ticker'], as_index=False)['price'].mean()
        means_df.columns = ['Ticker', 'Average price']

        return utils.df_to_table(means_df, 'Average ticker price on traded days')

    def get_trades_per_date(self, ticker: str, date: str) -> Table:
        '''
            Given a ticker and a date, return list of trades for that ticker on the provided date

            Parameters:
                ticker(str): ticker to search
                date(str): date to search in YYYY-MM-DD format

            Returns:
                rich.Table | str: table with results or empty message
        '''

        trade_df = self.trade_df
        filtered_df = trade_df.loc[(trade_df['ticker'] == ticker) & (trade_df['trade_date'] == date)]
        filtered_df = filtered_df[['trade_id', 'customer_id', 'trade_type', 'quantity', 'price']]
        filtered_df.columns = ['ID', 'Customer ID', 'Trade type','Quantity', 'Price']

        return utils.df_to_table(filtered_df, f'Trades for ticker {ticker} on date {date}', empty_message=f'No trades for {ticker} on date {date} found!')