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

from flask import request, Blueprint
import requests

from utils import load_file_config, HEADERS

student_blueprints = Blueprint("student_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-academic') + "/student"


@student_blueprints.route("/students", methods=['GET'])
def get_all_students() -> dict:
    url = f'{url_base}/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@student_blueprints.route("/student/<string:id_>", methods=['GET'])
def get_student_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@student_blueprints.route("/student/insert", methods=['POST'])
def insert_student() -> dict:
    student = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=student)
    return response.json()


@student_blueprints.route("/student/update/<string:id_>", methods=['PUT'])
def update_student(id_: str) -> dict:
    student = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=student)
    return response.json()


@student_blueprints.route("/student/delete/<string:id_>", methods=['DELETE'])
def delete_student(id_: str) -> dict:
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code
