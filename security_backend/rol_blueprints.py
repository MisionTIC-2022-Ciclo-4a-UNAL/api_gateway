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

from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config


rol_blueprints = Blueprint('rol_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-security') + "/rol"


@rol_blueprints.route("/rols", methods=['GET'])
def get_all_roles() -> dict:
    url = f'{url_base}/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@rol_blueprints.route("/rol/<int:id_>", methods=['GET'])
def get_rol_by_id(id_: int) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@rol_blueprints.route("/rol/insert", methods=['POST'])
def insert_rol() -> dict:
    rol = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=rol)
    return response.json()


@rol_blueprints.route("/rol/update/<int:id_>", methods=['PUT'])
def update_rol(id_: int) -> dict:
    rol = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.put(url, headers=HEADERS, json=rol)
    return response.json()


@rol_blueprints.route("/rol/delete/<int:id_>", methods=['DELETE'])
def delete_rol(id_: int) -> dict:
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code
