#asi se define una clase en python ej "class nombre_clase"
#agregarle atributos y de que tipo es
#self es como el objeto del this
class TaskModel():
    id = int
    description = str

#se van a setear según los parametros asignados que se llaman igual 
    def __int__(self, id, description):
        self.id = id
        self.description = description

#metodo para retomar el objeto en formato json o diccionario
    def json(self, depht =0):
        json = {
            'id': self.id,
            'description': self.description
        }

        return json

#tarea.id=1
#tarea.description = "Hola Jimena"
#tarea.json()
#{'id':1, 'description': "Hola Jimena"}




    