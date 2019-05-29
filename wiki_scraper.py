#To run this code got to command prompt and type "python wiki_scraper.py"
#The final CSV file would be generated at the path from where the code has been run 

#importing beautiful soup library(HTML parsing library for python)

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import unicodedata
#User defined function to fetch data from individual pages of each city

def fetch_ind_city_desc(hyper_link_city):
    url_city = hyper_link_city
    response_city = requests.get(url_city)
    soup_city = bs(response_city.text,"html.parser")
    
    #Printing only the first paragraph for each city page, which can be easily modified to pull any other data from the page 
    
    page_data = soup_city.find_all("p")
    
    city_description = page_data[1].text 
    
    
    if city_description is None or city_description.strip() == '':
        city_description_ascii = 'No data Available'   
            
    else:
        city_description = city_description.strip().replace(',', '')
        nfkd_form = unicodedata.normalize('NFKD', city_description)
        city_description_ascii = nfkd_form.encode('ASCII', 'ignore')
    
    return city_description_ascii

#Fetching major airports from each city's individual page

def fetch_major_airports(hyper_link_city):
    url_airport = hyper_link_city
    response_airport = requests.get(url_airport)
    soup_airport = bs(response_airport.text,"html.parser")
    
    #Finding airport tags and then fetching data from them
    
    if soup_airport.find("th", text="Primary airport"):
        major_airports = soup_airport.find("th", text="Primary airport").find_next_sibling("td").text
        return major_airports
    elif soup_airport.find("th", text="Primary Airport"):
        major_airports = soup_airport.find("th", text="Primary Airport").find_next_sibling("td").text
        return major_airports
    elif soup_airport.find("th", text="Major airports"):
        major_airports = soup_airport.find("th", text="Major airports").find_next_sibling("td").text
        return major_airports
    elif soup_airport.find("th", text="Major Airports"):
        major_airports = soup_airport.find("th", text="Major Airports").find_next_sibling("td").text
        return major_airports
    elif soup_airport.find("th", text="Major airport"):
        major_airports = soup_airport.find("th", text="Major airport").find_next_sibling("td").text
        return major_airports
    elif soup_airport.find("th", text="Airport"):
        major_airports = soup_airport.find("th", text="Airport").find_next_sibling("td").text
        return major_airports
    elif soup_airport.find("th", text="Airports"):
        major_airports = soup_airport.find("th", text="Airports").find_next_sibling("td").text
        return major_airports
    else:
        major_airports = ''
        return major_airports

#Module to write into a CSV file

def write_to_csv():
    df = pd.DataFrame([record.split("~") for record in table_form])

    #Column names for the file
    
    df.columns = ['Rank','City','State','Population', '2010 Population Census', '% Change in  population' ,'Land_Area','Land Area(km)','Population Density(mi)','Population Density(km)','Location_Coordinates','Airports','Wiki_Page','City_Description']
    
    #Excluding the rows where city is None
    
    df_1 = df[df['Population'].notnull()][['City','State','Population','Land_Area','Location_Coordinates','Airports','Wiki_Page','City_Description']]
    
    #Writing the data to a csv file which would can be loaded into the Big Query
    
    df_1.to_csv('./us_top_cities_data.csv', sep=',',index=False,encoding='utf-8-sig',decimal=',')

#Main method to pull all top cities data from wikipedia

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'
    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    soup.prettify()

    #Beautiful soup method to find all table body tags within HTML

    tables = soup.find_all("tbody")
    
    #Pulling data from 4th table on the wikipedia page
    
    rows = tables[4].find_all("tr")

    table_form=[]
    x=0
    #Iterating through each row in the wikipedia table
    
    for row in rows:
        counter = 0
        table_row = []
        hyper_link_city=''
        city_details = ''
        nfkd_form=''
        city_details_ascii=''
        city_airports = ''
        x+=1
        
        #For each cell in table on wikipedia page find data within each 'td' tag
        
        for cell in row.find_all("td"):
            if cell.find("a", href=True) and counter!=1:
        
                #Extracting hyperlinks for each city's main wiki page, which is used to extract data from individual pages
        
                hyper_link_city = "https://en.wikipedia.org"+cell.find('a')['href']
                counter += 1
                
                #Calling fetch_ind_city_desc module to fetch first paragraph from each city's individual wiki page
                
                city_details = fetch_ind_city_desc(hyper_link_city)
                
                #Calling fetch_major_airports module to fetch each city's airport from their individual pages
                
                city_airports = fetch_major_airports(hyper_link_city)
            
            #By iterating throught the table, append each cities data to the final list
  
            table_row.append(cell.get_text().strip().split('[')[0].split('/')[0])
        
        #appending airports
        
        table_row.append(city_airports)
        
        #appending hyperlink to the city information
        
        table_row.append(hyper_link_city)
        
        #appending each city's description from their individual pages to the final table
        
        table_row.append(str(city_details))
        
        #table_form.append(",".join(table_row))
        
        table_form.append("~".join(table_row))

#Calling write_to_csv method in order to generate csv file for the scraped data

write_to_csv()
