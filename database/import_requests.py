import requests
import pandas as pd

def dados_requests():
    url = "https://labdados.com/produtos"
    response = requests.get(url)
    dados = pd.DataFrame.from_dict(response.json())
    
    return dados    