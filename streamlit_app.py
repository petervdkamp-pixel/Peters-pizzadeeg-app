import streamlit as st

# --- CONFIGURATIE ---
st.set_page_config(page_title="Pizza-expert calculator", page_icon="🍕", layout="centered")

st.title("🍕 Pizza-expert calculator")
st.markdown("De ultieme tool voor direct deeg en biga-recepten. Scroll voor tips eerst omlaag voor expert-tips.")

# EXPERTTIPS SECTIE
with st.expander("🎓 Expert-tips & Theorie"):
    st.write("**1. Hydratatie vs. Oventemperatuur:**")
    st.write("De hoeveelheid water in je deeg (hydratatie, weergegeven in percentage van de bloem (100%)) is direct gekoppeld aan hoe heet je bakt:")
    st.write("- **Hete oven (450°C+):** Je bakt heel kort (60-90 sec). Een hoge hydratatie (65-70%) is nodig zodat de pizza niet uitdroogt.")
    st.write("- **Huishoudoven (max 300°C):** Je bakt langer (8-12 min). Een lagere hydratatie (max 62%) voorkomt dat je bodem slap of zompig blijft. Je pizza wordt iets krokanter.")
    st.divider()    
    st.write("**2. Wat is direct deeg?**")
    st.write("Bij direct deeg meng je alle ingrediënten (bloem, water, gist en zout) in één keer. Dit is de basismethode en het meest eenvoudig.")
    st.write("- **Resultaat:** Een klassieke pizza met een egale structuur. De smaak komt hier vooral uit de lange rijs- of fermentatietijd in de koelkast.")
    st.write("- **Tips voor het kneedproces:** Kneed eerst de bloem, het water en de gist. Als het deeg een egale consistentie heeft, voeg dan in de laatste minuten van het kneden de gist toe.")
    st.divider()
    st.write("**3. Wat is biga?**")
    st.write("Biga is een 'droog' voordeeg dat je ongeveer 24 uur van tevoren maakt. Pas daarna meng je het met de rest van de ingrediënten.")
    st.write("- **Meer aroma:** Diepere, complexere smaken (notig en licht zurig).")
    st.write("- **Superieure structuur:** Een veel luchtigere en krokantere rand (*cornicione*) met grotere luchtbellen.")
    st.write("- **Verteerbaarheid:** De enzymen hebben meer tijd om het zetmeel en de gluten af te breken.")
    st.divider()
    st.write("**4. De juiste bloem (Tipo 00 & W-waarde):**")
    st.write("Voor een echte Napolitaanse pizza is **Tipo 00 bloem** vereist. Dit is de zuiverste maling voor een elastisch en stretchbaar deeg. Het kan bovendien meer water opnemen, zonder dat het plakkerig wordt.")
    st.write("De **W-waarde** (bakkracht) bepaalt hoe lang je deeg kan rijpen/fermenteren:")
    st.write("- **W260 - W300:** Ideaal voor rijstijden tussen de **24 en 48 uur**.")
    st.write("- **W320 - W400:** Nodig voor extreem lange rijstijden (**72+ uur**) of een zeer hoge hydratatie (70%+).")
    st.write("Een hogere W-waarde betekent een sterker 'skelet' dat de gassen langer kan vasthouden. Dit helpt met het bereiken van een luchtige korst. Gebruik je supermarktbloem (vaak W190)? Dan zal het deeg bij lange rijstijden slap worden en scheuren.")
    st.divider()
    st.write("**5. De ideale fermentatietijd:**")
    st.write("Hoewel je na 8 uur rijstijd al een pizza kunt bakken, adviseren wij **minimaal 24 uur** (en idealiter 48 uur of langer) totale rijstijd. Tijd is een ingrediënt: het zorgt ervoor dat het deeg lichter op de maag ligt en de gluten optimaal ontspannen voor het stretchen. Bij een korte rijstijd <24 uur, heb je meer kans dat het deeg scheurt.")
    st.divider()
    st.write("**6. De Kickstart:**")
    st.write("- **Direct Deeg:** Laat het deeg na het kneden 1 uur op kamertemperatuur rusten voordat het de koelkast in gaat. Dit zorgt ervoor dat het gist geactiveerd wordt.")
    st.write("- **Biga:** Laat de Biga (Stap 1) 1 tot 2 uur op kamertemperatuur staan. Na het mixen (Stap 2) kan het deeg direct de koelkast in.")
    st.divider()
    st.write("**7. Windowpane Test:**")
    st.write("Een lange fermentatie maakt het deeg elastisch en stretchbaar. Dat heb je nodig om het pizzadeeg goed te kunnen vormen. Je kunt je deeg testen: trek het zo dun uit dat je er bijna doorheen kunt kijken zonder dat het scheurt.")
    st.divider()
    st.write("**8. Suiker & Gist:**")
    st.write("Gebruik je suiker (aanbevolen onder 300°C)? Dit helpt vooral bij de kleuring. Het effect op de rijskracht is bij percentages onder de 3% verwaarloosbaar in relatie tot de invloed van tijd en temperatuur.")
    st.divider()
    st.write("**9. Deegtemperatuur & Techniek:**")
    st.write("- **Eindtemperatuur:** Probeer je deeg na het kneden rond de **23°C** te krijgen. Is je keuken warm? Gebruik dan ijswater.")
    st.write("- **Bulkfermentatie:** Het makkelijkste is om deeg in bulk (als één geheel in een afgesloten bak) in de koelkast te laten fermenteren/rijpen. Haal dit er een halfuurtje voor het opbollen uit.")
    st.write("- **Opbollen:** Maak je bollen 4-6 uur voor het bakken en laat ze dan op kamertemperatuur komen in een afgesloten bak (anders drogen ze uit). Zo heeft het glutennetwerk tijd om te ontspannen, wat het stretchen makkelijker maakt.")
    st.write("- **Stretchen:** Stretchen is de techniek waarbij je een deegbol met de hand uitduwt tot een ronde pizzabodem. Werk altijd met deeg op kamertemperatuur. Koud deeg is te stug en zal scheuren.")

