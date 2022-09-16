from flask import Flask, redirect
from distutils.sysconfig import PREFIX
from resources.task import Task, TaskList, TaskSearch
from flask_restful import Api
from flasgger import Swagger 
import os 

from db import db

#Api es la interfaz de comunicación , que sirve para que los otros sistemas se puedan conectar ahi 

app = Flask(__name__)
api = Api(app,errors = {
    ''
})
PREFIX = os.environ.get('PREFIX_PATH' , '/api')

#Swagger configuración
app.config['SWAGGER'] = {
    'title': 'todo-backend',
    'version': '1.0.0',
    'description': 'API de servicios REST en Flask / Jimena',
    'uiversion': 2,
    'tags': [{'name': 'jwt'}],
    'specs': [{
        'endpoint': 'apispec_1',
        'route': f'{PREFIX}/apispec_1.json',
        'rule_filter': lambda rule: True, # all in
        'model_filter': lambda tag: True # all in
    }],
    'specs_route': f"{PREFIX}/apidocs/",
    'static_url_path': f'{PREFIX}/static'
}
swagger = Swagger(app)

#Function to facilitate the app configuration from enviroment variables
def env_config(name, default):
    app.config[name] = os.environ.get(name, default=default)

#Database configuracion
env_config('SQLALCHEMY_DATABASE_URI','postgresql://postgres:notevoyadecir0@localhost:5432/todo')

#SQL ALCHEMY CONFIG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False



@app.route('/')
@app.route(f'{PREFIX}')
def welcome():
    return redirect(f"{PREFIX}/apidocs", code=302)

#los recursos siemrpe se nombran en plural "task" a "tasks"
api.add_resource (Task, f'{PREFIX}/tasks/<id>') #definicion de un recurso
api.add_resource (TaskList, f'{PREFIX}/tasks') #definicion de un recurso
api.add_resource (TaskSearch, f'{PREFIX}/search/tasks')

# Bloque opcional para ejecutr con python app.py
if __name__ =='__main__':
    db.init_app(app)
    app.run()
else:
    db.init_app(app)