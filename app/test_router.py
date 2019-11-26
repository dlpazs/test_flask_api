import pytest
import numpy as np
import requests
from flask import request
from app import app, utils
import json

class TestClass:
    def test_distance(self):
        dist_1 = utils.distance_np(np.array([7.22250]), np.array([124.25333]))
        assert round(dist_1[0]) == 7219

    def test_root(self):
        response = requests.get("http://localhost:5000/")
        assert response.status_code == 200

    def test_london(self):
        response = requests.get("http://localhost:5000/users/london")
        res = json.loads(response.text)
        assert response.status_code == 200
        assert isinstance(res, list)
        assert len(res) == 6

    def test_london_proximity(self):
        response = requests.get("http://localhost:5000/users/london/proximity")
        res = json.loads(response.text)
        assert response.status_code == 200
        assert isinstance(res, list)
        assert len(res) == 3

    def test_users(self):
        response = requests.get("http://localhost:5000/users")
        res = json.loads(response.text)
        assert response.status_code == 200
        assert isinstance(res, list)
        assert len(res) == 9
