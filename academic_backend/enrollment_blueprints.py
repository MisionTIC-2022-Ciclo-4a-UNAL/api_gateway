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

enrollment_blueprints = Blueprint("enrollment_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-academic') + "/enrollment"


@enrollment_blueprints.route("/enrollments", methods=['GET'])
def get_all_enrollments() -> dict:
    url = f'{url_base}/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@enrollment_blueprints.route("/enrollment/<string:id_>", methods=['GET'])
def get_enrollment_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@enrollment_blueprints.route("/enrollment/insert", methods=['POST'])
def insert_enrollment() -> dict:
    enrollment = request.get_json()
    course_id = enrollment.get('course').get('_id')
    del enrollment['course']
    student_id = enrollment.get('student').get('_id')
    del enrollment['student']
    url = f'{url_base}/insert/course/{course_id}/student/{student_id}'
    response = requests.post(url, headers=HEADERS, json=enrollment)
    return response.json()


@enrollment_blueprints.route("/enrollment/update/<string:id_>", methods=['PUT'])
def update_enrollment(id_: str) -> dict:
    enrollment = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=enrollment)
    return response.json()


@enrollment_blueprints.route("/enrollment/delete/<string:id_>", methods=['DELETE'])
def delete_enrollment(id_: str) -> tuple:
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code
