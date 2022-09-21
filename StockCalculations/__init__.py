import sys


def calculate_return(history):

    def calculate_return(current_closing_price, last_closing_price):

        # calculates the return of a stock 
        return round((current_closing_price - last_closing_price) / (last_closing_price), 4)

    return history[["Open","Close"]].apply(lambda x: calculate_return(x[1],x[0]), axis=1).to_list()

calculate_return.__doc__ = \
"""Calculates the return of a stock.

Given a dataframe with the columns "Open" and "Close", this function calculates the return of a stock.
Args:
    history (dataframe): A dataframe with the columns "Open" and "Close".
Returns:
    A dictionary with the key "return" and the value being a list of the returns of the stock.
"""