# Crypto_Sentiment_Analyzer

-----

## Executive Summary

The goal of this project is to help users make better investment decisions when buying or selling cryptos by studying the trends that are present in the market. We will create a sentiment analyzer which focuses on the top 10 cryptocurrencies and provides users with a bearish or bullish signal for the respective cryptos on any given day. The portfolio should allow users to determine what they should trade in and/or out of their portfolio.

-----

## Technologies

This application is written in Python 3.7 using JupyterLab version 3.0.14.

Import the following libraries:

- pandas (an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.)
- Pathlib (a library that enables consistent input and output of files from the main app.)
- OS (an interface between the Python Programming Language and the Host Operating System.)
- JSON (a lightweight data-interchange format inspired by JavaScript object literal syntax.)
- Requests (an elegant and simple HTTP library for Python, built for human beings.)
- Alpaca Trade API (a python library for the Alpaca Commission Free Trading API. It allows rapid trading algo development easily, with support for both REST and streaming data interfaces.)

-----

##  Installation Guide

- pandas: conda install pandas or pip install pandas
- pathlib: pip install pathlib
- requests: python -m pip install requests
- alpaca-trade-api: pip install alpaca-trade-api
- JSON: conda install -c jmcmurray json

-----

## Usage

The `Crypto_Analyzer.ipynb` notebook will be used to complete the following tasks:

- Use Alpaca APIs to retrieve the current top 10 cryptocurrencies
- Do a time-series analysis to make future predictions on the specific cryptocurrencies
- Create scatter plots to identify seasonal trends and patterns in the data
- Create an Amazon Lex Bot that tells user based off of time-series analysis what the forecast is for each crypto and how much of their portfolio they should buy or sell

-----

## Visualizations

-----

## Results

- 

-----

## Contributors

Derek Hall
Patten Williams
Chancie Altham

-----

## License

MIT License