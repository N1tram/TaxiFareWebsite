import streamlit as st
import datetime
import requests

st.markdown('''
# Prediction of Taxi Fares in NYC

Please provide the following information to get a prediction.
''')

date = st.date_input(
    "Date"
)
time = st.time_input(
    "Time"
)
pickup_lat = st.text_input(
    "Pickup Latitude",
    "-73.9798157"
)
pickup_lng = st.text_input(
    "Pickup Longitude",
    "40.7614327"
)
dropoff_lat = st.text_input(
    "Dropoff Latitude",
    "-73.9797156"
)
dropoff_lng = st.text_input(
    "Dropoff Longitude",
    "40.6413111"
)
passenger = st.selectbox("Passengers", [1,2,3,4,5,6,7,8])

url = 'https://taxifare.lewagon.ai/predict'

params = dict(
  pickup_datetime=datetime.datetime.combine(date,time),
  pickup_longitude=pickup_lng,
  pickup_latitude=pickup_lat,
  dropoff_longitude=dropoff_lng,
  dropoff_latitude=dropoff_lat,
  passenger_count=passenger
)

taxifare_api_url = url

if st.button('Predict'):
    response = requests.get(
    taxifare_api_url,
    params=params)
    if response.status_code == 200:
        st.text("API call success")
    else:
        st.text("API call error")
    prediction = round(response.json().get('fare'),2)
    st.text(prediction)
