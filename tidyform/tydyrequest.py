"""
Collection of functions to put JSON requests into a tidy pandas dataframe structure
"""
import pandas as pd
import json

def tidylist(formList: dict):
    df = pd.DataFrame(columns=['id', 'title', 'last_updated_at','settings','self','theme','_links'])
    num_forms = formList['items']
    for forms in num_forms:
        df1 = pd.DataFrame.from_dict(forms)
        df = df.append(df1)
    return df

def tidyquestions(formQuestions: dict):
    perguntas = formQuestions['fields']
    x = 0
    for pergunta in perguntas:
        if x == 0:
            df = pd.DataFrame.from_dict(pergunta)
        else:
            df1 = pd.DataFrame.from_dict(pergunta)
            df = df.append(df1)
    x = x + 1
    return