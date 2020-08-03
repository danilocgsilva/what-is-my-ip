import json, requests


class Wimi:

    def __init__(self):
        self.url_to_fetch_ip = 'https://api.ipify.org?format=json'
        self.url_to_fetch_ipv6 = 'https://api6.ipify.org?format=json'

    def get_ip(self, ipvtype):

        if ipvtype == 'ipv4':
            data_response = requests.get(self.url_to_fetch_ip)
        elif ipvtype == 'ipv6':
            data_response = requests.get(self.url_to_fetch_ipv6)

        jsondata = data_response.json()
        return jsondata["ip"]
