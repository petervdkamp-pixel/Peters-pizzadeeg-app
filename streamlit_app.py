import streamlit as st

# --- CONFIGURATIE ---
st.set_page_config(page_title="Pizza-expert calculator", page_icon="🍕", layout="centered")

st.title("🍕 Pizza-expert calculator")
st.markdown("De ultieme tool voor direct deeg en biga-recepten. Scroll voor tips eerst omlaag voor expert-tips.")

# --- SIDEBAR: INPUTS ---
st.header("📦 Basisinstellingen")
aantal = st.number_input("Aantal deegballen", min_value=1, value=6)
gewicht = st.number_input("Gewicht per bol (gram)", min_value=100, value=250)
hydro_totaal = st.slider("Hydratatie (%)", 50, 80, 65)
zout_perc = st.slider("Zout (%)", 1.0, 4.0, 2.5, 0.1)
suiker_perc = st.slider("Suiker (%)", 0.0, 3.0, 0.0, 0.5)
olijfolie_perc = st.slider("Olijfolie (%)", 0.0, 5.0, 0.0, 0.5)
waste_perc = st.number_input("Waste factor (% extra deeg)", 0, 10, 2)
oven_temp = st.number_input("Oventemperatuur (°C)", 150, 550, 480)

st.header("🧪 Methode & Gist")
methode = st.radio("Kies Methode", ["Direct deeg", "Biga"])
gist_type = st.radio("Gist Type", ["Instant (IDY)", "Vers"])

# --- RIJSSCHEMA ---
st.header("🕒 Planning & Temperatuur")
col1, col2 = st.columns(2)
with col1:
    temp_ct = st.number_input("Koelkasttemperatuur (°C)", 2, 10, 4)
with col2:
    temp_rt = st.number_input("Kamertemperatuur (°C)", 15, 30, 20)

if methode == "Biga":
    biga_perc = st.slider("Biga Percentage (%)", 10, 100, 50)
    st.subheader("Fase 1: De Biga")
    tijd_biga_ct = st.number_input("Uren Biga in koelkast", 0, 72, 24)
    tijd_biga_rt = st.number_input("Uren Biga op kamer (Kickstart)", 0, 24, 1)
    
    st.subheader("Fase 2: Na het mixen")
    tijd_deeg_ct = st.number_input("Uren deeg in koelkast", 0, 72, 18)
    tijd_deeg_rt = st.number_input("Uren deeg op kamertemperatuur", 0, 24, 6)
    
    totale_tijd_ct = tijd_biga_ct + tijd_deeg_ct
    totale_tijd_rt = tijd_biga_rt + tijd_deeg_rt
else:
    st.subheader("Planning direct deeg")
    totale_tijd_ct = st.number_input("Totaal uren in koelkast", 0, 100, 24)
    totale_tijd_rt = st.number_input("Totaal uren op kamer", 0, 48, 6)
totale_uren = totale_tijd_ct + totale_tijd_rt

# --- REKENKERN ---
verlies_factor = 1 + (waste_perc / 100)
totaal_gewicht = aantal * gewicht * verlies_factor
fi_totaal = (totale_tijd_ct * 2**((temp_ct - 20) / 7)) + (totale_tijd_rt * 2**((temp_rt - 20) / 7))
gist_perc_idy = (0.1 * 8) / fi_totaal
actueel_gist_perc = gist_perc_idy * 3 if gist_type == "Vers" else gist_perc_idy

bloem_totaal = totaal_gewicht / (1 + (hydro_totaal/100) + (zout_perc/100) + (suiker_perc/100) + (olijfolie_perc/100) + (actueel_gist_perc/100))
water_totaal = bloem_totaal * (hydro_totaal/100)
zout_totaal = bloem_totaal * (zout_perc/100)
suiker_totaal = bloem_totaal * (suiker_perc/100)
olijfolie_totaal = bloem_totaal * (olijfolie_perc/100)
gist_totaal = bloem_totaal * (actueel_gist_perc/100)

# --- OUTPUT ---
st.divider()
st.header("📋 Jouw Recept")

# Actieve Waarschuwing voor korte rijstijd
if totale_uren < 24:
    st.error(f"⚠️ **Waarschuwing:** Je totale rijstijd is slechts {totale_uren} uur. Wij adviseren minimaal 24 uur voor optimale smaak en verteerbaarheid (zie Expert Tips).")
    
# Contextuele adviezen
if oven_temp >= 450:
    if hydro_totaal < 65:
        st.warning("⚠️ **Hitte Advies:** Bij 450°C+ is 67-70% water aanbevolen om uitdroging te voorkomen.")
    if suiker_perc > 0:
        st.error("⚠️ **Suiker Waarschuwing:** Bij 450°C+ verbrandt suiker te snel. Laat suiker liever weg.")
    if olijfolie_perc > 0:
        st.warning("⚠️ **Olie Tip:** Olie kan gaan roken bij 450°C+. Wees zeer matig en laat liever weg.")
elif oven_temp < 300:
    if hydro_totaal > 64:
        st.warning("⚠️ **Bodem Tip:** Bij lage temp kan >64% water zorgen voor een zompige bodem.")
    if suiker_perc == 0:
        st.info("💡 **Bruining:** Voeg 1% suiker toe voor een mooiere kleur in een huishoudoven.")

