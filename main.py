import uvicorn
import logging
import json

import nest_asyncio
import azure.functions as func
import yfinance as yf
from pydantic import BaseModel

from StockCalculations import calculate_return
from FastAPIApp import app

# nest_asyncio.apply()


# TODO: Create Pydantic models for the request and response, 
#       this will help with validation and documentation.
# TODO: Authenticate the request
# TODO: Add logging



class User(BaseModel):
    ticker: str
    company_return: list



@app.get("/companyreturn/{ticker}")
async def get_company_info(ticker: str):

    # TODO: Validate the ticker

    # get company info from yfinance
    company = yf.Ticker(ticker.upper())

    # get company info
    hist = company.history(period="max", interval='1wk')["2015-01-01":]
    hist = hist.dropna()
    # calculate return
    company_return = calculate_return(hist)

    return {"ticker": ticker, "company_return": company_return}


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)


if __name__ == "__main__":
    logging.info("Starting server")
    uvicorn.run(app, host="0.0.0.0", port=5000)