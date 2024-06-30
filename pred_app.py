import streamlit as st
import pandas as pd
import numpy as np
import joblib
import io
import discretize

model = joblib.load('./best_model.sav')

st.title('Prédiction des frais médicaux')

st.markdown('Bienvenue sur notre application **Insurance Pred**, le simulateur de frais médicaux.')
st.markdown('Ce simulateur vous permet en fonction des caractéristiques de votre client d\'évaluer les frais médicaux.')

one_pred,multi_pred = st.tabs(["Par saisie","Par Importation"])

with one_pred:
    st.write("Sur ce volet, vous pouvez prédire uniquement les frais d'un assuré en remplissant le formulaire ci-dessous.")

    col1_1, col1_2 = st.columns(2)
    
    with col1_1:
        age = st.number_input('Age',min_value=16,max_value=70,value=40,placeholder="Âge de l'assuré")
        bmi = st.number_input('IMC',min_value=10.,max_value=55.,value=20.,placeholder="IMC de l'assuré",format='%.2f')
        children = st.number_input('Enfants à charge',min_value=0,max_value=5,placeholder="Nbre d'enfant")
    
    with col1_2:
        
        statut_sex = st.radio('Sexe',['Homme','Femme'])
        if statut_sex == 'Homme':
            sex = 'male'
        else:
            sex = 'female'
        
        stat_tabac = st.radio('Statut tabagique',options=['Non fumeur','Fumeur'])
        if stat_tabac == "Non fumeur":
            smoker = 'no'
        else:
            smoker = 'yes'
            
        region_fr = st.selectbox("Region",['Sud est','Sud Ouest','Nord est','Nord ouest'])
        
        if region_fr == 'Sud est':
            region = 'southeast'
        elif region_fr == 'Sud ouest':
            region = 'southwest'
        elif region_fr == 'Nord est':
            region = 'northeast'
        else:
            region = 'northwest'
            
            
    col2_1, col2_2, col2_3 = st.columns([0.6,0.2,0.2])
    
    with col2_2:
        press_pred = st.button("Prédire",type='primary')
    with col2_3:
        st.button("Reset",type='secondary')
        
    if press_pred:
        ins_info = pd.DataFrame({'age':[age],'bmi':[bmi],'children':[children],'sex':[sex],'smoker':[smoker],'region':[region]})
        pred_value = model.predict(ins_info)
        st.markdown(f"Les frais médicaux facturés par l'assurance pour cette personne s'élèveraient à **{np.round(pred_value[0],2)}**")
        
with multi_pred:
    st.write('Ce onglet vous permet de prédire les frais d\'assurances médicales sur la base d\'un dataset à importer.')
    