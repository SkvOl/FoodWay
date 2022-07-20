import requests
import json
import polyline

def get_route(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon):
    loc = "{},{};{},{}".format(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc) 
    if r.status_code!= 200:
        return []
    res = r.json()   
    routes = polyline.decode(res['routes'][0]['geometry'])

    return routes

def route(request, item):
    # пример item содержащего координаты 3 точек на карте
    #item = {
    #            '0' : [53.19799, 45.00664, 53.18288, 45.00131],#lat1,long1,lat2,long2
    #            '1' : [53.18288, 45.00131, 53.19193, 45.16496],
    #       }

    out = []
    for i in range(len(item)):
        item[i][0], item[i][1], item[i][2], item[i][3] = float(item[i][0]), float(item[i][1]), float(item[i][2]), float(item[i][3])
        out += get_route(item[i][0], item[i][1], item[i][2], item[i][3])
        

    return out
