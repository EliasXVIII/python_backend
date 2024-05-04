from pydantic import BaseModel

###Ahora voy a crear una clase importada de BaseModel para nuestros libros.

class Book(BaseModel):
    id: int
    title: str
    year: str
    score: int