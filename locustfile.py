from locust import HttpUser, task 
from data import books 
import random 

class EndpointFlooder(HttpUser): 
    @task 
    def flood_endpoint(self): 
        self.client.post(
                "/book", 
                json = (list(books.items())
                        [random.randint(0, 2)][0]) 
                ) 
