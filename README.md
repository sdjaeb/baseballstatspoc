# baseballstatspoc
Basic Flask app to display some player information gathered from multiple data sources and normalized to a common data schema.

Install Flask (https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)

`pip install requests`

# Notes
1. There is no error/exception handling.  A few things I would add:
    1. An error/404 page when the `requests.get` fails: 
    2. Checking against the various lists/dictionaries: KeyError, IndexError, TypeError
    3. File actions: FileNotFoundError, EOFError,  
    4. Fallback to Exception
2. Parameters on the various stats retrieval functions, to refine the data to retrieve.
    1. How many records from the data source
    2. Name Parts, Throws/Bats, Position, Team Played For, Height, Weight
