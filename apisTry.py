import requests

response = requests.get("https://randomuser.me/api/")


txt = response.text
stc = response.status_code
j = response.json()


print(stc)
print(txt)
print(j)






