"""
Source code adapted from: https://medium.datadriveninvestor.com/use-python-to-evaluate-a-stock-investment-7ef09effd426
"""
import requests
from bs4 import BeautifulSoup as bs
import os
from urllib.request import urlopen
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
# Financialmodelingprep api url
base_url = "https://financialmodelingprep.com/api/v3/"
ticker = "FB"

apiKey = os.environ.get("apiKey")

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

# income_statement = pd.DataFrame(get_jsonparsed_data(f"{base_url}income-statement/{ticker}?apikey={apiKey}"))
# income_statement = income_statement.set_index('date')
# income_statement = income_statement.apply(pd.to_numeric, errors='coerce')

# cash_flow_statement = pd.DataFrame(get_jsonparsed_data(f"{base_url}cash-flow-statement/{ticker}?apikey={apiKey}"))
# cash_flow_statement = cash_flow_statement.set_index('date')
# cash_flow_statement = cash_flow_statement.apply(pd.to_numeric, errors='coerce')

# balance_statement = pd.DataFrame(get_jsonparsed_data(f"{base_url}balance-sheet-statement/{ticker}?apikey={apiKey}"))
# balance_statement = balance_statement.set_index('date')
# balance_statement = balance_statement.iloc[::-1].apply(pd.to_numeric, errors='coerce')

# all_statements = pd.merge(income_statement,cash_flow_statement, how='outer', left_index=True, right_index=True)     
# all_statements = pd.merge(all_statements,balance_statement, how='outer', left_index=True, right_index=True)
# all_statements['Receivables-sales-ratio'] = all_statements['netReceivables'] / all_statements['revenue']

# result = all_statements
# result.to_csv("out.csv")

# operatingCashFlow_series = all_statements["operatingCashFlow"]

# Operating Cash Flow Analysis
test_series = {'2017-12-31': 24216000000, '2018-12-31': 29274000000, '2019-12-31': 36314000000, '2020-12-31': 38747000000, '2021-12-31': 57683000000}
test_series = pd.Series(data=test_series, index=['2017-12-31', '2018-12-31', '2019-12-31', '2020-12-31', '2021-12-31'])

ocf_check = dict()
ocf_check_recent = []
ocf_res = ["All Positive", "Positive in the last 3 years", "Negative", "Not enough info"]

# Check how many positives and negatives
for date, value in test_series.items():
    # print(f"Index : {date}, Value : {value}")
    if value > 0:
        ocf_check[date] = 0
    else:
        ocf_check[date] = 1
    # TODO: Add a condition for blank values
ocf_score = ocf_check.values()

# For cases where any value is not positive
if sum(ocf_score) > 0:
    # Check whether the past 3 years are positive
    for i in range(2, (len(test_series))):    
        if test_series[i] > 0:
            ocf_check_recent.append(0)
        else:
            ocf_check_recent.append(1)

    if sum(ocf_check_recent) == 0:
        print(ocf_res[1])

# if all positive
else:
    print(ocf_res[0])


# Net Profit Margin Analysis

# Interest Coverage Analysis

# Final Score

# url_input = f"{URL}{ticker.lower()}"