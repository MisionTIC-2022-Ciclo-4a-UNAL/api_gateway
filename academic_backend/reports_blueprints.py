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

from flask import Blueprint
import requests

from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-academic') + "/reports"


@reports_blueprints.route("/reports/student_enrollments/all", methods=['GET'])
def report_students_enrollments() -> dict:
    url = f'{url_base}/student_enrollments/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/student_enrollments/<string:id_>", methods=['GET'])
def report_students_enrollments_by_id(id_: str) -> dict:
    url = f'{url_base}/student_enrollments/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/course_enrollments/all", methods=['GET'])
def report_course_enrollments() -> dict:
    url = f'{url_base}/course_enrollments/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/course_enrollments/<string:id_>", methods=['GET'])
def report_course_enrollments_by_id(id_: str) -> dict:
    url = f'{url_base}/course_enrollments/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/students_top_enrollments", methods=['GET'])
def report_students_more_enrollments() -> dict:
    url = f'{url_base}/students_top_enrollments'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/department_enrollments", methods=['GET'])
def report_department_enrollments() -> dict:
    url = f'{url_base}/department_enrollments'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/department_distribution", methods=['GET'])
def report_department_distribution() -> dict:
    url = f'{url_base}/department_distribution'
    response = requests.get(url, headers=HEADERS)
    return response.json()
