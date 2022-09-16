#asi se define una clase en python ej "class nombre_clase"
#agregarle atributos y de que tipo es
#self es como el objeto del this
from db import db
from flask_restful.reqparse import Namespace
from utils import _assign_if_something

class TaskModel(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key = True)
    descrip = db.Column(db.String)
    status = db.Column(db.String)

#se van a setear según los parametros asignados que se llaman igual 
    def __init__(self, id, descrip, status):
        self.id = id
        self.descrip = descrip
        self.status = status

#metodo para retomar el objeto en formato json o diccionario
    def json(self, depht =0):
        json = {
            'id': self.id,
            'descrip': self.descrip,
            'status': self.status
        }

        return json

 #saber de memoria // @ indica que este metodo es un metodo de la clase que sera utilizado en otro lugar 
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    #comparacuion campo por campo
    def from_reqparse(self, newdata: Namespace):
        for no_pk_key in ['descrip', 'status']:
            _assign_if_something(self, newdata, no_pk_key)

#tarea.id=1
#tarea.descrip = "Hola Jimena"
#tarea.json()
#{'id':1, 'descrip': "Hola Jimena"}




    