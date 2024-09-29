from fastapi import FastAPI 

from models import BookRequest, BookResponse  
from data import books 

import uvicorn 

app = FastAPI() 

@app.post("/book", response_model=BookResponse) 
async def get_book(book: BookRequest) -> BookResponse:  
    return books[book.name]  
    
if __name__ == "__main__":
    uvicorn.run(app, port=8000) 


    

