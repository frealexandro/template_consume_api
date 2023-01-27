# Template_Consume_API
 This template is to consume an API, however, the JSON functionality is currently not working.

# Supermetrics V2

_In this project we consume a supermetrics API and transform it into an excel in order to organize and automate the information_

## Starting 🚀

_To get the project on your local machine, please clone the repository named Client_Api. Note that you must have permission from the organization._


### Pre-requirements 📋

_This project runs on Python, so you must have it installed on your operating system or virtual environment. You must also install the dependencies listed in the 'requirements.txt file'. To install the dependencies, use the following command:_

```
pip install -r requeriments.txt
```

### Facility 🔧


1.Locate the path where the files downloaded from the GitHub repository are located. You will find four python files. To execute the main file, you must first modify the parameters. However, the API consumption already has some default parameters. If you wish to modify them, you can do so in the **params.py** file.


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

2.Set the route where the data in the excel file will be saved. This can also be modified in the **params.py** file.

```
self.Route = 'C:\\Users\\Santiago\\Documents\\GitHub\\Client_Api\\Supermetrics.xlsx'

```

## running the tests ⚙️


_Once the parameters have been set, execute the main.py file. If there is an error with the API consumption, the system will display a message with the error. To execute it from the command prompt on Windows, use the following command:_


```
python main.py

``` 



### Analyze end-to-end tests 🔩


_If the process is executed successfully, the following messages will appear in the command prompt:_

```
'Exportano archivo a un Dataframe'
'Exportando archivo a un Excel'
'Archivo listo'

```

### coding style ⌨️

_This program is completely modularized using object-oriented programming and adheres to the PEP 8 coding style guidelines._



## built with 🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Guia de Parametrizacion
* [OPENPYXL](https://openpyxl.readthedocs.io/en/stable/) - Libreria manipulacion excel
* [PANDAS](https://pandas.pydata.org/) - Libreria manipulacion data
* [REQUEST](https://requests.readthedocs.io/en/latest/) - Libreria consumo API
* [FASTAPI](https://fastapi.tiangolo.com/) - Freamwork API

## Versioning 📌

For all available versions, see the [tags en este repositorio](https://github.com/di-contactica/Client_Api/commits/main).

## Autors ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)

