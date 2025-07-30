
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Nombre Pestaña
st.set_page_config(layout = 'centered', page_title = 'TFT Comps', page_icon = ':penguin:')

# Titulo Pagina
t1, t2 = st.columns([0.6, 0.4])
t1.image('unnamed.png', width = 500)
t2.title('Tiert List')
t2.markdown("**tel:** 1212 **| emal:** Manute@udea.edu.co")

#Secciones
steps = st.tabs(['**Comps**', '**Items**', '**Augments**'])
with steps[0]:

    st.write('SOUL SOCIETY')
    st.image('Captura.PNG', width = 0)
    data_df = pd.read_csv('Campanhas.csv', encoding= 'latin-1', sep = ';')
    data = st.selectbox('Escoge un ID', data_df['ID_Campana'], help = 'Muestra las campañas existentes')
    met_df = pd.read_csv('Metricas.csv', encoding= 'latin-1', sep = ';')

    m1, m2, m3 = st.columns([1,1,1])

    id1 = met_df[(met_df['ID_Campana'] == data)]
    m1.write('Metricas filtradas')
    m1.metric(label = 'Metrica 1', value = sum(id1['Conversiones']), delta = str(sum(id1['Rebotes'])) + 'Numero de Rebotes', delta_color = 'inverse')
    m2.write('Metricas filtradas')
    m2.metric(label = 'Metrica 2', value = np.mean(id1['Clics']), delta = str(np.mean(id1['Impresiones'])) + 'Promedio de impresiones', delta_color = 'inverse')
    


    if st.button('Type: Crafting', type = 'primary'):
        st.write('No disponible por cambio de parche')

with steps[2]:
    st.selectbox('**Tipo de aumento**', ['Silver','Gold', 'Prismatic'])




        
