# Trade Analysis Challenge

## Dependency installation

This project uses [Poetry](https://python-poetry.org/) for dependency management and virtual environment management. To install dependencies, simply execute

`poetry install`

Afterwards to enter the projects virtual environment, execute

`poetry shell`

There is also a *requirements.txt* file if you prefer to use pip

`pip install -r requirements.txt`

## Usage

To analyze a csv, execute

`python -m trade_analysis <path/to/csv>`

If you want to search for ticker and date, execute

`python -m trade_analysis <path/to/csv> --date <YYYY-MM-DD> --ticker <ticker>`

## Brief explanation of each solution

### Calculate the total buy and sell volume for each ticker

Use pandas to group the dataframe by ticker and trade type, obtain the sum of quantity per those two values and create two columns
"buy_volume" and "sell_volume" with the sum of all the quantities on columns where trade_type is equal to "BUY" and "SELL" respectively.
Columns of "BUY" trades will have "sell_volume" as NaN and vice versa. Fill the NaN values with zeroes. Group the dataframe by 
ticker and obtain the max value for buy_volume and sell_volume. This way, if the ticker has any buy or sell volume, the maximum value
will be the total sum, otherwise it will be zero.

### Identify customers with more than 3 trades in the same day

Use pandas to group the dataframe by customer id and trade date, count the trade id's and assign the value to a new column "daily_trades".
Filter the dataframe to rows where daily_trades is greater than 3, select only the Customer ID's column and drop duplicates to obtain unique Customer ID's.

### Calculate the average price for each ticker on days it was traded

Use Pandas to group the dataframe by ticker value and get the average of prices.

### Given a ticker and a date, return list of trades for that ticker on the provided date

Use Pandas to filter the dataframe where the columns ticker and date are equal to the values provided. 