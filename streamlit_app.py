import streamlit
streamlit.title('My parents new healthy meal')

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
