import json
from pandas.io.json import json_normalize
from itertools import islice
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
class Analysis:
    def callingDeals(deals):
        return (deals)

    def topTenDeals(deals):
        dat=take(2, deals['data'] )
        return (list(dat))

    def openDeal(deals):
        dat=deals['data']
        dat2=[]
        for d in dat:
            if d.get('status') == 'open':
                dat2.append(d)
        return dat2
    
    def closeDeal(deals):
        dat=deals['data']
        dat2=[]
        for d in dat:
            if d.get('status') == 'close':
                dat2.append(d)
        return dat2


    def wonDeal(deals):
        dat=deals['data']
        dat2=[]
        for d in dat:
            if d.get('status') == 'won':
                dat2.append(d)
        return dat2

    def pandasdemo(d):
        deals=d['data']
        deal=json.dumps(deals)
        data=json.loads(deal)
        #print(json_normalize(data))
        df=json_normalize(data)
        
        df['add_time'] = pd.to_datetime(df['add_time'])
        df.index = df['add_time']
        #won deals
        dfa = df.groupby(['status']).get_group('won')
        won_w = dfa['add_time'].resample('W').count().tail(1).get(0)
        #won deal count 
        all_w = df['add_time'].resample('W').count().tail(1).get(0)
        #conversion rate
        print ('Conversion ratio_last week = '+'{:.1%}'.format(won_w/all_w))
        
        #weekly revenue
        won_val=dfa['value'].resample('W').sum()
        print('Revenue: $', won_val)
        
        dfa = df.groupby(['status']).get_group('won')
        monthly_leads = dfa['add_time'].resample('M').count()
        monthly_leads.plot()
        

       # dfa.columns.value_counts()
       # df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
        #return dfa.to_json(orient='records')

    

        

       


    

            

