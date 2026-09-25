S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Cerebrospinal fluid (CSF) and lumbar puncture", imp=True, txt="""
**CSF** is formed by the choroid plexus (about 500 mL/day; 150 mL present in adults) and cushions the brain and cord.

**Lumbar puncture (LP)**
- *Indications:* suspected meningitis, encephalitis, subarachnoid haemorrhage, demyelinating disease, cancer cell study, spinal anaesthesia.
- *Contraindications:* **raised intracranial pressure from a mass** (risk of coning; scan first), infection at the puncture site, bleeding disorder or very low platelets.
- *Site:* **L3-L4 or L4-L5** (below the end of the spinal cord).
- *Procedure:* explain and take consent; **lateral position, back at the edge of bed, knees to chest, chin on chest**; strict asepsis; local anaesthetic; needle with stylet through the interspace; measure **opening pressure** (normal 70-180 mm CSF), collect **3 sterile tubes** - tube 1 chemistry and serology, tube 2 microbiology, tube 3 cell count (tube 4 for cytology if needed); apply plaster.
- *Nursing care after LP:* lie flat for the period ordered (commonly 1-4 hours), encourage fluids, watch for **post-LP headache** (relieved by lying flat), leakage or bleeding at the site, fever, back pain, leg weakness or numbness; record neurological observations.

