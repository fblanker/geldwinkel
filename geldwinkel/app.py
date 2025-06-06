
import streamlit as st

st.set_page_config(page_title="De Geldwinkel", page_icon="🛍️")

# Init session state
if 'geld' not in st.session_state:
    st.session_state.geld = 5.0
if 'mandje' not in st.session_state:
    st.session_state.mandje = []

# Producten en prijzen
producten = {
    "Appel 🍎": 1.0,
    "Banaan 🍌": 1.5,
    "Sinaasappel 🍊": 2.0
}

st.title("🛍️ De Geldwinkel – Niveau 1: Fruitkraam")
st.write("Welkom! Je hebt €{:.2f} om uit te geven. Wat wil je kopen?".format(st.session_state.geld))

# Winkel interface
for naam, prijs in producten.items():
    if st.button(f"Koop {naam} – €{prijs:.2f}"):
        if st.session_state.geld >= prijs:
            st.session_state.geld -= prijs
            st.session_state.mandje.append(naam)
            st.success(f"Je hebt {naam} gekocht!")
        else:
            st.error("Je hebt niet genoeg geld!")

st.write(f"💶 Geld over: €{st.session_state.geld:.2f}")
st.write("🧺 Je winkelmandje:", ", ".join(st.session_state.mandje) if st.session_state.mandje else "leeg")

if st.session_state.geld <= 0:
    st.warning("Je hebt geen geld meer! Goed gedaan!")
