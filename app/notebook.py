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

        def crear_titulo(self, titulo, ) -> str:
            return f"el titulo es {self.titulo}"

        def nota(self, texto) -> str:
            return f'el texto dice {self.texto}'

        def importancia_nota(self, HIGH, MEDIUM, LOW, identificador) -> str:
            if identificador == HIGH:
                return f'la importancia de la nota es HIGH'
            if identificador == MEDIUM:
                return f'la importancia de la nota es MEDIUM'
            else:
                return f"la importancia de la nota es LOW"

        def add_tag(self, tag: str):
            for tag in self.tags:
                if tag is not self.tags:
                    tag.append(self.tags)
                else:
                    return f'ya esta agregada'

        def listar_notas(self):
            pass

        def datetime(self, hora, formato_fecha_hora):
            hora = datetime.now()
            formato_fecha_hora = hora.strftime("%Y-%m-%d %H:%M:%S")
            return formato_fecha_hora




