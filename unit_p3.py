S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Blood sample collection, haemoglobin, PCV and anaemia", imp=True, txt="""
**Blood collection (venepuncture):** verify patient identity, apply tourniquet for less than 1 minute, clean with alcohol and let it dry, use a sterile needle, label the tube at the bedside, fill to the mark, mix gently by inversion (do not shake), send promptly.
| Tube (cap) | Additive | Used for |
|---|---|---|
| Lavender | EDTA | CBC, ESR (EDTA), blood group |
| Blue | Sodium citrate 3.2% (blood : citrate = 9 : 1) | PT, APTT, ESR (Westergren, 4 : 1) |
| Green | Heparin | Some biochemistry, blood gases |
| Grey | Sodium fluoride | Blood glucose |
| Red / yellow | None or clot activator | Serum tests, cross-match |

**Haemoglobin (Hb):** oxygen-carrying pigment. Normal: men 13-17 g/dL, women 12-15 g/dL. Methods: **cyanmethaemoglobin (Drabkin) method - the recommended standard**; Sahli's acid haematin (simple, less accurate); automated analysers.
**PCV (haematocrit):** percentage of blood volume occupied by red cells. Men 40-50%, women 36-46%. Methods: Wintrobe tube, microhaematocrit (centrifuge). Raised in polycythaemia and dehydration; low in anaemia.
**Red cell indices:** MCV (size) 80-100 fL; MCH (Hb per cell) 27-32 pg; MCHC 32-36 g/dL.

**Anaemia:** Hb below normal - WHO cut-offs: men <13, non-pregnant women <12, pregnant women <11 g/dL.
| Type | MCV | Common causes |
|---|---|---|
| Microcytic hypochromic | Low | **Iron deficiency (commonest in India)**, thalassaemia |
| Normocytic | Normal | Acute blood loss, chronic disease, aplastic anaemia |
| Macrocytic | High | Vitamin B12 and folate deficiency |
Features: fatigue, pallor, breathlessness, palpitation, koilonychia (iron deficiency). Confirm with peripheral smear, reticulocyte count and serum ferritin.
""", dots=[(S + r'"Anaemia\n(low Hb)"->"Microcytic\n(MCV below 80)"->"Iron deficiency,\nthalassaemia";"Anaemia\n(low Hb)"->"Normocytic"->"Blood loss, chronic\ndisease, aplastic";'
                r'"Anaemia\n(low Hb)"->"Macrocytic\n(MCV above 100)"->"B12 or folate\ndeficiency"}', "Classification of anaemia by red cell size")],
     example="A 24-year-old woman with vegetarian diet and heavy periods has Hb 8 g/dL, MCV 68 fL, low ferritin: iron deficiency anaemia. The nurse collects an EDTA sample, teaches iron-rich foods and "
             "correct iron tablet use (with vitamin C, not with tea) and warns that stools turn black."),
dict(t="2. WBC count, differential count and platelet count", imp=True, txt="""
**Total leucocyte count (TLC):** 4,000-11,000 per microlitre. Counted in a **Neubauer chamber** after dilution with Turk's fluid, or by automated analyser.
**Differential count (DLC)** on a Leishman- or Giemsa-stained smear (mnemonic: *Never Let Monkeys Eat Bananas*):
| Cell | Normal % | Raised in |
|---|---|---|
| Neutrophils | 40-75 | Bacterial infection, inflammation, stress |
| Lymphocytes | 20-45 | Viral infection, TB, whooping cough |
| Monocytes | 2-10 | TB, recovery phase of infection |
| Eosinophils | 1-6 | **Allergy, asthma, parasitic infestation** |
| Basophils | 0-1 | Chronic myeloid leukaemia |
**Leucocytosis** = TLC above 11,000; **leucopenia** = below 4,000 (viral infections, typhoid, aplastic anaemia, chemotherapy). **Neutropenia** (neutrophils below 1,500) gives high infection risk - reverse isolation and strict hand hygiene. **Leukaemia:** very high or abnormal counts with immature cells (blasts); acute (ALL in children, AML in adults) vs chronic (CML, CLL).

