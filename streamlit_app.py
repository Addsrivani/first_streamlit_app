import streamlit
streamlit.title('My parents new healthy meal')

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
import pandas
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)
import requests 
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)       
import snowflake.connector
   
