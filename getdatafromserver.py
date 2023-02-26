import requests


def read_data():
    url_get = 'http://jarwall.com/v/aja/sngpl_get/ajkER8ERNFNJmxngnxcgiuNSJFDGGORTFEser888er&tbs=u273'

    response = requests.get(url_get)
    print(response)
    data = response.text
    print(data)
    pres = data[34:39]
    time = data[90:109]
    return (pres, time)


def write_data(pres_val):
    url_hard = 'http://jarwall.com/v/aja/sngpl_hard/ajkER8ERNFNJmxngnxcgiuNSJFDGGORTFEser888er&tbs=u273&press=' \
               + str(pres_val)

    response = requests.get(url_hard)
    print(response)
