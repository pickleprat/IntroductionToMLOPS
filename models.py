from pydantic import BaseModel 

class BookRequest(BaseModel): 
    name: str 

class BookResponse(BaseModel): 
    author: str 
    sold_out: bool 
    billboard: bool 
