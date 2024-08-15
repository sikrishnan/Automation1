import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Data Visualizer')

folder_path =  r"C:\Users\Mahalakshmi.S\Desktop\srikrishnan learning\jenking_jar\datasets"
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    # Save the uploaded file to the folder path
    file_save_path = os.path.join(folder_path, uploaded_file.name)
    with open(file_save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' saved to '{folder_path}'")
    
files =  [file for file in os.listdir(folder_path) if file.endswith('.csv')]
selected_file = st.selectbox('Select a file', files, index=None)

if selected_file:
    file_path = os.path.join(folder_path,selected_file)
    data = pd.read_csv(file_path)
    col1,col2=st.columns(2)
    columns = data.columns.tolist()
    with col1:
        st.write(selected_file +" file dataset")
        st.write(data.head())
    with col2:
        x_axis = st.selectbox('Select the X-Axis',options=columns + [None], index=None)
        y_axis = st.selectbox('Select the Y-Axis',options=columns + [None], index=None)

        graph_plot_list = ['Line Plot','Bar Chart', 'Scatter Plot']

        plot_type = st.selectbox('Select the required plot type', options=graph_plot_list, index= None)

if st.button('Generate Plot'):
    fig = None
    if plot_type == 'Line Plot':
        fig = px.line(data, x=x_axis, y=y_axis, title=f'{plot_type} of {y_axis} vs {x_axis}')
    elif plot_type == 'Bar Chart':
        fig = px.bar(data, x=x_axis, y=y_axis, title=f'{plot_type} of {y_axis} vs {x_axis}')
    elif plot_type == 'Scatter Plot':
        fig = px.scatter(data, x=x_axis, y=y_axis, title=f'{plot_type} of {y_axis} vs {x_axis}')

    if fig:
        st.plotly_chart(fig, use_container_width=True)    

#python -m streamlit run .\Disease_datavisualizzation.py