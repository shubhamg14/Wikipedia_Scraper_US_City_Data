# Wikipedia_Scraper_US_City_Data

Web Scraper written in python using Beautiful Soup library to fetch data for top cities in the US from Wikipedia.

## Requirements
1. Python 3
2. Beautiful Soup
3. Pandas

## Description

* The program first hits the wikipedia URL of "List_of_United_States_cities_by_population" and then fetches few columns ('City', 'State', 'Population', 'Land_Area', 'Location_Coordinates') from that table.

* _*Secondly, it fetches the underlying web url to each individual city's page and then **hits each city's page and fetches Major Aiprorts near to that city and also the first paragraph as City's description.**_

* _This program can be easily extended to fetch as many fields as required from individual pages_.

## Code Walkthrough

* Imported required libraries (BeautifulSoup, Pandas and Request for HTTP requests)

* Functions:

  * __*fetch_ind_city_desc()*__: This function hits the individual city's URL and fetches the first oaragraph description about the city and store  it under 'City_Description' field in final CSV.
  
  * __*fetch_major_airports()*__: This function hits the individual city;s URL and fetches major airports near that city. This data can be found under 'Airports' field in CSV
  
  * __*write_to_csv()*__: This function generates CSV file for the scraped data.
  
  * __*Main()*__: This function is the main method for the program which first visits the List of top United States cities page on Wikipedia from where it fetches few columns about each city such as ('City', 'State', 'Population', 'Land_Area', 'Location_Coordinates') and then calls
fetch_ind_city_desc(), fetch_major_airports() and finally write_to_csv() method for writing final output to a CSV file in the current       directory from where the program is being run.

## Testing

The generated CSV file got successfully loaded into BigQuery table.

## Screenshots

__Final schema of Big Query table__

![alt text](https://github.com/shubhamg14/Wikipedia_Scraper_US_City_Data/blob/master/Big_Query_Screenshots/wiki_scraping_schema.PNG)

__File load status of Big Query table__

![alt text](https://github.com/shubhamg14/Wikipedia_Scraper_US_City_Data/blob/master/Big_Query_Screenshots/wiki_scraping_load_status.PNG)

__Data screenshots from Big Query table__

__Screenshot-1__

![alt text](https://github.com/shubhamg14/Wikipedia_Scraper_US_City_Data/blob/master/Big_Query_Screenshots/wiki_scraping_big_query_1.PNG)

__Screenshot-2__

![alt text](https://github.com/shubhamg14/Wikipedia_Scraper_US_City_Data/blob/master/Big_Query_Screenshots/wiki_scraping_big_query_2.PNG)


__Screenshot-3__

![alt text](https://github.com/shubhamg14/Wikipedia_Scraper_US_City_Data/blob/master/Big_Query_Screenshots/wiki_scraping_big_query_3.PNG)

__Screenshot of CSV File__

![alt text](https://github.com/shubhamg14/Wikipedia_Scraper_US_City_Data/blob/master/Big_Query_Screenshots/wiki_scraping_csv.PNG)

## Executing the code

In terminal type "__python3 wiki_scraper.py__" and code will execute. The final csv would be generated at the location from where the code is run.