**Platelet count:** 1.5-4 lakh per microlitre (150,000-400,000). Counted by automated analyser or Rees-Ecker fluid.
- **Thrombocytopenia:** dengue, ITP, leukaemia, chemotherapy, hypersplenism, DIC. Spontaneous bleeding risk below 20,000; surgery needs above 50,000.
- Thrombocytosis: after splenectomy, iron deficiency, myeloproliferative disease.
""", example="A child with fever, rash and a platelet fall from 2 lakh to 40,000 on day 4 has dengue; the nurse watches for bleeding gums, black stools and falling BP, avoids IM injections and NSAIDs, and encourages oral fluids. "
             "A patient on chemotherapy with a TLC of 1,200 and neutrophils of 400 is neutropenic and needs protective isolation."),
dict(t="3. Erythrocyte sedimentation rate (ESR)", imp=True, txt="""
**Definition:** the rate at which red cells settle in anticoagulated blood in one hour, reported in mm/hour.
**Westergren method (standard):** 4 volumes of blood + 1 volume of 3.8% sodium citrate; a 200 mm graduated tube held vertically at room temperature; read after **1 hour**. Wintrobe method uses a shorter 100 mm tube. Normal (Westergren): men up to 15 mm/hr, women up to 20 mm/hr.
**Principle:** red cells stack in **rouleaux** when plasma fibrinogen and globulins rise, and rouleaux sediment faster.
| Raised ESR | Lowered ESR |
|---|---|
| TB, infections, rheumatoid arthritis, malignancy, myeloma, pregnancy, anaemia, SLE | Polycythaemia, sickle cell disease, heart failure, very low fibrinogen |
**Sources of error:** tilted tube, air bubbles, delay beyond 2-4 hours, wrong blood-to-citrate ratio, vibration, high temperature.
**Significance:** non-specific screening test and useful to follow disease activity (TB, RA, temporal arteritis); a normal ESR does not exclude disease.
""", example="A 35-year-old with cough, night sweats and weight loss has an ESR of 80 mm/hr; the high, non-specific value pushes the doctor to look for TB with sputum AFB. "
             "After treatment the ESR falls, which helps to track response."),
dict(t="4. Coagulation tests: bleeding time, PT, APTT", imp=True, txt="""
**Haemostasis:** (1) vascular spasm, (2) **platelet plug**, (3) **coagulation** - fibrin clot, (4) later lysis.

**Bleeding time (BT):** measures platelet number and function. *Duke's method* (ear lobe puncture, blot every 30 seconds): 1-5 minutes. *Ivy's method* (forearm, BP cuff at 40 mmHg): 2-7 minutes. Prolonged in thrombocytopenia, platelet function defects, von Willebrand disease, aspirin use.

**Prothrombin time (PT):** tests the **extrinsic and common pathway** (factor VII, X, V, II, fibrinogen). Citrated plasma + thromboplastin + calcium; normal 11-16 seconds; reported as **INR** (normal 0.8-1.2). Prolonged in vitamin K deficiency, liver disease, **warfarin therapy** (target INR usually 2-3), DIC.
**APTT (activated partial thromboplastin time):** tests the **intrinsic and common pathway** (XII, XI, IX, VIII). Normal about 25-35 seconds. Prolonged in **haemophilia A (factor VIII) and B (factor IX)**, von Willebrand disease, **heparin therapy** (used to monitor heparin), DIC.
**Sample:** 3.2% sodium citrate tube filled exactly to the mark (9 : 1), mixed gently, tested within a few hours.

