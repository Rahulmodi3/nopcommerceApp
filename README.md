

# Selenium Hybrid Framework

Create Hybrid Framework uisng (Python, Selenium, PyTest, Page Object Model, HTML Reports)



## Installation


•	Selenium : Selenium Libraries

•	Pytest : Python UnitTest framework

•	pytest-html : PyTest HTML Reports

•	pytest-xdist : Run Tests Parallel

•	Openpyxl : MS Excel Support

## Running Tests

To Run tests on desired browser
```bash
  pytest -s -v testCases/test_login.py - browser chrome

  pytest -s -v testCases/test_login.py --browser firefox
```
To Run tests parallel 
```bash
pytest -s -v -n=2  testcases/test_login.py -- browser chrome

```
To Genrate HTML Report
```bash
pytest -n=2 --html=Reports\report.html testCases/test_login.py - -browser chrome

```

To Run Group testCases
```bash
pytest  -m “sanity or regression” --html=./Reports/report.html testCases/-- browser chrome

```
    
