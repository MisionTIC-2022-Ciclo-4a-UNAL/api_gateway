"""
 # Copyright: Copyright (c) 2022
 #
 # License
 #
 # Copyright (c) 2022 by Carlos Andres Sierra Virgüez.
 # All rights reserved.
 #
 # This file is part of Academic #MisionTIC2022 Project Software.
 #
 # Academic #MisionTIC2022 Project is free software: you can redistribute it and/or modify it
 # under the terms of the GNU General Public License as published by the Free Software Foundation,
 # either version 3 of the License, or (at your option) any later version.
 #
 # Academic #MisionTIC2022 Project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 # without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 # See the GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License along with Academic #MisionTIC2022 Project.
 # If not, see <https://www.gnu.org/licenses/>.
"""

import json
import re
import requests

HEADERS = {"Content-Type": "application/json; charset=utf-8"}


def clean_url(url: str) -> str:
    """
    This method takes an endpoint path and remove any reference to a database
    id replacing it with a ? sign
    :param url: original endpoint path
    :return: endpoint with id references
    """
    segments = url.split("/")
    for segment in segments:
        if re.search('\\d', segment):
            url = url.replace(segment, "?")
    return url


def validate_grant(endpoint: str, method: str, id_rol: int) -> bool:
    """
    This method validates if a rol has the grant to consume a specific
    endpoint following a defined http method
    :param endpoint: endpoint path
    :param method: http method
    :param id_rol: rol id, based on user current rol
    :return: if rol has grant
    """
    data_config = load_file_config()
    url = f'{data_config.get("url-backend-security")}/rol/validate/{id_rol}'
    has_grant = False
    body = {
        "url": endpoint,
        "method": method
    }
    response = requests.get(url, json=body, headers=HEADERS)
    try:
        if response.status_code == 200:
            has_grant = True
    except Exception as e:
        print(e)
    return has_grant


def load_file_config() -> dict:
    """
    This function takes the json file where the configuration is set up
    and pass into a python dictionary
    :return: application setup
    """
    with open("config.json") as file_:
        data = json.load(file_)
    return data
