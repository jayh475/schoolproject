import http.client, urllib.parse, json

stations = {}
key = {'Ocp-Apim-Subscription-Key': '1b540df20b07441da700ea735d59d6fe'}

plaatsnaam = input('voer een station in:')
stations['station'] = plaatsnaam
params = urllib.parse.urlencode(stations)

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    payloadObject = data['payload']
    departuresList = payloadObject['departures']

    for departure in departuresList:
        print(departure['actualDateTime'], departure['direction'])

    conn.close()


except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))


