install: 
	pip install -r requirements.txt 

lint: 
	pylint --disable=R,C *.py 

serve: 
	python app.py 

test: 
	python -m pytest -vv test_app.py && locust -t 2s -u 100 --spawn-rate 5 -H http://localhost:8000

clean_cache: 
	rm -rf __pycache__ .pytest_cache 
