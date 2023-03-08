# portfolio-recommendation-engine
Build and track portfolio based on user inputs

## Problem statement
Build portfolio recommendation application that will be used to propose portfolios (for example -using subset of instruments within SP500 Index) for investment to clients based on their preference.

## Resources
Sharpe Ratio – Portfolio variance, growth
https://towardsdatascience.com/calculating-sharpe-ratio-with-python-755dcb346805

## Sample sources to fetch market data
+ https://datahub.io/core/s-and-p-500
+ https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs
+ https://data.nasdaq.com/

## Ask
+ Users will input portfolio preferences (e.g. Market Capitalization, Investment Sector, Volatility) while computing portfolio composition. 
+ User preferences and portfolios proposed by the tool should be stored for future analysis. 
+ Portfolio re-composition based on pre-defined triggers (e.g. change in a constituent’s volatility by 5%) or by the user should be allowed.
+ Recommend portfolio should consist of 20-30 stocks

## Assumptions 
+ Indices other than SP500 can also be used
+ Market data for calculations can be obtained from publicly available resources 
+ Soft real-time performance is expected
+ Limit to 5 years of timeframe for back-testing
+ Sharpe ratio can be used to compare portfolio performances against benchmark portfolio.
+ Customer can provide below preferences to the tool
+ Investment sector (e.g. Technology, Energy, Financial)
+ Market Capitalization (e.g. Large / Mid / Small cap)
+ Portfolio Rate of return / Volatility



