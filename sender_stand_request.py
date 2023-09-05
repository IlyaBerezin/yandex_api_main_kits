import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body, auth_token):
    user_token = data.headers.copy()
    user_token["Authorization"] = "Bearer " + str(auth_token)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body, headers=user_token)

response = post_new_client_kit(data.kit_body, data.headers);
print(response.status_code)
print(response.json())

#def get_kit_table():
#    return requests.get(configuration.URL_SERVICE + configuration.KIT_TABLE_PATH)