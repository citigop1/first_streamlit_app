# - first script
#- updated recently
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title ('My Parents New Healthy Diner');

streamlit.header('Breakfast menu');
streamlit.text('🫐Omega 3 & Blueberry Oatmeal');
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie');
streamlit.text('🍳Hard-Boiled Free-Range Egg');
streamlit.text('🥑 Avocado Toast🍞');


streamlit.header('🍊🫐Build your Own Fruit Smoothie🍑🍓');
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index))

fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado','Strawberries']);

fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
     fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
     streamlit.dataframe(fruityvice_normalized)
   
 except URLError as e:
    streamlit.error()
   
   fruit_choice=streamlit.text_input('What fruit would like information about?','kiwi')
   streamlit.write('The user entered', fruit_choice)

#streamlit.text(fruityvice_response.json())

#Normalize the response
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json());
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()


my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select current_user(), current_account(), current_region()")
my_data_row=my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
# my_data_row=my_cur.fetchone()

my_data_row=my_cur.fetchall()
streamlit.header("The Fruit load list contains")
streamlit.dataframe(my_data_row)

add_my_fruit=streamlit.text_input('What fruit would like to add?')
streamlit.write('The user entered', add_my_fruit)
 
#streamlit.text("Thanks for adding " +add_my_fruit)
my_cur.execute("insert into fruit_load_list values('From Streamlit')")


