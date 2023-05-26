import streamlit
streamlit.title('My parents new healthy meal')
streamlit.header('Breakfast Menu')
streamlit.text('Omega')
streamlit.text('Kale')
streamlit.text('boiled egg salad')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
##streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacodo','Strawberries'])





# Display the table on the page.

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
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