# Recept Weergave
col_r1, col_r2 = st.columns(2)
if methode == "Biga":
    bloem_biga = bloem_totaal * (biga_perc / 100)
    water_biga = bloem_biga * 0.45
    with col_r1:
        st.subheader("Stap 1: De Biga")
        st.write(f"**Bloem:** {bloem_biga:.0f}g")
        st.write(f"**Water:** {water_biga:.0f}g (45%)")
        st.write(f"**Gist ({gist_type}):** {gist_totaal:.2f}g")
    with col_r2:
        st.subheader("Stap 2: Hoofdmix")
        st.write(f"**Restant bloem:** {bloem_totaal - bloem_biga:.0f}g")
        st.write(f"**Extra water:** {water_totaal - water_biga:.0f}g")
        st.write(f"**Zout:** {zout_totaal:.1f}g")
        if suiker_totaal > 0: st.write(f"**Suiker:** {suiker_totaal:.1f}g")
        if olijfolie_totaal > 0: st.write(f"**Olijfolie:** {olijfolie_totaal:.1f}g")
else:
    with col_r1:
        st.write(f"**Bloem:** {bloem_totaal:.0f}g")
        st.write(f"**Water:** {water_totaal:.0f}g")
        st.write(f"**Zout:** {zout_totaal:.1f}g")
    with col_r2:
        st.write(f"**Gist ({gist_type}):** {gist_totaal:.2f}g")
        if suiker_totaal > 0: st.write(f"**Suiker:** {suiker_totaal:.1f}g")
        if olijfolie_totaal > 0: st.write(f"**Olijfolie:** {olijfolie_totaal:.1f}g")

st.info(f"Totaal deeggewicht: {totaal_gewicht:.0f}g (incl. {waste_perc}% waste)")

# EXPERTTIPS SECTIE
with st.expander("🎓 Expert-tips & Theorie"):
    st.write("**1. Hydratatie vs. Oventemperatuur:**")
    st.write("De hoeveelheid water in je deeg is direct gekoppeld aan hoe heet je bakt:")
    st.write("- **Hete oven (450°C+):** Je bakt heel kort (60-90 sec). Een hoge hydratatie (65-70%) is nodig zodat de pizza niet uitdroogt.")
    st.write("- **Huishoudoven (max 300°C):** Je bakt langer (8-12 min). Een lagere hydratatie (max 62%) voorkomt dat je bodem slap of zompig blijft. Je pizza wordt iets krokanter.")
    st.divider()
    
    st.write("**2. De juiste bloem (Tipo 00):**")
    st.write("Voor deze calculator en de genoemde rijstijden is **Tipo 00 bloem** (met een hoog eiwitgehalte, min. 12g) vereist. Deze bloem is fijner gemalen en kan de grote hoeveelheid water en de lange fermentatie aan zonder dat het deeg slap wordt. Denk aan het merk Caputo.")
    st.divider()
    
    st.write("**3. Waarom Biga?**")
    st.write("Een Biga is een 'droog' voordeeg (45% hydratatie). In tegenstelling tot een direct deeg, waarbij je alles in één keer mengt, geeft een biga je pizza:")
    st.write("- **Meer aroma:** Diepe, complexe smaken die je met een kort proces nooit haalt.")
    st.write("- **Superieure structuur:** Een veel luchtigere en krokantere rand (*cornicione*).")
    st.write("- **Verteerbaarheid:** De lange fermentatie breekt complexe zetmelen alvast af.")
    st.divider()
    
    st.write("**4. De ideale fermentatietijd:**")
    st.write("Hoewel je na 8 uur al een pizza kunt bakken, adviseren wij **minimaal 24 uur** (en idealiter 48 uur of langer) totale rijstijd. Tijd is een ingrediënt: het zorgt ervoor dat het deeg lichter op de maag ligt en de gluten optimaal ontspannen voor het stretchen.")
    st.divider()
    
    st.write("**5. De Kickstart:**")
    if methode == "Direct Deeg":
        st.write("Laat het deeg na het kneden 1 uur op kamertemperatuur rusten. Dit geeft de gist een 'kickstart' voordat het de koelkast in gaat.")
    else:
        st.write("Laat de Biga (Stap 1) 1 tot 2 uur op kamertemperatuur staan voordat deze de koelkast in gaat. Na het mixen in Stap 2 kan het deeg direct koud staan.")
    st.divider()
    
    st.write("**6. Windowpane Test:**")
    st.write("Een lange fermentatie maakt het deeg elastisch en stretchbaar. Dat heb je nodig om het pizzadeeg goed te kunnen vormen. Je kunt je deeg testen: trek het zo dun uit dat je er bijna doorheen kunt kijken zonder dat het scheurt.")
    st.divider()
    
    if suiker_perc > 0:
        st.write("**6. Suiker & Gist:**")
        st.write("De toegevoegde suiker helpt vooral bij de kleuring. Het effect op de rijskracht is bij deze percentages verwaarloosbaar.")
