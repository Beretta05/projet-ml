import pandas as pd

def categorize_bmi(data):
    if isinstance(data,pd.Series):
        return pd.cut(data,bins=[0,18.5,24.9,30,100],labels=['sous-poids','normal','surpoids','obésité'])
    elif isinstance(data,pd.DataFrame):
        return data.apply(pd.cut,args=([0,18.5,24.9,30,100],), axis=0, labels=['sous-poids','normal','surpoids','obésité'])