# --- INPUTS ---
st.header("📦 Basisinstellingen")
aantal = st.number_input("Aantal deegballen", min_value=1, value=6)
gewicht = st.number_input("Gewicht per bol (gram)", min_value=100, value=250)
hydro_totaal = st.slider("Hydratatie (%)", 50, 80, 67)
zout_perc = st.slider("Zout (%)", 1.0, 4.0, 2.5, 0.1)
suiker_perc = st.slider("Suiker (%)", 0.0, 3.0, 0.0, 0.5)
olijfolie_perc = st.slider("Olijfolie (%)", 0.0, 5.0, 0.0, 0.5)
waste_perc = st.number_input("Waste factor (% extra deeg)", 0, 10, 2)
oven_temp = st.number_input("Oventemperatuur (°C)", 150, 550, 480)

st.header("🧪 Methode & Gist")
methode = st.radio("Kies Methode", ["Direct deeg", "Biga"])
gist_type = st.radio("Type gist", ["Instant (IDY)", "Vers"])

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
    tijd_biga_rt = st.number_input("Uren Biga op kamertemperatuur (Kickstart)", 0, 24, 1)
    
    st.subheader("Fase 2: Na het mixen")
    tijd_deeg_ct = st.number_input("Uren deeg in koelkast", 0, 72, 18)
    tijd_deeg_rt = st.number_input("Uren deeg op kamertemperatuur", 0, 24, 6)
    
    totale_tijd_ct = tijd_biga_ct + tijd_deeg_ct
    totale_tijd_rt = tijd_biga_rt + tijd_deeg_rt
else:
    st.subheader("Planning direct deeg")
    totale_tijd_ct = st.number_input("Totaal uren in koelkast", 0, 100, 24)
    totale_tijd_rt = st.number_input("Totaal uren op kamertemperatuur", 0, 48, 6)
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
    st.error(f"⚠️ **Waarschuwing:** Je totale rijstijd is slechts {totale_uren} uur. Wij adviseren minimaal 24 uur voor optimale smaak en verteerbaarheid (zie Expert-tips).")
    
