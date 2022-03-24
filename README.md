# Crypto_Sentiment_Analyzer

-----

## Executive Summary

The goal of this project is to help users understand the trends that are present in the current market so as to make better investment decisions when buying or selling cryptos. We will create a user friendly sentiment analyzer which focuses on Bitcoin and provides users with a bearish or bullish signal on any given day. The application should help users determine what to trade into and/or out of their portfolio.

In this Project, we will create and submit the following deliverables:

- A Jupyter notebook that contains the following:
    1. A time-series analysis on Bitcoin.
    2. Professionally styled and formatted visualizations.
- An interactive Streamlit application that provides users with a forecast for bitcoin.

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
- numpy (a Python library that adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.)
- dotenv (loads environment variables from .env files.)
- matplotlib (a plotting library for the Python programming language.)
- scikit-learn (an open source machine learning library that supports supervised and unsupervised learning.)

-----

##  Installation Guide

- pandas: conda install pandas or pip install pandas
- pathlib: pip install pathlib
- requests: python -m pip install requests
- alpaca-trade-api: pip install alpaca-trade-api
- JSON: conda install -c jmcmurray json
- streamlit: pip install streamlit
- scikit-learn: pip install -U scikit-learn
- dotenv: pip install python-dotenv
- matplotlib: pip install matplotlib
- numpy: pip install numpy

-----

## Usage

The `Crypto_Analyzer.ipynb` notebook will be used to complete the following tasks:

- Use Alpaca APIs to retrieve the data for bitcoin.
- Clean and prepare the data for the analysis and application.
- Do a time-series analysis to make future predictions on the cryptocurrency.
- Provide an accuracy score to determine how likely it is that the predictions will be correct.

The `streamlit.py` application will be used to complete the following tasks:

- Ensure that the user meets the minimum age requirement of 21 years.
- Provide users with a forecast for bitcoin.

-----

## Results

- Our prediction model recieved an accuracy score of 99 percent.

-----

## Streamlit Application

To open the Streamlit application type the following command into your terminal: `streamlit run streamlit.py`

<img width="477" alt="Streamlit_1" src="https://user-images.githubusercontent.com/94569323/160000273-b74d2608-0a27-4430-a7d8-1b36860f66b0.png">

<img width="825" alt="Streamlit_2" src="https://user-images.githubusercontent.com/94569323/160000309-38bf2902-3d37-4f22-9f9b-ade8f1b0c5f7.png">

<img width="757" alt="Streamlit_3" src="https://user-images.githubusercontent.com/94569323/160000342-f4bad437-fd57-45c8-920f-ef6513c1f0b5.png">

<img width="445" alt="Streamlit_4" src="https://user-images.githubusercontent.com/94569323/160000383-b2bb6c9c-d3cc-458f-a258-88d9a2451234.png">

-----

## Future Plans

Future plans for this project include:

- Incorporate a LexBot into the portfolio.
- Incorporate a larger number of cryptocurrencies into the analyzer.

-----

## Contributors

Derek Hall
Patten Williams
Chancie Altham

-----

## License

MIT License