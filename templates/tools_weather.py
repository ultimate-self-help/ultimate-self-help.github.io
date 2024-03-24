
import streamlit as st
import requests
from bs4 import BeautifulSoup
#import icecream as ic

def app():
    st.title("Weather")

    # def get_html_content(search_query):
    #     # Source: https://stackoverflow.com/questions/75136507/how-to-scrape-specific-google-weather-text-with-beautifulsoup
    #     # params = {'q':'weather in New York City, New York, USA', 'hl': 'en'}
    #     params = {'q': 'weather in ' + search_query, 'h1': 'en'}
    #     #params = {'q':'weather in New York City, New York, USA', 'hl': 'en'}
    #     headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    #     cookies = {'CONSENT':"YES+cb.20220419-08-p0.cs+FX+111"}

    #     url = 'https://www.google.com/search'
    #     soup = BeautifulSoup(requests.get(url, params=params, headers=headers, cookies=cookies).content, 'html.parser')

    #     st.write("Day, Description, Temp C for " + search_query)    
    #     for t in soup.select('#wob_dp [aria-label]'):
    #         how = t.find_next('img')['alt']
    #         temp = t.find_next('span').get_text(strip=True)
    #         print('{:<5} {:<20} {}'.format(t.text, how, temp))
            
    #         #.bug. I suspect incorrect days, dates?
    #         st.write('{:<5} {:<20} {}'.format(t.text, how, temp))


    def get_json_content(seach_query):
        params = {'q': 'weather in ' + search_query, 'h1': 'en'}
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}
        cookies = {'CONSENT':"YES+cb.20220419-08-p0.cs+FX+111"}
        url = 'https://www.google.com/search'
        soup = BeautifulSoup(requests.get(url, params=params, headers=headers, cookies=cookies).content, 'html.parser')

        new_array = []
        for t in soup.select('#wob_dp [aria-label]'):
            how = t.find_next('img')['alt']
            temp = t.find_next('span').get_text(strip=True)
            print('{:<5} {:<20} {}'.format(t.text, how, temp))
            #st.write('{:<5} {:<20} {}'.format(t.text, how, temp))
            new_array.append({
                "Day":t.text,
                "Outlook": how,
                "Temp": temp,
            })
        #new_dataframe = st.dataframe(new_array, hide_index=True) 
        #print("NEW DF: ", new_array)
        
        st.table(new_array)
        st.write("According to Google.com")
            


    with st.form("google_search"):
        search_query = st.text_input(
                "To get this weeks forcast. Enter your City and Country e.g. Sydney Australia.",
                placeholder="Sydney Australia",
                value="Sydney Australia"
        )

        submitted = st.form_submit_button("Get Todays Weather")
        if submitted:
            get_json_content(search_query)
            #get_html_content(search_query) (Obsolete, not used)

            