
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="De Geldwinkel", page_icon="🛍️")

# Init session state
if 'geld' not in st.session_state:
    st.session_state.geld = 10.0
if 'spaarpot' not in st.session_state:
    st.session_state.spaarpot = 0.0
if 'mandje' not in st.session_state:
    st.session_state.mandje = []
if 'level' not in st.session_state:
    st.session_state.level = 1

def laad_afbeelding(naam):
    bestandsnaam = naam.lower().replace(" ", "") + ".png"
    pad = os.path.join("images", bestandsnaam)
    return Image.open(pad)

st.title("🛍️ De Geldwinkel")

st.write(f"📍 Niveau: {st.session_state.level}")
st.write(f"💶 Je hebt €{st.session_state.geld:.2f}")
st.write(f"🐷 In je spaarpot: €{st.session_state.spaarpot:.2f}")

# Knop om te sparen
if st.button("➡️ Zet €1 in je spaarpot"):
    if st.session_state.geld >= 1:
        st.session_state.geld -= 1
        st.session_state.spaarpot += 1
        st.success("€1 toegevoegd aan je spaarpot!")
    else:
        st.error("Niet genoeg geld om te sparen!")

# Producten per level
levels = {
    1: {
        "Appel": 1.0,
        "Banaan": 1.5,
        "Sinaasappel": 2.0
    },
    2: {
        "Knuffelbeer": 3.0,
        "Bal": 2.5,
        "Trein": 4.0
    }
}

producten = levels[st.session_state.level]

st.subheader("🛒 Wat wil je kopen?")

for naam, prijs in producten.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(f"images/{naam.lower()}.png", width=100)
    with col2:
        if st.button(f"Koop {naam} – €{prijs:.2f}", key=naam):
            if st.session_state.geld >= prijs:
                st.session_state.geld -= prijs
                st.session_state.mandje.append(naam)
                st.success(f"Je hebt {naam} gekocht!")
            else:
                st.error("Je hebt niet genoeg geld!")

st.write("🧺 Je winkelmandje:", ", ".join(st.session_state.mandje) if st.session_state.mandje else "leeg")

# Niveau wisselen
if st.session_state.level == 1 and st.button("🎯 Ga naar Niveau 2: Speelgoedwinkel"):
    st.session_state.level = 2
    st.session_state.mandje = []

if st.session_state.geld <= 0:
    st.warning("Je hebt geen geld meer! Goed gedaan!")
