from dataclasses import dataclass
import requests
from pandas import json_normalize
import pandas as pd 
import numpy as np
import json
from Error import*




class Call_Api:

    def __init__(self, params, Url, Path):
        
        self.json = params
        self.base_url = Url
        self.Path = Path

    def Call(self):

        Error = Error_Api()
        Data = Error.Error_Call(self.base_url,self.json)
        Data_Clean = Data.json()
        return Data_Clean
    
    def Norm_Exp(self,Data):

        df = json_normalize(Data,'data')
        df.to_excel (self.Path,header=False,index=False)
