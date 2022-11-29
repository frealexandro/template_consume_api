# Template_Consume_API
 This template is to consume Api , but in this moment the json doesn't work
# Supermetrics V2

_In this project we consume a supermetrics API and transform it into an excel in order to organize and automate the information_

## Starting 🚀

_To get the project on your local machine please clone the repository with the name of **Client_Api**, remember that you must have permission from the organization_


### Pre-requirements 📋

_This project runs with the python software once it is installed. You must install the following dependencies in your operating system or virtual environment contained in the file requirements.txt_

```
pip install -r requeriments.txt
```

### Facility 🔧


1.You must look for the path where the files downloaded from the **Git Hub** repository are located, there you will find 4 python files
  to execute the main file, you must first modify the parameters, but in the same way the consumption of the API already brings some
  default parameters if you want to modify them you can modify them you must modify the object inside the **params.py** file


```
 self.Json = {"json": 
                '{"ds_id": "MC",\
                "ds_accounts" :"5bd69150b5_l",\
                "ds_user":"182462257_4140394_us2",\
                "start_date":"2022-04-30",\
                "end_date":"2022-06-19",\
                "fields":"campaign_id, campaign_name, date,clicks_total",\
                "max_rows":1000,\
                "api_key":"api_OAU570LTP00q8ObdUB1Te45PhuNScXwIvvsM5XS5vBB51xvB9CfmLR2mcW6mfiE_djkkmDlPloC8BPso6b_8cwIh2kpv9OFoV9T"}'}

```

2.You must establish the route in which the data contained in the excel file will end, this can also be modified in the file **params.py**

```
self.Route = 'C:\\Users\\Santiago\\Documents\\GitHub\\Client_Api\\Supermetrics.xlsx'

```

## running the tests ⚙️


_Once the parameters have been established, the file **main.py** must be executed in case of an error with the consumption of the API, the system will throw a message with the error presented, to execute it from the console in windows you can use the next command_


```
python main.py

``` 



### Analyze end-to-end tests 🔩


_Si todo el proceso se ejecuta correctamente, te saldran los siguientes los mensajes en la terminal de comandos_

```
'Exportano archivo a un Dataframe'
'Exportando archivo a un Excel'
'Archivo listo'

```

### coding style ⌨️

_This program was completely modularized through object-oriented programming and also attempted to be codified under the **pep 8** regime._



## built with 🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Guia de Parametrizacion
* [OPENPYXL](https://openpyxl.readthedocs.io/en/stable/) - Libreria manipulacion excel
* [PANDAS](https://pandas.pydata.org/) - Libreria manipulacion data
* [REQUEST](https://requests.readthedocs.io/en/latest/) - Libreria consumo API
* [FASTAPI](https://fastapi.tiangolo.com/) - Freamwork API

## Versioning 📌

For all available versions, see the [tags en este repositorio](https://github.com/di-contactica/Client_Api/commits/main).

## Autores ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)


## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
