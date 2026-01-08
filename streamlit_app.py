import streamlit as st

st.set_page_config(page_title="Pizzaformule.nl dé pizzacalculator met alle denkbare variabelen voor de ultieme pizza", page_icon="🍕", layout="centered")

st.title("🍕 Pizzaformule.nl")
st.markdown("De ultieme tool met alle denkbare variabelen voor direct deeg en biga-recepten, volgens de (neo-)Napolitaanse traditie.")

# EXPERTTIPS SECTIE
with st.expander("🎓 Expert-tips & Theorie"):
    st.write("**🍕 De Napolitaanse Pizza**")
    st.write("Een Napolitaanse pizza is de wereldberoemde klassieker uit Napels, herkenbaar aan een zeer luchtige, soepele rand en een dunne, zachte bodem. De traditionele basis bestaat uit slechts 4 ingrediënten: bloem (Tipo 00), water, zout en gist. "
        "Er wordt *geen* olie of suiker toegevoegd. Het deeg rijpt lang en wordt kort (60-90 sec) "
        "op extreem hoge temperatuur (450°C+) gebakken voor de kenmerkende luchtige, gevlekte rand.")
    st.write("Bij temperaturen onder de 350°C (zoals in een reguliere huishoud-oven) duurt het bakken langer (5-8 min). "
        "Voeg dan olijfolie toe voor een minder taaie korst en suiker om de bruining te versnellen. "
        "Zonder deze toevoegingen droogt het deeg uit voordat het mooi gekleurd is.")
    st.divider()
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
    st.write("**7. Suiker & Gist:**")
    st.write("Gebruik je suiker (aanbevolen onder 300°C)? Dit helpt vooral bij de kleuring. Het effect op de rijskracht is bij suikerpercentages onder de 3% verwaarloosbaar in relatie tot de invloed van tijd en temperatuur.")
    st.divider()
    st.write("**8. Deegtemperatuur & Techniek:**")
    st.write("- **Eindtemperatuur:** Probeer je deeg na het kneden rond de **23°C** te krijgen. Als je keuken kouder is, dan zorgt de wrijving van je keukenmachine met het deeg voor temperatuurstijging. Is je keuken warm? Probeer dan ijswater, of laat een deel van je water bestaan uit ijsklontjes.")
    st.write("- **Bulkfermentatie:** Het makkelijkste is om deeg in bulk (als één geheel in een afgesloten bak) in de koelkast te laten fermenteren/rijpen. Haal dit er een halfuurtje voor het opbollen uit.")
    st.write("- **Opbollen:** Maak je bollen 4-6 uur voor het bakken en laat ze dan op kamertemperatuur komen in een afgesloten bak (anders drogen ze uit). Zo heeft het glutennetwerk tijd om te ontspannen, wat het stretchen makkelijker maakt.")
    st.write("- **Stretchen:** Stretchen is de techniek waarbij je een deegbol met de hand uitduwt tot een ronde pizzabodem. Werk altijd met deeg op kamertemperatuur. Koud deeg is te stug en zal scheuren.")
    st.write("- **Waste:** Tijdens het proces van deeg maken, blijft er altijd wel iets aan je handen of de kom plakken. Om te voorkomen dat je minder deeg hebt voor je bollen dan de bedoeling, kun je hiervoor corrigeren. Hanteer tussen de 1 en 3% waste.")

