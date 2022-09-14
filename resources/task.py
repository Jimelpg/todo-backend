#crear un constructor = resources
# def es para definir metodos
# __int__ para definir constructores
#jason es para retornar el objeto en formao json = diccionario
# get me trae todos los datos por ejemplo con el id me trae los datos de la tarea
# 404  es el código de error
#401 no autorizado (mas ppt)

from flask_restful import Resource, reqparse
from models.task import TaskModel
from flasgger import swag_from

class Task (Resource):

    #para el manejo de peticiones
    #reqparse.RequestParse()

    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)
    parser.add_argument('description', type= str)

    @swag_from('../swagger/task/get_task.yaml')
    def get(self, id):
        tarea = TaskModel(1, "Hola Jimena")
        if tarea:
            return tarea.json()
        return {'message': "No se encuentra la Tarea"},404



