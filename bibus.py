import requests

END_POINT = 'https://applications002.brest-metropole.fr/WIPOD01/Transport/REST'
PAYLOAD_BASE={'format':'json'}
# Static
def get_version():
    payload=PAYLOAD_BASE
    url=END_POINT+'/getVersion'
    r=requests.get(url,params=payload)
    return r.json()

def get_stops_names():
    payload=PAYLOAD_BASE
    url=END_POINT+'/getStopsNames'
    r=requests.get(url,params=payload)
    return r.json()

def get_routes():
    payload=PAYLOAD_BASE
    url=END_POINT+'/getRoutes'
    r=requests.get(url,params=payload)
    return r.json()

def get_stops_route(route_id,trip_headsign):
    payload=PAYLOAD_BASE
    payload['route_id']=route_id
    payload['trip_headsign']=trip_headsign
    url=END_POINT+'/getStops_route'
    r=requests.get(url,params=payload)
    return r.json()

# Dynamic
def get_stops_near(longitude,latitude):
    payload=PAYLOAD_BASE
    payload['longitude']=longitude
    payload['latitude']=latitude
    url=END_POINT+'/getStopsNear'
    r=requests.get(url,params=payload)
    return r.json()

def get_next_departures(route_id,stop_name,trip_headsign):
    payload=PAYLOAD_BASE
    payload['route_id']=route_id
    payload['stop_name']=stop_name
    payload['trip_headsign']=trip_headsign
    url=END_POINT+'/getNextDepartures'
    r=requests.get(url,params=payload)
    return r.json()