| Condition | Platelets | BT | PT | APTT |
|---|---|---|---|---|
| Immune thrombocytopenia (ITP) | Low | Prolonged | Normal | Normal |
| Haemophilia A / B | Normal | Normal | Normal | **Prolonged** |
| von Willebrand disease | Normal | Prolonged | Normal | Prolonged |
| Warfarin / vitamin K deficiency | Normal | Normal | **Prolonged** | Normal or mild |
| DIC | Low | Prolonged | Prolonged | Prolonged |
""", dots=[(S + r'"Intrinsic (APTT)\nXII, XI, IX, VIII"->"Common pathway\nX, V, prothrombin,\nfibrinogen";"Extrinsic (PT)\ntissue factor, VII"->"Common pathway\nX, V, prothrombin,\nfibrinogen";'
                r'"Common pathway\nX, V, prothrombin,\nfibrinogen"->"Fibrin clot"}', "Coagulation pathways and the tests that measure them")],
     example="A boy with knee swelling after minor injury has a normal PT and BT but a prolonged APTT: haemophilia A, confirmed by factor VIII assay. A patient on warfarin has INR 5.2, well above target; "
             "the nurse withholds the dose, informs the doctor and checks for bleeding."),
dict(t="5. Blood chemistry", imp=False, txt="""
Tests on serum or plasma (plain or gel tube; fluoride tube for glucose). Fasting for 8-12 hours is needed for glucose and lipids.
| Test | Normal (adult) | Clinical significance |
|---|---|---|
| Fasting glucose | 70-100 mg/dL | 126 or more = diabetes; low = hypoglycaemia |
| Post-prandial (2 h) | Below 140 mg/dL | 200 or more on OGTT = diabetes |
| HbA1c | Below 5.7% | 6.5% or more = diabetes; reflects 3 months |
| Urea / creatinine | Urea 15-40; creatinine 0.6-1.2 mg/dL | Raised in renal failure (creatinine more specific) |
| Uric acid | 3.5-7.2 mg/dL | Raised in gout |
| Bilirubin (total) | 0.2-1.2 mg/dL | Raised in jaundice |
| ALT / AST | Up to about 40 U/L | Raised in hepatitis, liver injury |
| ALP | 40-130 U/L | Raised in obstructive jaundice, bone disease |
| Albumin | 3.5-5.0 g/dL | Low in cirrhosis, nephrotic syndrome |
| Sodium / potassium | 135-145 / 3.5-5.0 mmol/L | Dangerous imbalance: arrhythmia, seizures |
| Calcium | 8.5-10.5 mg/dL | Low: tetany; high: stones, bone pain |
| Total cholesterol / LDL / TG | Below 200 / below 100 / below 150 mg/dL | Raised in heart-disease risk; HDL should be above 40 (men), 50 (women) |
| Troponin I / T | Undetectable | Raised in myocardial infarction |
| Amylase / lipase | Amylase 30-110 U/L | Raised in acute pancreatitis |
**Nursing:** correct fasting instructions, no IV drip in the sampling arm, avoid haemolysis (raises potassium falsely), label carefully.
""", example="A patient's report reads: ALT 620, AST 540, bilirubin 6 mg/dL, ALP normal. This pattern suggests hepatocellular injury such as viral hepatitis; a rise mainly in ALP and bilirubin would instead suggest biliary obstruction."),
dict(t="6. Blood bank: grouping, cross-matching, donors and components", imp=True, txt="""
**ABO system (Landsteiner):** red cells carry A and/or B antigens, and plasma has the opposite antibodies.
| Group | Antigen on red cells | Antibody in plasma |
|---|---|---|
| A | A | Anti-B |
| B | B | Anti-A |
| AB | A and B | None (**universal recipient**) |
| O | None | Anti-A and anti-B (**universal donor** for red cells) |
**Rh system:** presence of D antigen = Rh positive; most people are Rh positive. Rh-negative women carrying an Rh-positive baby need anti-D immunoglobulin to prevent haemolytic disease of the newborn.
**Blood grouping:** *forward (cell) grouping* - patient red cells mixed with anti-A, anti-B, anti-D; *reverse (serum) grouping* - patient serum mixed with known A and B cells. Both must agree.
**Cross-matching:** *major* = donor red cells + recipient serum (checks recipient antibodies against donor cells; must be done before every transfusion); *minor* = donor serum + recipient cells. Methods: immediate spin, incubation, antihuman globulin (Coombs) phase. Absence of agglutination = compatible.

