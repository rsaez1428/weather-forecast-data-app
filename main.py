import streamlit as st

import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")

days = st.slider("Forecast Days",
                 min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

if days > 1:
    days1 = 'days'
else:
    days1 = 'day'

st.subheader(f"{option} for the next {days} {days1} in {place}")


def get_data(days):
    dates = ["2023-12-26", "2023-12-27", "2023-12-28"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})

st.plotly_chart(figure)