# Waarschuwing voor W-waarde op basis van tijd
if totale_uren > 48:
    st.warning(f"⚠️ **Bloemadvies:** Voor een totale rijstijd van {totale_uren} uur heb je een sterke bloem nodig (minimaal W320).")
elif totale_uren >= 24:
    st.info("💡 **Bloemadvies:** Voor deze rijstijd is een medium-sterke bloem (W260 - W300) ideaal.")
    
# Contextuele adviezen
if oven_temp >= 450:
    if hydro_totaal < 65:
        st.warning("⚠️ **Hitte-advies:** Bij 450°C+ is 67-70% water aanbevolen om uitdroging te voorkomen.")
    if suiker_perc > 0:
        st.error("⚠️ **Suikerwaarschuwing:** Bij 450°C+ verbrandt suiker te snel. Laat suiker liever weg.")
    if olijfolie_perc > 0:
        st.warning("⚠️ **Olietip:** Olie kan gaan roken bij 450°C+. Wees zeer matig en laat liever weg.")
elif oven_temp < 300:
    if hydro_totaal > 64:
        st.warning("⚠️ **Bodemtip:** Bij lage temp kan >64% water zorgen voor een zompige bodem.")
    if suiker_perc == 0:
        st.info("💡 **Bruining:** Voeg 1% suiker toe voor een mooiere kleur in een huishoudoven.")

# Recept Weergave
col_r1, col_r2 = st.columns(2)
if methode == "Biga":
    bloem_biga = bloem_totaal * (biga_perc / 100)
    water_biga = bloem_biga * 0.45
    with col_r1:
        st.subheader("Stap 1: De Biga (voordeeg)")
        st.write(f"**Bloem:** {bloem_biga:.0f}g")
        st.write(f"**Water:** {water_biga:.0f}g (45%)")
        st.write(f"**Gist ({gist_type}):** {gist_totaal:.2f}g")
    with col_r2:
        st.subheader("Stap 2: Hoofddeeg-mix (totaal)")
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

# --- VOLLEDIG KOPIEERBLOK ONDERAAN ---
st.divider()
st.subheader("📲 Recept kopiëren")

# We berekenen de waarden hier ter plekke zodat de tekst altijd klopt
if methode == "Biga":
    # Berekening voor de tekst
    b_biga = bloem_totaal * 0.5
    w_biga = b_biga * 0.45
    b_rest = bloem_totaal - b_biga
    w_rest = water_totaal - w_biga
    
    export_tekst = f"""🍕 PIZZA RECEPT (BIGA)
-----------------------------------------
Aantal: {aantal} bollen van {gewicht}g
Hydratatie: {hydro_totaal}%
Totaal rijstijd: {totale_uren} uur

STAP 1 (De Biga):
• Bloem: {b_biga:.0f}g
• Water: {w_biga:.0f}g
• Gist: {gist_totaal:.2f}g (Alles)
• Planning: {tijd_biga_ct}u koelkast / {tijd_biga_rt}u kamer

STAP 2 (Het Deeg):
• Restant Bloem: {b_rest:.0f}g
• Restant Water: {w_rest:.0f}g
• Zout: {zout_totaal:.1f}g
• Planning: {tijd_deeg_ct}u koelkast / {tijd_deeg_rt}u kamer
-----------------------------------------"""
else:
    export_tekst = f"""🍕 PIZZA RECEPT (DIRECT)
-----------------------------------------
Aantal: {aantal} bollen van {gewicht}g
Hydratatie: {hydro_totaal}%
Totaal rijstijd: {totale_uren} uur

INGREDIËNTEN:
• Bloem: {bloem_totaal:.0f}g
• Water: {water_totaal:.0f}g
• Zout: {zout_totaal:.1f}g
• Gist: {gist_totaal:.2f}g

PLANNING:
• Koelkast: {totale_tijd_ct} uur
• Kamertemperatuur: {totale_tijd_rt} uur
-----------------------------------------"""

# Toon de tekst in een kopieerbaar blok
st.code(export_tekst, language="text")
st.caption("Klik op het icoontje rechtsboven om het recept te kopiëren.")
