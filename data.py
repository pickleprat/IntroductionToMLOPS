from models import BookResponse 
from typing import Dict 
books : Dict[str, BookResponse] =  { 
        "Silent Patient": BookResponse(author="Alex Edward", sold_out=True, billboard=True),  
        "Heartache": BookResponse(author="Merissa Meyers", sold_out=True, billboard=False), 
        "Heaven's Official Blessing": BookResponse(author="Xing Pie", sold_out=False, billboard=False),  
} 
