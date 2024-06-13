import streamlit as st

def calculate_emissions(km_essence, cons_essence, km_diesel, cons_diesel, meetings, distance_meeting, num_sheets_used, num_sheets_cloud):
    # CO2 emissions factors
    factor_essence = 2.31
    factor_diesel = 2.68
    factor_paper = 2.7

    # Convert number of sheets to kg
    paper_used_kg = num_sheets_used * 0.005
    paper_cloud_kg = num_sheets_cloud * 0.005

    # Calculate emissions
    emissions_essence = km_essence * (cons_essence / 100) * factor_essence
    emissions_diesel = km_diesel * (cons_diesel / 100) * factor_diesel
    emissions_paper_used = paper_used_kg * factor_paper

    # Calculate potential emissions if meetings were done by car (using essence)
    emissions_meetings_car = meetings * distance_meeting * (cons_essence / 100) * factor_essence

    # Calculate potential emissions if pages were printed instead of cloud
    emissions_paper_cloud = paper_cloud_kg * factor_paper

    # Total emissions
    total_emissions = emissions_essence + emissions_diesel + emissions_paper_used

    # Calculate the gain in CO2 emissions
    gain_co2_meetings = emissions_meetings_car
    gain_co2_paper = emissions_paper_cloud

    result = {
        'Emissions Essences': emissions_essence,
        'Emissions Diesel': emissions_diesel,
        'Emissions Papier Utilisé': emissions_paper_used,
        'Emissions Réunions en Voiture': emissions_meetings_car,
        'Emissions Potentielles Pages Non Imprimées': emissions_paper_cloud,
        'Total Emissions': total_emissions,
        'Gain CO2 Visioconférences': gain_co2_meetings,
        'Gain CO2 Pages Non Imprimées': gain_co2_paper
    }

    return result

st.title('Calculateur de CO2')

km_essence = st.number_input('Kilomètres parcourus (Essence)', value=0.0)
cons_essence = st.number_input('Consommation de carburant (Essence, litres/100 km)', value=0.0)
km_diesel = st.number_input('Kilomètres parcourus (Diesel)', value=0.0)
cons_diesel = st.number_input('Consommation de carburant (Diesel, litres/100 km)', value=0.0)
meetings = st.number_input('Réunions évitées grâce aux visioconférences', value=0)
distance_meeting = st.number_input('Distance moyenne par réunion (km)', value=0.0)
num_sheets_used = st.number_input('Nombre de feuilles de papier utilisées', value=0)
num_sheets_cloud = st.number_input('Nombre de feuilles de papier mises sur le cloud', value=0)

if st.button('Calculer'):
    result = calculate_emissions(km_essence, cons_essence, km_diesel, cons_diesel, meetings, distance_meeting, num_sheets_used, num_sheets_cloud)
    
    st.write(f"Émissions de CO2 (kg):")
    st.write(f"Essence: {result['Emissions Essences']:.2f}")
    st.write(f"Diesel: {result['Emissions Diesel']:.2f}")
    st.write(f"Papier utilisé: {result['Emissions Papier Utilisé']:.2f} (Nombre de feuilles: {num_sheets_used})")
    st.write(f"Émissions potentielles pour réunions en voiture: {result['Emissions Réunions en Voiture']:.2f}")
    st.write(f"Émissions potentielles pour pages non imprimées: {result['Emissions Potentielles Pages Non Imprimées']:.2f}")
    st.write(f"Total: {result['Total Emissions']:.2f}")
    st.write(f"Gain en CO2 grâce aux visioconférences: {result['Gain CO2 Visioconférences']:.2f}")
    st.write(f"Gain en CO2 grâce aux pages non imprimées: {result['Gain CO2 Pages Non Imprimées']:.2f}")
