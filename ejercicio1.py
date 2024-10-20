# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd
import streamlit as st
from datetime import time
from datetime import datetime
import datetime

st.title('Titulo del Proyecto')
st.write('Hola **como** estas')
st.header('header')
st.caption('Caption')

num=st.slider("num",0,100,step=5)
st.write("El numero ingresado es {}".format(num))


appointment = st.slider("Progame la asesoria:",
                        value=(time(11,30), time(12,45)))
st.write("Esta agendado para:", appointment)

start_time = st.slider("Ver casos ocurridos en",
                       value=datetime.datetime(2020, 1, 1, 9, 30),
                       format="DD/MM/YY - hh:mm") 
st.write("Fecha seleccionada:", start_time)

d = st.date_input(
    "Fecha de cumpleaños",
    datetime.date(2019, 7, 6)) 
st.write('Tu cumpleños es:', d)

option = st.selectbox('¿Cómo desearía ser contactado/a?',
                      ('Email', 'Teléfono', 'Whatsapp')) 
st.write('Seleccionó:', option)

n = st.slider("n", 5,100, step=1) 
chart_data = pd.DataFrame(np.random.randn(n),columns=['data']) 
st.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                  columns=['lat', 'lon']) 
st.map(df)