import streamlit as st

def km_to_miles(km):
    """Convert kilometers to miles."""
    return km * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles / 0.621371

# setup the Streamlit app
st.title("Kilometers ⇄ Miles Converter")

conversion_directon = st.radio("Choose the conversion direction:", ("Kilometers to Miles", "Miles to Kilometers"))

if conversion_directon == "Kilometers to Miles":
    km = st.number_input("Enter distance in kilometers:", min_value=0.0, step=0.1)
    if st.button("Convert"):
        miles = km_to_miles(km)
        st.success(f"{km} kilometers is equal to {miles:.2f} miles.")
else:
    miles = st.number_input("Enter distance in miles:", min_value=0.0, step=0.1)
    if st.button("Convert"):
        km = miles_to_km(miles)
        st.success(f"{miles} miles is equal to {km:.2f} kilometers.")