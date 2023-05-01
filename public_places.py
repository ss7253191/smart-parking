# Python program to get a set of
# places according to your search
# query using Google Places API

# importing required modules
import requests
import json

# enter your api key here
# api_key = '1fdef5a56f0221712cd38e8531db03a8'

# url variable store url

auth_url = "https://outpost.mapmyindia.com/api/security/oauth/token?grant_type=client_credentials&client_id=33OkryzDZsJ1EBQ_x46Ui_xN_j50SpUAykKisy_URbs2NQ1ZFsbOK9fmgyUu45NUni3kSnDu_29FmI7ZISkM_0MvJ0loAvWo&client_secret=lrFxI-iSEg9k9OYupUwDoDlAhi5JI4PF0nX5wyXURqKXWrjHG3O1n_1rw7l_Ug-gnCB4AoZ1oZbYzTwVlY1TmcLUxlS6kgKLJqjt-73pX_w="
auth = requests.post(auth_url)
# print(auth)
tokens=auth.json()
# print(type(tokens))
# Serializing json
json_object = json.dumps(tokens, indent =4 )

# Writing to sample.json
with open("authorization.json", "w") as outfile:
    outfile.write(json_object)
# print(tokens)

token_types=(tokens["token_type"])
# print(token_types)
access_token=(tokens["access_token"])
# print(access_token)
keyVal= f"{token_types} {access_token}"
headers = {"Authorization" : keyVal}
# print(headers)

query = input('Search query: ')

url = f"https://atlas.mapmyindia.com/api/places/nearby/json?keywords={query}&refLocation=22.6812,75.8798&itemCount=10"


# # # get method of requests module
# # # return response object
r = requests.get(url,headers=headers)
res=r.json()
# print(re  s)

response_json = json.dumps(res, indent =4 )

# Writing to sample.json
with open("templates/petrol_pump.json", "w") as outfile:
    outfile.write(response_json)
# # # json method of response object convert
# # # json format data into python format data
# # x = r.json()
# # print(x)
# # # now x contains list of nested dictionaries
# # # we know dictionary contain key value pair
# # # store the value of result key in variable y
# # y = x['results']
# # # print (y)
# # # keep looping upto length of y
# # for i in range(len(y)):

# # 	# Print value corresponding to the
# # 	# 'name' key at the ith index of y
# # 	print(y[i]['name'])
