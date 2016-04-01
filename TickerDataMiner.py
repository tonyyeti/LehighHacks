from __future__ import division
import json
import time
import requests
import pandas as pd
import numpy as np

def DataSource(a1,horizon):
    url = 'https://dev.api.thomsonreuters.com/eikon/v1/datagrid?X-TR-API-APP-ID=aQFLyisUVIDAXyl73AlDCMjLOvjhrOeD'
    payload = {
        "instruments": [".SPX"],
        "fields": [
            {"name": "TR.IndexConstituentRIC"},
            {"name": "TR.IndexConstituentName"},
            # {"name": "TR.IndexConstituentSectorName"},
        ],
    }

    headers = {'content-type': 'application/json'}

    jdata = json.dumps(payload)
    req = requests.post(url, jdata.encode('utf-8'))
    a = json.loads(req.text)
    ticker = []
    name = []

    for i in range(0,len(a['data']),1):
        ticker.append(a['data'][i][1])
        name.append(a['data'][i][2])
        # industry.append(a['data'][i][3])

    # industry = []
    # for i in range(0,len(name),1):
    #     payload = {
    #         "instruments": [ticker[i]],
    #         "fields": [
    #             {"name": "TR.TRBCBusinessSector"},
    #             # {"name": "TR.IndexConstituentName"},
    #             # {"name": "TR.IndexConstituentSectorName"},
    #         ],
    #     }
    #
    #     jdata = json.dumps(payload)
    #     req = requests.post(url, jdata.encode('utf-8'))
    #     a = json.loads(req.text)
    #     industry.append(a['data'][0][1])
    # print industry
    industry = [u'Transportation', u'Utilities', u'Industrial & Commercial Services', u'Pharmaceuticals & Medical Research', u'Industrial Goods', u'Real Estate', u'Cyclical Consumer Services', u'Retailers', u'Cyclical Consumer Services', u'Real Estate', u'Banking & Investment Services', u'Technology Equipment', u'Energy - Fossil Fuels', u'Insurance', u'Insurance', u'Retailers', u'Cyclical Consumer Services', u'Industrial & Commercial Services', u'Cyclical Consumer Services', u'Industrial & Commercial Services', u'Cyclical Consumer Products', u'Insurance', u'Chemicals', u'Automobiles & Auto Parts', u'Technology Equipment', u'Real Estate', u'Banking & Investment Services', u'Technology Equipment', u'Technology Equipment', u'Healthcare Services', u'Software & IT Services', u'Technology Equipment', u'Retailers', u'Healthcare Services', u'Retailers', u'Retailers', u'Healthcare Services', u'Food & Drug Retailing', u'Mineral Resources', u'Cyclical Consumer Products', u'Banking & Investment Services', u'Pharmaceuticals & Medical Research', u'Software & IT Services', u'Transportation', u'Cyclical Consumer Services', u'Industrial & Commercial Services', u'Real Estate', u'Personal & Household Products & Services', u'Personal & Household Products & Services', u'Healthcare Services', u'Cyclical Consumer Products', u'Software & IT Services', u'Retailers', u'Software & IT Services', u'Pharmaceuticals & Medical Research', u'Healthcare Services', u'Real Estate', u'Cyclical Consumer Products', u'Retailers', u'Retailers', u'Industrial & Commercial Services', u'Real Estate', u'Insurance', u'Industrial Goods', u'Applied Resources', u'Automobiles & Auto Parts', u'Technology Equipment', u'Energy - Fossil Fuels', u'Industrial Conglomerates', u'Cyclical Consumer Products', u'Industrial & Commercial Services', u'Technology Equipment', u'Retailers', u'Software & IT Services', u'Insurance', u'Technology Equipment', u'Food & Beverages', u'Healthcare Services', u'Utilities', u'Applied Resources', u'Utilities', u'Cyclical Consumer Products', u'Banking & Investment Services', u'Cyclical Consumer Services', u'Energy - Fossil Fuels', u'Banking & Investment Services', u'Cyclical Consumer Services', u'Industrial Goods', u'Industrial & Commercial Services', u'Cyclical Consumer Services', u'Food & Beverages', u'Industrial Goods', u'Real Estate', u'Food & Beverages', u'Transportation', u'Automobiles & Auto Parts', u'Industrial Goods', u'Retailers', u'Pharmaceuticals & Medical Research', u'Healthcare Services', u'Technology Equipment', u'Retailers', u'Technology Equipment', u'Energy - Fossil Fuels', u'Technology Equipment', u'Chemicals', u'Chemicals', u'Retailers', u'Industrial Goods', u'Real Estate', u'Utilities', u'Energy - Fossil Fuels', u'Energy - Fossil Fuels', u'Cyclical Consumer Services', u'Pharmaceuticals & Medical Research', u'Food & Drug Retailing', u'Transportation', u'Food & Beverages', u'Energy - Fossil Fuels', u'Healthcare Services', u'Energy - Fossil Fuels', u'Cyclical Consumer Services', u'Cyclical Consumer Services', u'Banking & Investment Services', u'Pharmaceuticals & Medical Research', u'Food & Drug Retailing', u'Chemicals', u'Industrial Goods', u'Energy - Fossil Fuels', u'Software & IT Services', u'Banking & Investment Services', u'Technology Equipment', u'Insurance', u'Cyclical Consumer Services', u'Industrial Goods', u'Pharmaceuticals & Medical Research', u'Real Estate', u'Telecommunications Services', u'Banking & Investment Services', u'Software & IT Services', u'Software & IT Services', u'Real Estate', u'Cyclical Consumer Products', u'Technology Equipment', u'Real Estate', u'Cyclical Consumer Services', u'Real Estate', u'Retailers', u'Pharmaceuticals & Medical Research', u'Banking & Investment Services', u'Utilities', u'Healthcare Services', u'Automobiles & Auto Parts', u'Software & IT Services', u'Chemicals', u'Software & IT Services', u'Automobiles & Auto Parts', u'Pharmaceuticals & Medical Research', u'Healthcare Services', u'Healthcare Services', u'Energy - Fossil Fuels', u'Cyclical Consumer Services', u'Banking & Investment Services', u'Food & Drug Retailing', u'Industrial Goods', u'Transportation', u'Software & IT Services', u'Mineral Resources', u'Investment Holding Companies', u'Healthcare Services', u'Healthcare Services', u'Healthcare Services', u'Pharmaceuticals & Medical Research', u'Retailers', u'Banking & Investment Services', u'Industrial Goods', u'Utilities', u'Food & Beverages', u'Pharmaceuticals & Medical Research', u'Industrial Goods', u'Food & Beverages', u'Insurance', u'Energy - Fossil Fuels', u'Utilities', u'Technology Equipment', u'Insurance', u'Industrial & Commercial Services', u'Real Estate', u'Industrial Conglomerates', u'Utilities', u'Energy - Fossil Fuels', u'Technology Equipment', u'Energy - Fossil Fuels', u'Banking & Investment Services', u'Utilities', u'Insurance', u'Retailers', u'Chemicals', u'Utilities', u'Utilities', u'Chemicals', u'Healthcare Services', u'Technology Equipment', u'Industrial Goods', u'Technology Equipment', u'Mineral Resources', u'Industrial & Commercial Services', u'Utilities', u'Food & Drug Retailing', u'Food & Beverages', u'Industrial Goods', u'Healthcare Services', u'Utilities', u'Software & IT Services', u'Energy - Fossil Fuels', u'Industrial & Commercial Services', u'Healthcare Services', u'Retailers', u'Utilities', u'Pharmaceuticals & Medical Research', u'Industrial & Commercial Services', u'Banking & Investment Services', u'Healthcare Services', u'Technology Equipment', u'Energy - Fossil Fuels', u'Industrial Goods', u'Cyclical Consumer Services', u'Industrial Goods', u'Technology Equipment', u'Banking & Investment Services', u'Energy - Fossil Fuels', u'Food & Beverages', u'Chemicals', u'Healthcare Services', u'Industrial Goods', u'Technology Equipment', u'Banking & Investment Services', u'Personal & Household Products & Services', u'Industrial Goods', u'Renewable Energy', u'Banking & Investment Services', u'Transportation', u'Banking & Investment Services', u'Real Estate', u'Mineral Resources', u'Healthcare Services', u'Insurance', u'Technology Equipment', u'Cyclical Consumer Services', u'Cyclical Consumer Products', u'Banking & Investment Services', u'Food & Beverages', u'Personal & Household Products & Services', u'Industrial & Commercial Services', u'Technology Equipment', u'Industrial & Commercial Services', u'Insurance', u'Energy - Fossil Fuels', u'Utilities', u'Industrial & Commercial Services', u'Utilities', u'Energy - Fossil Fuels', u'Industrial & Commercial Services', u'Energy - Fossil Fuels', u'Food & Drug Retailing', u'Software & IT Services', u'Food & Beverages', u'Food & Beverages', u'Banking & Investment Services', u'Retailers', u'Pharmaceuticals & Medical Research', u'Real Estate', u'Energy - Fossil Fuels', u'Retailers', u'Healthcare Services', u'Energy - Fossil Fuels', u'Real Estate', u'Insurance', u'Industrial & Commercial Services', u'Healthcare Services', u'Cyclical Consumer Products', u'Utilities', u'Food & Beverages', u'Insurance', u'Energy - Fossil Fuels', u'Industrial Goods', u'Food & Beverages', u'Software & IT Services', u'Automobiles & Auto Parts', u'Real Estate', u'Industrial Goods', u'Banking & Investment Services', u'Industrial Goods', u'Energy - Fossil Fuels', u'Banking & Investment Services', u'Cyclical Consumer Products', u'Industrial Goods', u'Banking & Investment Services', u'Insurance', u'Cyclical Consumer Services', u'Real Estate', u'Cyclical Consumer Services', u'Cyclical Consumer Services', u'Automobiles & Auto Parts', u'Energy - Fossil Fuels', u'Banking & Investment Services', u'Software & IT Services', u'Insurance', u'Industrial Goods', u'Retailers', u'Transportation', u'Banking & Investment Services', u'Utilities', u'Food & Beverages', u'Chemicals', u'Telecommunications Services', u'Cyclical Consumer Services', u'Healthcare Services', u'Real Estate', u'Retailers', u'Technology Equipment', u'Personal & Household Products & Services', u'Banking & Investment Services', u'Technology Equipment', u'Chemicals', u'Transportation', u'Applied Resources', u'Utilities', u'Banking & Investment Services', u'Telecommunications Services', u'Mineral Resources', u'Banking & Investment Services', u'Food & Beverages', u'Cyclical Consumer Services', u'Pharmaceuticals & Medical Research', u'Utilities', u'Cyclical Consumer Services', u'Cyclical Consumer Services', u'Technology Equipment', u'Transportation', u'Industrial Conglomerates', u'Transportation', u'Banking & Investment Services', u'Cyclical Consumer Services', u'Banking & Investment Services', u'Retailers', u'Applied Resources', u'Utilities', u'Energy - Fossil Fuels', u'Healthcare Services', u'Industrial Conglomerates', u'Software & IT Services', u'Utilities', u'Industrial & Commercial Services', u'Real Estate', u'Personal & Household Products & Services', u'Software & IT Services', u'Utilities', u'Pharmaceuticals & Medical Research', u'Software & IT Services', u'Software & IT Services', u'Real Estate', u'Healthcare Services', u'Banking & Investment Services', u'Insurance', u'Industrial & Commercial Services', u'Software & IT Services', u'Real Estate', u'Software & IT Services', u'Food & Beverages', u'Healthcare Services', u'Banking & Investment Services', u'Healthcare Services', u'Retailers', u'Insurance', u'Technology Equipment', u'Pharmaceuticals & Medical Research', u'Cyclical Consumer Services', u'Transportation', u'Chemicals', u'Energy - Fossil Fuels', u'Energy - Fossil Fuels', u'Cyclical Consumer Services', u'Retailers', u'Food & Beverages', u'Mineral Resources', u'Pharmaceuticals & Medical Research', u'Healthcare Services', u'Retailers', u'Industrial Goods', u'Energy - Fossil Fuels', u'Insurance', u'Pharmaceuticals & Medical Research', u'Technology Equipment', u'Automobiles & Auto Parts', u'Cyclical Consumer Products', u'Technology Equipment', u'Industrial Goods', u'Personal & Household Products & Services', u'Pharmaceuticals & Medical Research', u'Insurance', u'Food & Beverages', u'Banking & Investment Services', u'Technology Equipment', u'Healthcare Services', u'Industrial Conglomerates', u'Retailers', u'Banking & Investment Services', u'Retailers', u'Automobiles & Auto Parts', u'Energy - Fossil Fuels', u'Insurance', u'Banking & Investment Services', u'Cyclical Consumer Services', u'Banking & Investment Services', u'Personal & Household Products & Services', u'Technology Equipment', u'Personal & Household Products & Services', u'Real Estate', u'Cyclical Consumer Products', u'Industrial & Commercial Services', u'Software & IT Services', u'Software & IT Services', u'Applied Resources', u'Cyclical Consumer Products', u'Industrial Goods', u'Food & Beverages', u'Energy - Fossil Fuels', u'Software & IT Services', u'Transportation', u'Energy - Fossil Fuels', u'Transportation', u'Retailers', u'Insurance', u'Retailers', u'Energy - Fossil Fuels', u'Banking & Investment Services', u'Insurance', u'Software & IT Services', u'Retailers', u'Food & Drug Retailing', u'Cyclical Consumer Services', u'Food & Beverages', u'Pharmaceuticals & Medical Research', u'Food & Drug Retailing', u'Industrial & Commercial Services', u'Energy - Fossil Fuels', u'Industrial Goods', u'Food & Beverages', u'Food & Beverages', u'Technology Equipment', u'Food & Drug Retailing', u'Real Estate', u'Cyclical Consumer Services', u'Cyclical Consumer Services', u'Technology Equipment', u'Software & IT Services', u'Cyclical Consumer Services', u'Software & IT Services', u'Utilities', u'Utilities', u'Energy - Fossil Fuels', u'Banking & Investment Services', u'Cyclical Consumer Products', u'Food & Beverages', u'Pharmaceuticals & Medical Research', u'Industrial & Commercial Services', u'Cyclical Consumer Services', u'Technology Equipment', u'Utilities', u'Real Estate', u'Real Estate', u'Banking & Investment Services', u'Transportation', u'Retailers', u'Industrial Goods', u'Cyclical Consumer Products', u'Food & Beverages', u'Utilities', u'Utilities', u'Banking & Investment Services', u'Cyclical Consumer Products', u'Industrial Goods', u'Energy - Fossil Fuels', u'Insurance', u'Insurance', u'Industrial & Commercial Services', u'Food & Beverages', u'Industrial Goods', u'Cyclical Consumer Products', u'Utilities', u'Real Estate', u'Software & IT Services', u'Energy - Fossil Fuels', u'Energy - Fossil Fuels', u'Telecommunications Services', u'Utilities', u'Industrial Goods', u'Energy - Fossil Fuels', u'Technology Equipment', u'Banking & Investment Services', u'Telecommunications Services', u'Industrial & Commercial Services', u'Industrial & Commercial Services']
    industries = set(industry)

    a = np.array([name, industry, ticker]).T
    info = pd.DataFrame( a, columns=['name','industry','ticker'])


    indu = []
    indstock = []
    for i in range(0,len(a1),1):
         indu.append(industry[a1[i]])
    for i in range(0,len(name),1):
        if info['industry'][i] in indu:
            indstock.append(info['ticker'][i])

    tick = indstock
    k = int(len(indstock)/30)
    x = []
    for i in range(0,k+1,1):
        a = tick[30*i:30*(i+1)]
        x.append(a)
    if horizon == 1:

        ### Gather Longterm and Shortterm data
        url = 'https://dev.api.thomsonreuters.com/eikon/v1/timeseries?X-TR-API-APP-ID=aQFLyisUVIDAXyl73AlDCMjLOvjhrOeD'
        longterm = []
        for i in range(0,len(x),1):
            payload = {
                "rics": x[i],
                "interval": "monthly",
                "startdate": "2011-04-01T00:00:00Z",
                "enddate": "2016-03-31T23:59:59Z",
                "fields":
               ["TIMESTAMP","CLOSE"]
            }

            jdata = json.dumps(payload)
            req = requests.post(url, jdata.encode('utf-8'))
            a = json.loads(req.text)
            for i in range(0,len(x[i]),1):
                b = pd.DataFrame(a['timeseriesData'][i]['dataPoints'],columns = ['date','price'])['price'].values

                longterm.append(b)
        # print longterm
        LTreturnmatrix = []
        for i in range(0, len(longterm), 1):
            stockreturn = []
            for k in range(0, len(longterm[i]) - 1, 1):
                a = longterm[i][k + 1]
                b = longterm[i][k]
                stockreturn.append(np.log(a / b))
            LTreturnmatrix.append(stockreturn)
        return indstock, longterm, LTreturnmatrix

    elif horizon == 0:
        shortterm = []
        for i in range(0,len(x),1):
            payload = {
                "rics": x[i],
                "interval": "daily",
                "startdate": "2016-01-01T00:00:00Z",
                "enddate": "2016-03-31T23:59:59Z",
                "fields":
               ["TIMESTAMP","CLOSE"]
            }

            jdata = json.dumps(payload)
            req = requests.post(url, jdata.encode('utf-8'))
            a = json.loads(req.text)
            for i in range(0,len(x[i]),1):
                b = pd.DataFrame(a['timeseriesData'][i]['dataPoints'],columns = ['date','price'])['price'].values
                shortterm.append(b)
        # # print shortterm
        STreturnmatrix = []
        for i in range(0, len(shortterm), 1):
            stockreturn = []
            for k in range(0, len(shortterm[i]) - 1, 1):
                a = shortterm[i][k + 1]
                b = shortterm[i][k]
                stockreturn.append(np.log(a / b))
            STreturnmatrix.append(stockreturn)
        return indstock, shortterm, STreturnmatrix

a1 = [1]
horizon = 1

stock_list = DataSource(a1, horizon)[0]
price_raw = DataSource(a1, horizon)[1]
returns = DataSource(a1, horizon)[2]


print returns, price_raw, stock_list
