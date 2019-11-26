from math import sin, cos, sqrt, atan2, radians
import numpy as np
from typing import List
import requests
import json
import pandas as pd

def distance_np(dest_lat: np.ndarray,
                dest_lng: np.ndarray,
                orig_lat: np.ndarray = np.array([51.509865]),
                orig_lng: np.ndarray = np.array([-0.118092])
                ) -> np.ndarray:
    """

    Computes the Haversine distance between co-ordinates.

    Args:
        dest_lat: a numpy array of lattitude's.
        desk_lng: a numpy array of longitude's.
        orig_lat: a numpy array of length 1, for london's lattitude but can be set to any city.
        orig_lng: a numpy array of length 1, for london's longitude but can be set to any city.
    Returns:
        dist: a numpy array of all computed distances.

    """
    R = 3958.8
    dest_lat = dest_lat*np.pi/180.0
    dest_lng = np.deg2rad(dest_lng)
    orig_lat = np.deg2rad(orig_lat)
    orig_lng = np.deg2rad(orig_lng)
    d = np.sin((orig_lat - dest_lat)/2)**2 + np.cos(dest_lat) * \
        np.cos(orig_lat) * np.sin((orig_lng - dest_lng)/2)**2
    dist = 2 * R * np.arcsin(np.sqrt(d))
    return dist

def get_londoners() -> List:
    """
    Returns:
        users: list of users from the https://bpdts-test-app.herokuapp.com/city/London/users api call.
    """
    res = requests.get(
        'https://bpdts-test-app.herokuapp.com/city/London/users')
    if res.status_code == 200:
        users = json.loads(res.text)
    return users

def get_londonders_proximity() -> List:
    """
    Returns:
        users: list of users from the https://bpdts-test-app.herokuapp.com/users api call after filtering
        on distances less than 50 miles of London's latitude: 51.509865 and longitude: -0.118092.
        The function extracts the latitude and longitudes as a numpy array for a vectorized implementation
        of the Haversine formula. 
    """
    try:
        res = requests.get('https://bpdts-test-app.herokuapp.com/users')
        if res.status_code == 200:
            data = json.loads(res.text)
            df = pd.DataFrame(data)
            df.latitude = df.latitude.astype(float)
            df.longitude = df.longitude.astype(float)
            lats = df.latitude.values
            longs = df.longitude.values
            dist = distance_np(lats, longs)
            indexes = [idx for idx, i in enumerate(dist) if i < 50.]
            users = []
            for x in indexes:
                if x != 0:
                    users.append(data[x-1])
                else:
                    users.append(data[x])
            return users
    except Exception as e:
        return {"message": str(e)}
