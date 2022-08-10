from urllib.error import HTTPError
from Call_Api import*
import requests





class Error_Api:

    def __init__(self):
        

        self.HTTPError = "Hay un Error con la repuesta del HTTPError"
        self.Conection = "Porfavor conectate a una red"
        self.Timeout = "Tiempo de respuesta agotado porfavor intenta otra vez"
        self.request_E = "Hay un problema con el request"
        

    def Error_Call(self,base_url,json):
        
        try:
            response = requests.get(url= base_url,params= json)


            
        except requests.exceptions.HTTPError as errh:
            HTTPError = errh
            print(self.HTTPError)
        except requests.exceptions.ConnectionError as errc:
            ConnectionError = errc
            print(self.Conection)
        except requests.exceptions.Timeout as errt:
            TimeoutError = errt
            print(self.Timeout)
        except requests.exceptions.RequestException as err:
            requests_E = err
            print(self.request_E)
        
        return response