**Donor selection (voluntary donation):** age 18-65, weight at least 45 kg, Hb at least 12.5 g/dL, normal pulse and BP, no fever or recent illness; interval 3 months for men, 4 months for women. Volume 350-450 mL in CPDA-1 bag. Every unit is screened for **HIV, hepatitis B, hepatitis C, syphilis and malaria**.

**Storage:** whole blood 2-6 degrees C, up to 35 days (CPDA-1). Never keep blood in an ordinary fridge or warm it in hot water.
| Component | Storage | Use |
|---|---|---|
| Packed red cells | 2-6 C, 35 days | Anaemia, blood loss |
| Platelet concentrate | 20-24 C with gentle agitation, up to 5 days | Thrombocytopenia, bleeding |
| Fresh frozen plasma | -30 C or below, 1 year | Clotting factor deficiencies, liver disease, DIC |
| Cryoprecipitate | -30 C or below | Haemophilia A, von Willebrand, fibrinogen lack |
| Albumin | Room temp / cool | Hypoalbuminaemia, burns |
""", dots=[(S + r'"Donor O"->"Recipient O";"Donor O"->"Recipient A";"Donor O"->"Recipient B";"Donor O"->"Recipient AB";"Donor A"->"Recipient A";"Donor A"->"Recipient AB";"Donor B"->"Recipient B";"Donor B"->"Recipient AB";"Donor AB"->"Recipient AB"}', "Red cell compatibility: arrows go from donor group to recipient group")],
     example="An accident victim needs blood urgently and the group is unknown: group O Rh-negative red cells are given as emergency uncrossmatched blood while grouping is done. "
             "A patient with a platelet count of 8,000 and gum bleeding receives a platelet concentrate, never refrigerated."),
dict(t="7. Plasmapheresis and transfusion reactions", imp=True, txt="""
**Plasmapheresis:** blood is drawn, plasma is separated from cells by centrifuge or filter, the cells are returned with replacement fluid (albumin or plasma). *Therapeutic* uses: Guillain-Barre syndrome, myasthenia gravis, thrombotic thrombocytopenic purpura, hyperviscosity, Goodpasture syndrome, poisoning. *Donor* apheresis (plateletpheresis) collects platelets and returns the rest. Watch for hypotension, citrate reaction (tingling, cramps from low calcium), infection.

**Transfusion reactions**
| Reaction | Cause | Features | Action |
|---|---|---|---|
| **Acute haemolytic** | ABO mismatch (usually a labelling or identification error) | Fever, chills, back pain, red urine, hypotension, DIC | Stop at once; treat shock and renal protection |
| **Febrile non-haemolytic** (commonest) | Antibodies to donor white cells | Fever and chills within hours | Stop, antipyretic; leucodepleted blood later |
| Allergic | Plasma proteins | Urticaria, itching | Antihistamine; may resume slowly |
| Anaphylactic | IgA deficiency | Wheeze, shock | Stop, adrenaline |
| TRALI | Donor antibodies, within 6 hours | Sudden breathlessness, pulmonary oedema, normal heart | Oxygen, ventilation |
| TACO (circulatory overload) | Too much, too fast, in elderly or cardiac | Cough, raised JVP, crepitations | Sit up, diuretic, slow rate |
| Bacterial contamination | Infected unit | High fever, septic shock | Stop, cultures, antibiotics |
| Delayed haemolytic | Antibodies formed later | Fall in Hb, jaundice after days | Investigate |
Massive transfusion: hypothermia, hyperkalaemia, low calcium (citrate).