# --- INPUTS ---
st.header("📦 Basisinstellingen")
aantal = st.number_input("Aantal deegballen", min_value=1, value=6,
help="Voer hier het totaal aantal pizza's in dat je wilt gaan bakken.")
gewicht = st.number_input("Gewicht per bol (gram)", min_value=100, value=250,
help="Een standaard Napolitaanse pizza (30cm) is 250-280 gram. Voor een kleine pizza (20-25cm) gebruik je 200 gram.")
hydro_totaal = st.slider("Hydratatie (%)", 50, 80, 65,
help="De hoeveelheid water t.o.v. de bloem. 60-65% is makkelijk hanteerbaar. >70% is voor gevorderden en vereist sterke bloem. Zie ook de Expert-tips voor meer informatie over de relatie tussen hydratatie en baktemperatuur.")
zout_perc = st.slider("Zout (%)", 1.0, 4.0, 2.5, 0.1,
help="Zout geeft smaak en verstevigt de gluten. Gebruikelijk is 2.5% tot 3% van het bloemgewicht.")
suiker_perc = st.slider("Suiker (%)", 0.0, 3.0, 0.0, 0.5,
help="Suiker helpt bij de kleuring van de korst, vooral in ovens die niet warmer worden dan 300°C. Advies is om het sowieso niet te gebruiken bij temperaturen >400°C.")
olijfolie_perc = st.slider("Olijfolie (%)", 0.0, 5.0, 0.0, 0.5,
help="Olie maakt het deeg soepeler en de korst krokanter bij lagere temperaturen (huishoudoven). Gebruik geen olie bij temperaturen >400°C.")
waste_perc = st.number_input("Waste factor (% extra deeg)", 0, 10, 2,
help="Extra marge voor deeg dat achterblijft in de kom of aan de handen. 2% is meestal voldoende.")
oven_temp = st.number_input("Oventemperatuur (°C)", 150, 550, 480,
help="Heb je een huishoud-oven? Hanteer een zo hoog mogelijke temperatuur. De meeste huishoud-ovens hebben een maximale temperatuur van 300°C. Heb je een pizza-oven? Bak je pizza tussen de 450 en 500 graden.")

st.header("🧪 Methode & Gist")
methode = st.radio("Kies Methode", ["Direct deeg", "Biga"],
help="Lees de Expert-tips bovenaan deze pagina voor meer informatie over de verschillen.")
gist_type = st.radio("Type gist", ["Instant (IDY)", "Vers"],
help="Instant gist zijn de droge korrels. Verse gist is het blokje uit de koeling (gebruik hier 3x zoveel van).")

# --- RIJSSCHEMA ---
st.header("🕒 Planning & Temperatuur")
col1, col2 = st.columns(2)
with col1:
    temp_ct = st.number_input("Koelkasttemperatuur (°C)", 2, 10, 4)
with col2:
    temp_rt = st.number_input("Kamertemperatuur (°C)", 15, 30, 20)

if methode == "Biga":
    biga_perc = st.slider("Biga Percentage (%)", 10, 100, 50,
    help="Dit is het deel van de totale bloem dat in de Biga gaat. \n\n"
         "30-50%: Ideaal voor een gebalanceerde smaak en goede hanteerbaarheid. De meeste keukenmachines kunnen 50% biga wel aan, mits je het in blokjes snijdt of oplost in het water van stap 2. "
         "100% (Full Biga): Zorgt voor maximale luchtigheid en aroma, maar is lastiger te kneden in stap 2.")
    st.subheader("Fase 1: De Biga")
    tijd_biga_ct = st.number_input("Uren Biga in koelkast", 0, 72, 24,
    help="De tijd dat de Biga koud rijpt om enzymatische processen (smaak) te stimuleren. Advies: 24 uur.")
    tijd_biga_rt = st.number_input("Uren Biga op kamertemperatuur (Kickstart)", 0, 24, 1,
    help="Om het gist een kickstart te geven kun je het deeg op kamertemperatuur laten staan, voordat je het in de koelkast doet. Advies: 1 uur.")
    
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

# --- 4. REKENKERN ---
massa_per_bol = gewicht * (1 + waste_perc/100)
totale_massa = aantal * massa_per_bol

# Berekening bloem (basis = 100%)
factor = 1 + (hydro_totaal/100) + (zout_perc/100) + (olijfolie_perc/100) + (suiker_perc/100)
bloem_totaal = totale_massa / factor

water_totaal = bloem_totaal * (hydro_totaal/100)
zout_totaal = bloem_totaal * (zout_perc/100)
olijfolie_totaal = bloem_totaal * (olijfolie_perc/100)
suiker_totaal = bloem_totaal * (suiker_perc/100)

# --- VERBETERDE GIST BEREKENING (Tijd + Temperatuur) ---

# 1. Gemiddelde temperatuur berekenen over de hele periode
tijd_totaal = totale_tijd_ct + totale_tijd_rt
if tijd_totaal > 0:
    temp_gemiddeld = ((totale_tijd_ct * temp_ct) + (totale_tijd_rt * temp_rt)) / tijd_totaal
else:
    temp_gemiddeld = temp_rt

# 2. De Gistformule (Finetuning voor jouw 2,5g resultaat)
# We verlagen de basis_factor naar 0.07
basis_factor = 0.07 

