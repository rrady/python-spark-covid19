import requests
import socket
import json

if __name__ == "__main__":
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"format": "json", "code": "ro"}
    headers = {
        'x-rapidapi-host': "",
        'x-rapidapi-key': ""
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    s = socket.socket()
    host = "127.0.0.1"
    port = 5545
    s.bind((host, port))

    print("listening..")

    s.listen(5)
    c, addr = s.accept()

    print("connected: " + str(addr))

    data = json.loads(response.text)
    ro = data[0]
    activeCases = ro.get("confirmed") - ro.get("recovered") - ro.get("deaths")

    print("active cases: " + str(activeCases))

    c.send(str(activeCases).encode('utf-8'))
