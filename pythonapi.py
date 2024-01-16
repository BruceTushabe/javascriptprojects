import requests
response = requests.get("https://api.thecatapi.com/v1/breeds")
y = response.text

x = response.status_code

z = response.headers

print(y)

print(x)

print(z)
