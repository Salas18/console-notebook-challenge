# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
import datetime
from datetime import datetime

class Notebook:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code, title, text, importance, tags, creation_date):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.tags: list[str] = []
        self.creation_date = datetime



