from fastapi import FastAPI, HTTPException ### con esto voy a importar FastAPI, HTTPException lo importo para generar el mensaje de que no puede encontrar el libro y da el mensaje.

##se creo un modelo con BaseModel en model/books.py y lo vamos a importar en este archivo.

from model.books import Book


### *** => quiero hacer un crud y para ello vamos a hacer lo siguiente, una spseudo base de datos con un diccionario

books_db = [
    {
        "id": 0,
        "title":"Cien años de soledad",
        "year":"1967",
        "score": 496
    },
    {
        "id": 1,
        "title":"El señor de los anillos",
        "year":"1954",
        "score": 486
    },
    {
        "id": 2,
        "title":"El hobbit",
        "year":"1937",
        "score": 476
    },
    {
        "id": 3,
        "title":"1984",
        "year":"1949",
        "score": 466
    },
    {
        "id": 4,
        "title":"Un mundo feliz",
        "year":"1932",
        "score": 456
    },
    {
        "id": 5,
        "title":"Orgullo y prejuicio",
        "year":"1813",
        "score": 446
    },
    {
        "id": 6,
        "title":"Don Quijote de la Mancha",
        "year":"1605",
        "score": 436
    },
    {
        "id": 7,
        "title":"El Principito",
        "year":"1943",
        "score": 426
    },
    {
        "id": 8,
        "title":"La Hiliada",
        "year":"siglo VIII a.C",
        "score": 350
    }
]

app = FastAPI() ### dentro de app guardo FastAPI()

### Voy a crear un decorador al cual vamos a acceder con get en la url /

@app.get("/")
def root():
    return {"message": "This is my first backend"}

### luego vamos a la terminal para ejecutar uvicorn main:app --reload paso a =>arriba

###-----------------------------------------------###

###ahora vamos a obtener todos los datos de nuestra de la base de datos y para eso vamos a crear un GET que traiga en una funcion 
###todos los libros de la base de datos
@app.get("/api/v1/books", response_model=list[Book]) ###voy a indicarle que traiga el modelo que espera el front con Response_model "¡¡¡¡¡¡¡¡¡¡¡atencion con list[Book]!!!!!!"
### el list es para que agregue esto entre corchetes en la documentacion.
def get_books():
    return books_db

###Ahora voy a crear un filtrado de datos
### Este a traves de un bucle for nos va a proporcionar la informacion del libro solicitado, en caso de no estar disponible voy a generar una exepcion con HTTPExceptions a traves de un raiseç
@app.get("/api/v1/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

### Ahora voy a crear una funcion para crear un nuevo libro nuevo y poder verlo en la lista nueva!
@app.post("/api/v1/books", response_model=Book) ### con response_model=Book va a mostrar el nuevo archivo como lo hemos creado en basemodel con el nombre de class Book(BaseModel)
def create_book(book_data: Book): ###En esta funcion estoy almacenando los libros nuevos que se carguen 
    new_book = book_data.model_dump()###y en new_book voy a almacenar los datos nuevos pero en formato diccionario con el parametro model_dump()
    books_db.append(new_book) ### luego lo almaceno en la base de datos(books_db)y con el parametro .append(new_book) le estoy diciendo que lo guarde al final de la lista.!
    return new_book

### Ahora voy a crear una funcion para borrar eliminar un libro
@app.delete("/api/v1/books/{book_id}", response_model=Book) ### con el metodo .delete voy a eliminar en la ruta  /api/v1/books/ con el id{book_id} eliminare por id y tendra un response model de book
def delete_book(book_id: int): ### creo una funcion delete_book y le indicare que recoja el id del book que es un int(entero)
    for book in books_db: ### en este bucle FOR, si el ID del book es == al book_id ya cargado que realice el .remove(en book) de la base de datos books_db
        if book["id"] == book_id:
            book_delete = book
            books_db.remove(book)
            return book_delete
    raise HTTPException(status_code=404, detail="Book not found")