# We verhogen de exponent naar 1.13. 
# Hierdoor wordt de gist in de koelkast nóg meer afgeremd in de berekening.
temp_diff = temp_gemiddeld - 20
gist_factor = (basis_factor / (tijd_totaal / 24)) * (1.13 ** -temp_diff)

# 3. Veiligheidsmarges (voor Instant Dry Yeast)
if gist_factor < 0.04: gist_factor = 0.04 
if gist_factor > 1.0: gist_factor = 1.0

# 4. Correctie voor gist-type (Vers = 3x IDY)
if gist_type == "Vers":
    gist_factor *= 3

gist_totaal = (bloem_totaal / 100) * gist_factor
# -------------------------------------------
# -------------------------------------------

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
if oven_temp >= 400:
    if hydro_totaal < 65:
        st.warning("⚠️ **Hitte-advies:** Bij 400°C+ is 67-70% water aanbevolen om uitdroging te voorkomen.")
    if suiker_perc > 0:
        st.error("⚠️ **Suikerwaarschuwing:** Bij 400°C+ verbrandt suiker te snel. Laat suiker liever weg.")
    if olijfolie_perc > 0:
        st.warning("⚠️ **Olietip:** Olie kan gaan roken bij 400°C+. Wees zeer matig en laat liever weg.")
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
        st.subheader("Stap 1: De biga (voordeeg)")
        st.write(f"• **Bloem:** {bloem_biga:.0f}g")
        st.write(f"• **Water:** {water_biga:.0f}g (45%)")
        st.write(f"• **Gist ({gist_type}):** {gist_totaal:.2f}g")
    with col_r2:
        st.subheader("Stap 2: Het deeg (totaal)")
        st.write(f"• **De biga uit stap 1, na fermentatie/rijping**")
        st.write(f"• **Restant bloem:** {bloem_totaal - bloem_biga:.0f}g")
        st.write(f"• **Extra water:** {water_totaal - water_biga:.0f}g")
        st.write(f"• **Zout:** {zout_totaal:.1f}g")
        if suiker_totaal > 0: st.write(f"• **Suiker:** {suiker_totaal:.1f}g")
        if olijfolie_totaal > 0: st.write(f"• **Olijfolie:** {olijfolie_totaal:.1f}g")
else:
    with col_r1:
        st.write(f"• **Bloem:** {bloem_totaal:.0f}g")
        st.write(f"• **Water:** {water_totaal:.0f}g")
        st.write(f"• **Zout:** {zout_totaal:.1f}g")
    with col_r2:
        st.write(f"• **Gist ({gist_type}):** {gist_totaal:.2f}g")
        if suiker_totaal > 0: st.write(f"• **Suiker:** {suiker_totaal:.1f}g")
        if olijfolie_totaal > 0: st.write(f"• **Olijfolie:** {olijfolie_totaal:.1f}g")

st.info(f"Totaal deeggewicht: {totale_massa:.0f}g (incl. {waste_perc}% waste)")

# --- UITKLAPBAAR KOPIEERBLOK ONDERAAN ---
with st.expander("📲 Klik hier om het recept eenvoudig te kopiëren naar bijv. Whatsapp of een notitieblok"):
    
    # We berekenen de waarden hier ter plekke zodat de tekst altijd klopt
    if methode == "Biga":
        b_biga = bloem_totaal * (biga_perc / 100)
        w_biga = b_biga * 0.45
        b_rest = bloem_totaal - b_biga
        w_rest = water_totaal - w_biga
        
        export_tekst = f"""🍕 PIZZA RECEPT (BIGA)
-----------------------------------------
Aantal: {aantal} bollen van {gewicht}g
Hydratatie: {hydro_totaal}%
Totaal rijstijd: {totale_uren} uur

STAP 1 (De biga):
• Bloem: {b_biga:.0f}g
• Water: {w_biga:.0f}g
• Gist: {gist_totaal:.2f}g (Alles)
• Planning: {tijd_biga_ct}u koelkast / {tijd_biga_rt}u kamer

STAP 2 (Het deeg):
• De biga (uit stap 1 na fermentatie/rijping)
• Restant Bloem: {b_rest:.0f}g
• Restant Water: {w_rest:.0f}g
• Zout: {zout_totaal:.1f}g
• Planning: {tijd_deeg_ct}u koelkast / {tijd_deeg_rt}u kamer
-----------------------------------------"""
    else:
        export_tekst = f"""🍕 PIZZA RECEPT (DIRECT DEEG)
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
