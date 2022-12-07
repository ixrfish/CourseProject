# Team Name: Avocado
# Project Name: Website Address Book
Topic: Web App for extracting addresses from an url

## Overview
This project provides a website `localhost:3000` for user to input an Eater URL containing multiple restaurant locations. An alert will pop up after the user has entered the url and prompted them to scroll down to see the result. The result is available as a table. The crawler result is at the first row and each different parsing method is a separate row. The backend server will fetch the content of the url and parse the contained address with multiple methods. It will also compare the precision of each method by compare to the ground truth data provided by the crawler. The software can be used to fetch a list of address in the Eater article. The user can then store the address or favorite them in Google Map to visit them later. 

## To Run the Software
Call `npm install` to install frontend dependencies and call `pip3 install -r requirements.txt` to install the python dependencies.
To start the frontend server, call `yarn start`. Call `yarn start-api` to start the backend api. 

## Implementation
The backend api server is in charge of parsing the address. Its entrypoint is `app.py` and the other code is in the `src/api` folder. To implement a new parser, edit the `src/api/address_parser.py` to add the parser code and call it in `app.py` for the new endpoint. The apis document is available when the api server is started at `localhost:5000/docs`. The crawler is implemented with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). For all parsers, the request is preprocessed by with fetching only the visible text part with Beautiful Soup. [Reference](https://stackoverflow.com/questions/1936466/how-to-scrape-only-visible-webpage-text-with-beautifulsoup) The [pyap](https://github.com/vladimarius/pyap) parser is a regular expression based parser that can parse the full address. The [commonregex](https://github.com/madisonmay/CommonRegex) is also a regular expression based matcher however it only provides street address. The nlp method uses [Spacy](https://github.com/explosion/spaCy) and a model trained mentioned in this [medium post](https://medium.com/globant/building-an-address-parser-with-spacy-e3376b7cff). Since the model expects a cleaned address, I added additional Named Entity Recognition matcher to find the actual addresses. 

## Team Member Contribution
The implementation is done solely by Iris.
