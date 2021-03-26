# baseballstatspoc
Basic Flask app to display some player information gathered from multiple data sources and normalized to a common data schema.

Install Flask (https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)

`pip install requests`

## Data Sources
1. JSON file:

    http://127.0.0.1:5000/json-stats/

2. API:

    http://127.0.0.1:5000/api-stats/

3. Aggregate sources (JSON file and API) - will return num rows from each source
   
   http://127.0.0.1:5000/ -or-
   
   http://127.0.0.1:5000/combined-stats/

## Changing the number of rows returned
The number of records returned defaults to 10.
    
    Getting data from an api source:
    ex: http://127.0.0.1:5000/api-stats/

If you want more or less than 10, append the number to the URL
    
    ex: http://127.0.0.1:5000/api-stats/5/
    
Negative values will do a reverse slice. Anything less than -1 will clamp at -1.
