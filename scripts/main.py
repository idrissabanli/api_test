import requests

# # response = requests.get('https://api.github.com/users/idrissabanli')
# response = requests.get('https://google.com')

# # response_json = response.json()
# content = response.content

# # print(content)

# with open('google.html', 'wb') as f:
#     f.write(content)

post_valid_data = {
    "title": "Blog 2",
    "short_description": "Blog description 2",
    "content": "Blog content 2",
    "blogger_full_name": "Blogger 2"
}

response_valid_data = requests.post("http://35.225.243.133/blogs/", data=post_valid_data)

res_valid_data_json = response_valid_data.json()

print(res_valid_data_json)
print('yaradilan melumatin id=', res_valid_data_json["id"])
print('yaradilan melumatin basligi=', res_valid_data_json["title"])
print('yaradilan melumatin aciqlamasi=', res_valid_data_json["short_description"])