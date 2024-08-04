import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Data Visualizer')

folder_path =  r"C:\Users\Mahalakshmi.S\Desktop\srikrishnan learning\jenking_jar\datasets"
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
    fig, ax = plt.subplots(figsize=(6, 6))
    if plot_type == 'Line Plot':
        sns.lineplot(x=data[x_axis],y=data[y_axis])
    elif plot_type == 'Bar Chart':
        sns.barplot(x=data[x_axis],y=data[y_axis])
    elif plot_type == 'Scatter Plot':
        sns.scatterplot(x=data[x_axis],y=data[y_axis])

    plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=14)
    plt.xlabel(x_axis, fontsize=10)
    plt.ylabel(y_axis, fontsize=10)

    st.pyplot(fig)

#python -m streamlit run .\Disease_datavisualizzation.py