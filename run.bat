pytest -m "sanity" --html=./Reports/report.html testCases/ --browsername chromeheadless
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browsername chrome
rem pytest -s -v -m "regression" testCases/
rem pytest -s -v -m "sanity and regression" testCases/
