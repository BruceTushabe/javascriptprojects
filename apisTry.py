import requests

response = requests.get("https://randomuser.me/api/")


txt = response.text
stc = response.status_code
j = response.json()

m= response.method  

photos = response.json()["photos"]
print(j)
print(photos)






