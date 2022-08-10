import pandas as pd 
import numpy as np
import json
from pandas import json_normalize 
from Call_Api import*
from Error import*
from Params import*

def run():
    
    Params = Param()
    Params = Params.Json

    Url = Param()
    Url = Url.UrlApi
    
    My_Path = Param()
    My_Path = My_Path.Route

    Response = Call_Api(Params,Url,My_Path)
    Data = Response.Call()
    

    print('Exportano archivo a un Dataframe')
    Response.Norm_Exp(Data)
    print('Exportando archivo a un Excel')
    print('Archivo listo')

if __name__ == '__main__':
     run()