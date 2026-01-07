import streamlit as st

# --- CONFIGURATIE ---
st.set_page_config(page_title="Expert Pizza Calculator", page_icon="🍕")

st.title("🍕 Expert Pizza Calculator")
st.markdown("Bereken je recept voor Direct Deeg of Biga.")

# --- SIDEBAR: INPUTS ---
st.sidebar.header("Instellingen")
aantal = st.sidebar.number_input("Aantal deegballen", min_value=1, value=6)
gewicht = st.sidebar.number_input("Gewicht per bol (gram)", min_value=100, value=250)
hydro_totaal = st.sidebar.slider("Hydratatie (%)", 50, 80, 65)
zout_perc = st.sidebar.slider("Zout (%)", 1.0, 4.0, 2.5, 0.1)
waste_perc = st.sidebar.number_input("Waste factor (%)", 0, 10, 3)
oven_temp = st.sidebar.number_input("Oventemperatuur (°C)", 200, 500, 480)

methode = st.sidebar.radio("Methode", ["Direct Deeg", "Biga"])
gist_type = st.sidebar.radio("Gist Type", ["Instant (IDY)", "Vers"])

# --- RIJS SCHEMA ---
st.header("Rijs Schema")
col1, col2 = st.columns(2)

with col1:
    temp_ct = st.number_input("Temp Koelkast (°C)", 2, 10, 4)
    temp_rt = st.number_input("Temp Kamer (°C)", 15, 30, 20)

if methode == "Biga":
    biga_perc = st.slider("Biga Percentage (%)", 10, 100, 50)
    st.subheader("Fase 1: Biga")
    tijd_biga_ct = st.number_input("Uren Biga in koelkast", 0, 72, 24)
    tijd_biga_rt = st.number_input("Uren Biga op kamer", 0, 24, 0)
    
    st.subheader("Fase 2: Hoofddeeg")
    tijd_deeg_ct = st.number_input("Uren deeg in koelkast", 0, 72, 18)
    tijd_deeg_rt = st.number_input("Uren deeg op kamer", 0, 24, 6)
    
    totale_tijd_ct = tijd_biga_ct + tijd_deeg_ct
    totale_tijd_rt = tijd_biga_rt + tijd_deeg_rt
else:
    totale_tijd_ct = st.number_input("Totaal uren in koelkast", 0, 100, 24)
    totale_tijd_rt = st.number_input("Totaal uren op kamer", 0, 48, 6)

# --- REKENKERN ---
verlies_factor = 1 + (waste_perc / 100)
totaal_gewicht = aantal * gewicht * verlies_factor
fi_totaal = (totale_tijd_ct * 2**((temp_ct - 20) / 7)) + (totale_tijd_rt * 2**((temp_rt - 20) / 7))
gist_perc_idy = (0.1 * 8) / fi_totaal
actueel_gist_perc = gist_perc_idy * 3 if gist_type == "Vers" else gist_perc_idy

bloem_totaal = totaal_gewicht / (1 + (hydro_totaal/100) + (zout_perc/100) + (actueel_gist_perc/100))
water_totaal = bloem_totaal * (hydro_totaal/100)
zout_totaal = bloem_totaal * (zout_perc/100)
gist_totaal = bloem_totaal * (actueel_gist_perc/100)

# --- OUTPUT ---
st.divider()
st.header("📋 Je Recept")

if oven_temp >= 450 and hydro_totaal < 65:
    st.warning("⚠️ TIP: Verhoog hydratatie naar 67% voor een zachtere rand in een hete oven.")

if methode == "Biga":
    bloem_biga = bloem_totaal * (biga_perc / 100)
    water_biga = bloem_biga * 0.45
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Stap 1: De Biga")
        st.write(f"**Bloem:** {bloem_biga:.0f}g")
        st.write(f"**Water:** {water_biga:.0f}g")
        st.write(f"**Gist:** {gist_totaal:.2f}g")
    with col_b:
        st.subheader("Stap 2: Hoofdmix")
        st.write(f"**Restant bloem:** {bloem_totaal - bloem_biga:.0f}g")
        st.write(f"**Extra water:** {water_totaal - water_biga:.0f}g")
        st.write(f"**Zout:** {zout_totaal:.1f}g")
else:
    st.write(f"**Bloem:** {bloem_totaal:.0f}g")
    st.write(f"**Water:** {water_totaal:.0f}g")
    st.write(f"**Zout:** {zout_totaal:.1f}g")
    st.write(f"**Gist:** {gist_totaal:.2f}g")

st.info(f"Totaal deeg: {totaal_gewicht:.0f}g | Waste factor: {waste_perc}%")
