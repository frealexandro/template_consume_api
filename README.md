# Template_Consume_API
 This template is to consume Api , but in this moment the json doesn't work
# Supermetrics V2

_En este proyecto consumimos una API de supermtrics y los transformamos en un excel con el fin de organizar y automatizar la informacion_

## Comenzando 🚀

_Para obtener el proyecto en tu maquina local porfavor clone el repositorio con el nombre de **Client_Api**, Recuerda que debes tener permiso de la organizacion_


### Pre-requisitos 📋

_Este proyecto se ejecuta con el software python una vez instalado este.Debes instalar las siguientes dependencias en tu sistema opertivo o entorno vrtual contenidas en el archivo requeriments.txt_

```
pip install -r requeriments.txt
```

### Instalación 🔧


1.debes buscar la ruta donde se encuentra los archivos descargados del repositorio de  **Git Hub**, alli encontraras 4 achivos python
  para ejecutar el archivo principal, debes primero modificar los parametros,pero de igual forma el consumo de la API ya trae unos 
  parametros por defecto si deseas modificarlos pudes modificarlos debes modificar el objeto dentro del archivo **params.py**


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

2.debes establecer la ruta en la que va a terminar la data contenida en el el archivo excel ,esta tambien puede ser modificada en el arhivo **params.py**

```
self.Route = 'C:\\Users\\Santiago\\Documents\\GitHub\\Client_Api\\Supermetrics.xlsx'

```

## Ejecutando las pruebas ⚙️


_Una vez establecidos los parametros se debe ejecutar el archivo **main.py** en caso de presentarse un error con el consumo de la API el sistema arrojara un mensaje con el error 
presentado,para ejecutarlo desde la consola en windows se puede usar el siguiente comando_


```
python main.py

``` 



### Analice las pruebas end-to-end 🔩


_Si todo el proceso se ejecuta correctamente, te saldran los siguientes los mensajes en la terminal de comandos_

```
'Exportano archivo a un Dataframe'
'Exportando archivo a un Excel'
'Archivo listo'

```

### estilo de codificación ⌨️

_Este programa se modularizo en su totalidad mediante programcion orientada a objetos y tambien se intento codificar bajo el regimen del **pep 8**_



## Construido con 🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Guia de Parametrizacion
* [OPENPYXL](https://openpyxl.readthedocs.io/en/stable/) - Libreria manipulacion excel
* [PANDAS](https://pandas.pydata.org/) - Libreria manipulacion data
* [REQUEST](https://requests.readthedocs.io/en/latest/) - Libreria consumo API
* [FASTAPI](https://fastapi.tiangolo.com/) - Freamwork API

## Versionado 📌

Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/di-contactica/Client_Api/commits/main).

## Autores ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)

* También puedes mirar la lista de todos los [contribuyentes](https://github.com/orgs/di-contactica/people) quíenes han participado en este proyecto. 


## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