**Nursing responsibilities**
1. Two-person check of patient name, ID, blood group and bag number against the request form.
2. Baseline temperature, pulse, BP, respiration; use a set with a filter; use only normal saline with blood, no drugs or dextrose.
3. Start slowly (first 15 minutes, about 2 mL per minute, stay with the patient); repeat vitals at 15 minutes and hourly.
4. Complete each unit within 4 hours of leaving the blood bank.
5. **If a reaction is suspected: stop the transfusion, keep the vein open with saline, recheck identity, inform the doctor and the blood bank, and return the bag and a fresh sample.** Record everything.
""", dots=[(S + r'"Reaction suspected"->"STOP transfusion"->"Keep vein open\nwith normal saline"->"Check vitals, recheck\npatient and bag ID"->"Inform doctor\nand blood bank"->"Return bag and\nsend samples"}', "Steps when a transfusion reaction is suspected")],
     example="Ten minutes into a unit of red cells, a patient develops chills, back pain and dark urine. The nurse stops the transfusion immediately, keeps the vein open with normal saline, checks vitals and identity, "
             "calls the doctor and blood bank and sends the bag with a new sample: suspected acute haemolytic reaction."),
]

P3 = dict(
    id="P3", subject="Pathology", title="Unit III - Haematological tests", hrs=7, topics=TOPICS,
    mcq=[
        ("Recommended standard method for haemoglobin estimation", ["Sahli's acid haematin", "Cyanmethaemoglobin method", "Tallqvist scale", "Wintrobe method"], 1),
        ("Anticoagulant used for PT and APTT samples", ["EDTA", "Sodium citrate", "Sodium fluoride", "None"], 1),
        ("Normal MCV of red cells", ["50-70 fL", "80-100 fL", "100-120 fL", "120-140 fL"], 1),
        ("Cell type raised in allergy and parasitic infestation", ["Neutrophils", "Eosinophils", "Basophils", "Monocytes"], 1),
        ("Westergren ESR is read after", ["30 minutes", "1 hour", "2 hours", "24 hours"], 1),
        ("PT / INR is used to monitor therapy with", ["Heparin", "Warfarin", "Aspirin", "Insulin"], 1),
        ("Universal donor of red cells", ["AB positive", "O negative", "A positive", "B negative"], 1),
        ("Platelet concentrates are stored at", ["2-6 C without agitation", "20-24 C with gentle agitation", "-30 C", "37 C"], 1),
        ("Commonest transfusion reaction", ["Acute haemolytic", "Febrile non-haemolytic", "TRALI", "Anaphylactic"], 1),
        ("First nursing action if a transfusion reaction is suspected",
         ["Slow the drip and continue", "Stop the transfusion and keep the vein open with saline", "Give more fluid quickly", "Wait 30 minutes and observe"], 1),
    ],
    long=[
        ("Define anaemia. Classify it and describe the laboratory investigations. (PYQ pattern)",
         "WHO Hb cut-offs; microcytic, normocytic, macrocytic with causes; Hb, PCV, indices, peripheral smear, reticulocytes, ferritin."),
        ("Define ESR. Describe the Westergren method, factors affecting it and clinical significance. (PYQ pattern)",
         "Definition; 4:1 citrate, 200 mm tube, 1 hour; rouleaux; raised and lowered conditions; errors; non-specific."),
        ("Describe bleeding time, PT and APTT: principle, normal values and clinical use. (PYQ pattern)",
         "Duke and Ivy; extrinsic vs intrinsic pathway; INR and warfarin; APTT and heparin/haemophilia; comparison table."),
        ("Describe ABO and Rh blood groups, grouping and cross-matching. (Important topic)",
         "Antigens and antibodies table; forward and reverse grouping; major and minor cross-match; compatibility; Rh and anti-D."),
        ("Enumerate blood components and describe transfusion reactions with nursing management. (Important topic)",
         "Components with storage and use; reaction table; stop, keep vein open, inform, return bag; monitoring schedule."),
    ],
    imp=["Anaemia and red cell indices", "DLC and platelet count", "ESR (Westergren)", "BT, PT, APTT", "Blood grouping and cross-match", "Blood components and transfusion reactions"],
)