**Normal CSF:** clear and colourless; cells 0-5 lymphocytes per microlitre; protein 15-45 mg/dL; glucose 50-80 mg/dL (about two-thirds of blood glucose); chloride 118-132 mmol/L.
| Condition | Appearance | Cells | Protein | Glucose |
|---|---|---|---|---|
| Bacterial meningitis | Turbid, pus | Neutrophils, many | High | **Low** |
| Viral meningitis | Clear | Lymphocytes | Normal / slightly high | Normal |
| TB meningitis | Clear or cobweb clot | Lymphocytes | High | Low |
| Subarachnoid haemorrhage | Bloody, then **xanthochromic** (yellow) after 2-4 hours | Red cells | High | Normal |
Tests: cell count, Gram stain and culture, **Ziehl-Neelsen** (TB), **India ink** (cryptococcus), PCR, biochemistry.
""", dots=[(S + r'"Explain, consent,\nposition (lateral,\nknees to chest)"->"Asepsis; needle at\nL3-L4 or L4-L5"->"Collect 3 tubes:\nchemistry, microbiology,\ncell count"->"Label, send\nat once"->"Post-LP: lie flat,\nfluids, watch headache"}', "Lumbar puncture and CSF collection")],
     example="A 5-year-old with fever, vomiting and neck stiffness needs an LP: the nurse positions the child curled on the side, holds gently, hands over the tubes in order, labels them at the bedside and sends them immediately. "
             "A cloudy CSF with many neutrophils, high protein and low glucose confirms bacterial meningitis."),
dict(t="2. Other body cavity fluids, sputum and wound discharge", imp=True, txt="""
**Body cavity fluids** are collected by a doctor by aspiration: **pleural** (thoracocentesis), **peritoneal/ascitic** (paracentesis), **pericardial** (pericardiocentesis), **synovial** (arthrocentesis). The nurse prepares the trolley, positions and consents the patient, assists aseptically, labels tubes (plain, EDTA for cells, heparin, sterile for culture, blood-culture bottle) and monitors vitals afterwards.
- *Naked-eye:* clear/straw (transudate), turbid (infection), bloody (trauma, tumour, TB), milky (chyle), pus (empyema).
- *Tests:* protein, glucose, LDH, cell count and differential, Gram/ZN stain, culture, cytology, amylase, ADA (adenosine deaminase for TB).
- **Exudate vs transudate** (pleural fluid, Light's criteria): exudate if fluid/serum protein above 0.5, fluid/serum LDH above 0.6, or fluid LDH above two-thirds of upper serum limit.
- *Ascitic fluid:* **SAAG** (serum minus ascitic albumin) 1.1 g/dL or more = portal hypertension (cirrhosis); **neutrophils 250 per microlitre or more = spontaneous bacterial peritonitis**.
- *Synovial fluid:* gout - needle-shaped, negatively birefringent **urate crystals**; pseudogout - rhomboid calcium pyrophosphate crystals; septic arthritis - turbid fluid, many neutrophils.

**Sputum**
- *Collection:* **early-morning specimen** from a deep cough after rinsing the mouth (not saliva), in a sterile wide-mouth screw-cap container, before antibiotics; sit upright, well ventilated area for the nurse (mask or N95).
- *For TB (AFB smear):* two samples - one **spot** sample at first visit and one **early-morning** sample next day; **Ziehl-Neelsen stain** shows red acid-fast bacilli; CBNAAT for confirmation and rifampicin resistance.
- *Other tests:* Gram stain and culture with sensitivity, cytology for malignant cells, eosinophils in asthma. A good specimen shows many pus cells and few epithelial cells.

**Wound discharge:** clean the surface with sterile saline first; take pus or fluid from the **depth or base of the wound** with a sterile swab or aspirate; label the site; send immediately (anaerobic transport medium for deep wounds). Tests: Gram stain, aerobic and anaerobic culture with sensitivity; collect before antibiotics whenever possible.
""", dots=[(S + r'"Spot sample\n(first visit)"->"Early-morning sample\n(next day)"->"Ziehl-Neelsen stain\nand microscopy"->"AFB positive"->"Start DOTS\ntreatment"}', "Sputum examination for TB")],
     example="A cirrhotic patient has ascites, fever and abdominal tenderness; ascitic fluid shows 600 neutrophils per microlitre: spontaneous bacterial peritonitis. A man with 3 weeks of cough is told to bring a spot sample now and an early-morning sample tomorrow after rinsing his mouth."),
dict(t="3. Semen analysis", imp=True, txt="""
**Collection:** sexual abstinence of **2 to 7 days**; sample by **masturbation** into a clean, sterile, wide-mouth container (no lubricants, no ordinary condoms because they contain spermicide); collect the whole ejaculate; write name, time of collection and abstinence period; keep at body temperature and deliver to the laboratory **within 1 hour**. Repeat after 2-3 weeks if abnormal.

**Macroscopic:** volume, colour (grey-white), liquefaction (within 15-60 minutes), viscosity, pH.
**Microscopic:** sperm **count** (concentration), **motility** (progressive, non-progressive, immotile), **morphology** (stained smear), vitality, pus cells, round cells.

| Parameter | WHO 2021 lower reference limit | Older textbooks often give |
|---|---|---|
| Volume | 1.4 mL or more | 2-5 mL |
| Sperm concentration | 16 million/mL or more | 20 million/mL or more |
| Total motility | 42% or more | 50% or more |
| Progressive motility | 30% or more | 25% rapid progressive |
| Normal forms | 4% or more (strict criteria) | 30% or more |
| pH | 7.2 or more | 7.2-8.0 |
Use your textbook's values for the exam and remember that laboratories quote their own.

**Terms:** *azoospermia* (no sperm), *oligozoospermia* (low count), *asthenozoospermia* (poor motility), *teratozoospermia* (abnormal forms), *aspermia* (no ejaculate), *necrozoospermia* (dead sperm), *pyospermia* (pus cells).

**Importance:** the male factor is involved in about 40-50% of infertile couples; semen analysis is the first test of male infertility; also to check success of **vasectomy** (azoospermia) and in medico-legal work. Causes of abnormal results: varicocele, infection, undescended testes, hormone deficiency, obstruction of ducts, heat, smoking, alcohol, drugs.
""", dots=[(S + r'"Abstain\n2-7 days"->"Collect by masturbation\nin sterile container"->"Keep at body temp,\nreach lab in 1 hour"->"Liquefaction, volume, pH"->"Count, motility,\nmorphology"}', "Semen collection and analysis")],
     example="A couple has been unable to conceive for 2 years. The husband is told to abstain for 3 days, produce the sample in the clinic room, and hand it over within an hour. Analysis shows count 4 million/mL and 20% motility: severe oligo-asthenozoospermia, and the doctor looks for varicocele or infection."),
dict(t="4. Urine: collection, physical, chemical and microscopic examination, culture", imp=True, txt="""
**Types of specimen**
| Specimen | How / use |
|---|---|
| Random | Any time; routine screening |
| **First morning** | Most concentrated; pregnancy test, protein, microscopy |
| **Clean-catch midstream** | Best for **culture**; wash hands and genitalia (women front to back; men retract foreskin), discard first stream, collect middle stream in a sterile container |
| Catheter specimen | From the sampling port with an aseptic technique, never from the drainage bag |
| **24-hour urine** | Discard the first morning void, then collect all urine for 24 hours including the next morning's first sample; keep cool with preservative; used for protein, creatinine clearance, hormones |
| Suprapubic aspirate | By a doctor; infants and difficult cases |
Send within 1-2 hours or refrigerate (bacteria multiply and cells break down).

**Physical examination:** volume 800-2,000 mL/day (polyuria in diabetes; oliguria under 400 mL; anuria under 100 mL); colour pale yellow (dark in dehydration, red in haematuria, brown-yellow with froth in jaundice); transparency (turbid with pus, phosphates, bacteria); odour aromatic (ammoniacal in infection, fruity in ketosis); **specific gravity 1.003-1.030**; **pH 4.6-8.0** (average 6).

**Chemical (dipstick and tests):** **protein** (proteinuria in nephrotic syndrome, GN, UTI, pre-eclampsia; heat and acetic acid test), **glucose** (glycosuria in diabetes; Benedict's test), **ketones** (Rothera's test; DKA, starvation), **bile pigments** (Fouchet's; obstructive jaundice), **urobilinogen** (haemolytic jaundice), blood, nitrite and **leucocyte esterase** (UTI).

**Microscopy (centrifuged deposit):** RBC 0-2 per high-power field (haematuria if more), pus cells 0-5 per HPF (pyuria if more), epithelial cells; **casts** - hyaline (normal, exercise), **RBC casts (glomerulonephritis)**, WBC casts (pyelonephritis), granular (renal disease); crystals - calcium oxalate, uric acid, triple phosphate; bacteria, yeast, *Trichomonas*.

**Culture and sensitivity:** midstream specimen, before antibiotics; plated on **CLED or MacConkey agar**; **significant bacteriuria = 100,000 (10^5) organisms per mL or more** of one species; identify the organism (usually *E. coli*); **sensitivity by Kirby-Bauer disc diffusion** on Mueller-Hinton agar (zone of inhibition -> sensitive or resistant) to select the antibiotic.
""", dots=[(S + r'"Clean-catch\nmidstream urine"->"Dipstick and\nmicroscopy"->"Culture on CLED\nor MacConkey"->"Colony count\n100,000 per mL or more"->"Sensitivity:\nKirby-Bauer discs"->"Choose antibiotic"}', "Urine culture and sensitivity")],
     example="A 28-year-old woman with burning urination and frequency: dipstick shows nitrite and leucocyte esterase positive; pus cells are 30 per HPF and midstream culture grows E. coli at 10^5 per mL, sensitive to nitrofurantoin: cystitis. "
             "A patient with smoky urine, RBC casts and 3+ protein has glomerulonephritis."),
dict(t="5. Faeces: characteristics, occult blood, ova and parasites, reducing substances", imp=True, txt="""
**Collection:** fresh stool passed into a **clean, dry, wide-mouth container** with a spatula; not mixed with urine, water or disinfectant, and not taken from the toilet bowl; about a walnut-sized amount (5 g); label and send **at once** (motile amoebic trophozoites die within 30 minutes; keep warm). For parasites, send **3 samples on different days**. For culture use a sterile container or rectal swab in transport medium (Cary-Blair). Avoid barium, oils, laxatives, antacids before tests.

**Naked-eye characteristics**
| Finding | Meaning |
|---|---|
| Normal | 100-200 g/day, brown (stercobilin), semisolid, faecal odour |
| **Black, tarry (melaena)** | Bleeding in upper gut (also iron, bismuth) |
| Bright red blood | Piles, fissure, rectal cancer |
| **Rice-water** | **Cholera** |
| Pea-soup | Typhoid |
| Blood and mucus | Amoebic or bacillary dysentery, colitis |
| Pale, clay-coloured | Obstructive jaundice |
| Pale, bulky, greasy, floating (**steatorrhoea**) | Malabsorption, pancreatitis, coeliac disease |
| Worms seen | Ascaris, threadworm, tapeworm segments |

**Occult blood test (hidden blood):** guaiac test or immunochemical FIT; used for colorectal cancer screening, ulcers, hookworm. Preparation: for 3 days avoid red meat, iron tablets, aspirin/NSAIDs and large amounts of vitamin C (false negative); collect **3 consecutive stools**.

**Ova, cysts and parasites:** *direct wet mount* in saline and iodine; *concentration techniques* (formol-ether sedimentation, zinc sulphate flotation) improve detection.
| Organism | Finding |
|---|---|
| *Entamoeba histolytica* | Cysts with 4 nuclei; trophozoites containing red cells |
| *Giardia* | Pear-shaped trophozoites; oval cysts |
| *Ascaris* | Round mamillated (bumpy) egg |
| Hookworm | Thin-walled oval egg with 4-8 cells |
| *Trichuris* | Barrel-shaped (lemon) egg with polar plugs |
| *Taenia* | Round radially striated egg |

**Reducing substances:** tests (Benedict's/Clinitest) detect unabsorbed sugars such as lactose in watery, acidic stools of infants with lactose intolerance or carbohydrate malabsorption. Also examine stool pH (below 5.5 with carbohydrate malabsorption), leucocytes (invasive infection) and fat (Sudan III stain).
""", dots=[(S + r'"Fresh stool in\nclean container"->"Naked eye:\ncolour, blood, mucus"->"Wet mount:\nsaline and iodine"->"Concentration:\nformol-ether"->"Ova, cysts,\nparasites";"Fresh stool in\nclean container"->"Occult blood\ntest (3 samples)"}', "Stool examination")],
     example="A child with watery, acidic stools after milk feeds has reducing substances positive: lactose intolerance. A 50-year-old with tiredness and iron deficiency anaemia has a positive occult blood test on 3 samples: needs colonoscopy to exclude colon cancer. "
             "A labourer with anaemia and hookworm eggs in stool needs deworming and iron."),
]

P5 = dict(
    id="P5", subject="Pathology", title="Unit V - Clinical Pathology", hrs=5, topics=TOPICS,
    mcq=[
        ("Usual site for lumbar puncture in adults", ["T12-L1", "L1-L2", "L3-L4 or L4-L5", "S1-S2"], 2),
        ("Lumbar puncture is contraindicated in", ["Fever", "Suspected raised ICP from a brain mass", "Neck stiffness", "Suspected meningitis"], 1),
        ("Xanthochromia of CSF suggests", ["Bacterial meningitis", "Subarachnoid haemorrhage", "Viral meningitis", "Normal CSF"], 1),
        ("Needle-shaped, negatively birefringent crystals in synovial fluid indicate", ["Gout", "Pseudogout", "Rheumatoid arthritis", "Osteoarthritis"], 0),
        ("Recommended abstinence period before semen collection", ["12 hours", "2 to 7 days", "2 weeks", "1 month"], 1),
        ("Absence of sperm in the ejaculate is", ["Oligozoospermia", "Azoospermia", "Asthenozoospermia", "Teratozoospermia"], 1),
        ("Best urine specimen for culture", ["Random urine from a bag", "Clean-catch midstream urine", "First drop of urine", "Catheter bag urine"], 1),
        ("Significant bacteriuria is a count of", ["10 per mL", "1,000 per mL", "100,000 (10^5) per mL or more", "1 per mL"], 2),
        ("Red blood cell casts in urine indicate", ["Cystitis", "Glomerulonephritis", "Renal stone", "Normal urine"], 1),
        ("Rice-water stools are typical of", ["Typhoid", "Cholera", "Amoebiasis", "Obstructive jaundice"], 1),
    ],
    long=[
        ("Describe lumbar puncture: indications, contraindications, procedure, nursing care and normal and abnormal CSF findings. (PYQ pattern)",
         "L3-L4; position; 3 tubes; opening pressure; post-LP flat and headache; normal values; comparison table of bacterial, viral, TB, SAH."),
        ("Describe the collection and examination of sputum and wound discharge. (PYQ pattern)",
         "Early-morning deep cough, sterile container; spot-morning for AFB; ZN stain; Gram and culture; wound deep swab before antibiotic; transport."),
        ("Describe semen analysis: collection, normal values, abnormalities and importance in infertility. (PYQ pattern)",
         "Abstinence, masturbation, 1 hour; count, motility, morphology values; azoospermia and other terms; male factor and vasectomy check."),
        ("Describe the collection and examination of urine, including culture and sensitivity. (Important topic)",
         "Specimen types and 24-hour urine; physical, chemical (protein, glucose, ketones, bile), microscopy and casts; 10^5 per mL; Kirby-Bauer."),
        ("Describe the examination of stool: collection, characteristics, occult blood, ova and parasites, reducing substances. (Important topic)",
         "Collection rules; colour and consistency findings; occult blood diet preparation; wet mount and concentration; parasite features; Benedict's."),
    ],
    imp=["Lumbar puncture and CSF findings", "Sputum for AFB", "Semen analysis", "Urine: 24-hour collection, casts, culture", "Stool: occult blood, ova and parasites"],
)