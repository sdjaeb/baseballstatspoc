# baseballstatspoc
Basic Flask app to display some player information gathered from multiple data sources and normalized to a common data schema.

Install Flask (https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)

Dependencies:

`pip install requests`

## Data Sources
1. JSON file:

    `http://127.0.0.1:5000/json-stats/`
    
    ![json-stats](https://github.com/sdjaeb/baseballstatspoc/blob/main/screenshots/json-stats.png)

2. API:

    `http://127.0.0.1:5000/api-stats/`
    
    ![api-stats](https://github.com/sdjaeb/baseballstatspoc/blob/main/screenshots/api-stats.png)

3. Aggregate sources (JSON file and API) - will return num rows from each source
   
   `http://127.0.0.1:5000/` -or-
   
   `http://127.0.0.1:5000/combined-stats/`
   
   ![combined-stats](https://github.com/sdjaeb/baseballstatspoc/blob/main/screenshots/combined-stats.png)

## Changing the number of rows returned
The number of records returned defaults to 10. If you want more or less than 10, append the number to the URL.  Negative values will do a reverse slice. Anything less than -1 will clamp at -1.
    
`http://127.0.0.1:5000/api-stats/5/`

![api-stats-5](https://github.com/sdjaeb/baseballstatspoc/blob/main/screenshots/api-stats-5.png)
    

