from data import books 
import requests 

def test_app(): 
    idx = 1 
    for book, response in books.items() : 
        print(f"Test {idx} for book {book}") 
        print("="*100) 
        got_response = requests.post(url = "http://localhost:8000/book", json={ "name": book }, timeout=10) 
        got = got_response.json() 
        assert got_response.status_code == 200 
        assert got["author"] == response.author
        assert got["sold_out"] == response.sold_out 
        assert got["billboard"] == response.billboard 
        print("="*100) 


if __name__ == "__main__":
    test_app() 
        
        

