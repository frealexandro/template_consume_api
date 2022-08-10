class Param:
    
    def __init__(self):
        
        self.Json = {"json":
                    '{"ds_id":"GA",\
                    "ds_accounts":"116580388,116580388",\
                    "ds_user":"analytics.account@contactica-i.com",\
                    "start_date":"2022-06-30",\
                    "end_date":"2022-07-19",\
                    "fields":"profileID,Date,Campaign,Source,medium,adContent,Goal4Completions",\
                    "settings":{"show_all_time_values":true},\
                    "filter":"Campaign != (not set)",\
                    "max_rows":1000000,\
                    "api_key":"api_OAU570LTP00q8OdUB1Te45PhuNScXwIvvsM5XS5vBB51xvB9CfmLR2mcW6mfiE_djkkmDlPloC8BPso6b_8cwIh2kpvV9OFoV9T"}'}

#


        self.UrlApi ="https://api.supermetrics.com/enterprise/v2/query/data/json?"


        self.Route = 'C:\\Users\\Santiago\\Documents\\GitHub\\Client_Api\\Supermetrics.xlsx'