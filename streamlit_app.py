import requests
fruityvice_response=request.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
