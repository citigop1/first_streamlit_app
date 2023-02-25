
import streamlit
import pandas

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

