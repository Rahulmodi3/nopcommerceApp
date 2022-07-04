pytest -m "sanity" --html=./Reports/report.html testCases/
rem pytest -s -v-m “sanity or regression” --html=./Reports/report.html testCases/--browser chrome
rem pytest -s -v -m "regression" testCases/
rem pytest -s -v -m "sanity and regression" testCases/