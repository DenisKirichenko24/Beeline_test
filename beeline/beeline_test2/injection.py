import json

import pandas as pd
import requests

# from django.db.models.signals import post_save
# from django.dispatch import receiver

# excel_data_df = pd.read_excel('beeline/beeline_test2/docs/assignment_copy.xlsx',sheet_name='Tables')
# json_str = excel_data_df.to_dict(orient='records')
# response = requests.post("http://localhost:8585/api/v1/tags",json=json_str[0])

# excel_data_df = pd.read_excel('beeline/beeline_test2/docs/assignment_copy.xlsx',sheet_name='Tables', usecols=[2])
# json_str = excel_data_df.to_dict(orient='records')


def post_team():
    excel_data_df = pd.read_excel('beeline/media/docs/assignment.xlsx',sheet_name='Tables')
    excel_data_df.to_csv(r'beeline/media/docs/assignment.csv', index = False, header=True)
    team_data = pd.read_csv("beeline/media/docs/assignment.csv")
    team_json = open('beeline/beeline_test2/team.json')
    json_team = json.load(team_json)
    team = team_data.iloc[0,0]
    json_team["name"] = team
    request = requests.post("http://localhost:8585/api/v1/teams", json=json_team)
    print(request.json())
    return request


def post_db_service():
    excel_data_df = pd.read_excel('beeline/media/docs/assignment.xlsx',sheet_name='Tables')
    excel_data_df.to_csv(r'beeline/media/docs/assignment.csv', index = False, header=True)
    service_data = pd.read_csv('beeline/media/docs/assignment.csv')
    service_json = open('beeline/beeline_test2/servicetype.json')
    json_service = json.load(service_json)
    service = service_data.iloc[0,2]
    json_service["name"] = service   
    request = requests.post("http://localhost:8585/api/v1/services/databaseServices", json=json_service)
    print(request.json())
    return request


def post_database():
    request_service_id = requests.get("http://localhost:8585/api/v1/services/databaseServices/name/Hive-example")
    val = request_service_id.json()
    val_id = val["id"]
    base_json = open('beeline/beeline_test2/base.json')
    json_base = json.load(base_json)
    json_base['service'] = {"id":val_id,"type":"databaseService"}
    request = requests.post("http://localhost:8585/api/v1/databases", json=json_base)
    print(request.json())
    return request


def post_db_schema():
    request_db_id = requests.get("http://localhost:8585/api/v1/databases/name/Hive-example.Hive-db")
    val_bd = request_db_id.json()
    val_bd_id = val_bd["id"]
    schema_json = open('beeline/beeline_test2/schema.json')
    json_schema = json.load(schema_json)
    json_schema["database"] = {"id":val_bd_id, "type": "database"}
    schema = pd.read_excel('beeline/media/docs/assignment.xlsx',sheet_name='Tables')
    schema_name = schema.iloc[0,3]
    json_schema["name"] = schema_name
    request = requests.post("http://localhost:8585/api/v1/databaseSchemas", json=json_schema)
    print(request.json())
    return request


def post_db_table():
    tables_list = pd.read_excel('beeline/media/docs/assignment.xlsx',sheet_name='Fields')
    table = pd.read_excel('beeline/media/docs/assignment.xlsx',sheet_name='Tables')
    tables_columns = tables_list.columns.values
    table_name = table.iloc[0,4]
    table_desc = table.iloc[0,1]
    table_json = open("beeline/beeline_test2/table.json")
    json_tables = json.load(table_json)
    dict_columns = {"name":list(tables_columns), "dataType": "TEXT"}
    json_tables["columns"] = dict_columns
    json_tables["name"] = table_name
    json_tables["description"] = table_desc
    request = requests.post("http://localhost:8585/api/v1/tables", json=json_tables)
    return request


# post_team()
# post_db_service()
# post_database()
# post_db_schema()
# post_db_table()
