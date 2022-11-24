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

import requests

security_backend = "http://127.0.0.1:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

# Create Roles
roles = [
    {"name": "Administrador", "description": "Administrador del sistema académico"},
    {"name": "Profesor", "description": "Encargado de dictar los cursos"},
    {"name": "Estudiante", "description": "Estudiante de la institución"},
]
url = f'{security_backend}/rol/insert'
administrator = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == "Administrador":
        administrator = response.json()
    print(response.json())
print("="*30)

# Basic permission and relation with administrator
modules = ['student', 'department', 'course', 'enrollment', 'user', 'rol', 'permission']
endpoints = [('s', 'GET'), ('/?', 'GET'), ('/insert', 'POST'), ('/update/?', 'PUT'), ('/delete/?', 'DELETE')]
url = f'{security_backend}/permission/insert'
for module in modules:
    for endpoint, method in endpoints:
        permission = f'/{module}{endpoint}'
        body = {
            "url": permission,
            "method": method
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.json())
        data_ = response.json()
        url_relation = f'{security_backend}/rol/update/{administrator.get("idRol")}/add_permission/{data_.get("id")}'
        response = requests.put(url_relation, headers=headers)
