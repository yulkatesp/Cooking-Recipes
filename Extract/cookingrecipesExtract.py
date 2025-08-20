import requests
url = "https://ipinfo.io/190.60.194.114/json" #Se cambia la dirección IP dependiendo de la que se quiera ver 
try:
    response= requests.get(url)
    data= response.json()
    print(data)

except:
    print("Hubo un error")
