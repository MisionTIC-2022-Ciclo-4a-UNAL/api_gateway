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

from datetime import timedelta
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (create_access_token, verify_jwt_in_request,
                                get_jwt_identity, JWTManager)
import requests
from waitress import serve


import utils
from academic_backend.course_blueprints import course_blueprints
from academic_backend.department_blueprints import department_blueprints
from academic_backend.enrollment_blueprints import enrollment_blueprints
from security_backend.permission_blueprints import permission_blueprints
from academic_backend.reports_blueprints import reports_blueprints
from security_backend.rol_blueprints import rol_blueprints
from academic_backend.student_blueprints import student_blueprints
from security_backend.user_blueprints import user_blueprints

# Create flask application
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "misiontic"
cors = CORS(app)
jwt = JWTManager(app)

# Add blueprints to define all endpoints available for API Gateway
app.register_blueprint(course_blueprints)
app.register_blueprint(department_blueprints)
app.register_blueprint(enrollment_blueprints)
app.register_blueprint(permission_blueprints)
app.register_blueprint(reports_blueprints)
app.register_blueprint(rol_blueprints)
app.register_blueprint(student_blueprints)
app.register_blueprint(user_blueprints)


@app.before_request
def before_request_callback() -> tuple:
    """
    This method is used to check before any request if the user
    has the permission to consume the microservice
    :return: Error message: unauthorized
    """
    endpoint = utils.clean_url(request.path)
    exclude_routes = ["/login", "/"]
    if exclude_routes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        user = get_jwt_identity()
        if user.get('rol'):
            has_grant = utils.validate_grant(endpoint, request.method, user['rol'].get('idRol'))
            if not has_grant:
                return {"message": "Permission denied by revision."}, 401
        else:
            return {"message": "Permission denied by not rol."}, 401


@app.route("/", methods=['GET'])
def home() -> dict:
    response = {"message": "Welcome to the Academic #MisionTIC2022 Project API Gateway..."}
    return response


@app.route('/login', methods=['POST'])
def login() -> tuple:
    user = request.get_json()
    url = f'{data_config.get("url-backend-security")}/user/login'
    request_response = requests.post(url, json=user, headers=utils.HEADERS)
    if request_response.status_code == 200:
        user_logged = request_response.json()
        del user_logged['rol']['permissions']
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get("id")}, 200
    else:
        return {"message": "Invalid access"}, 401


if __name__ == '__main__':
    data_config = utils.load_file_config()
    print(f'API Gateway Server running: http://{data_config.get("url-api-gateway")}:{data_config.get("port")}')
    serve(app, host=data_config.get('url-api-gateway'), port=data_config.get('port'))
