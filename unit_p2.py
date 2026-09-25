S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Respiratory system", imp=True, txt="""
**Pneumonia** = inflammation of lung parenchyma with consolidation.
| | Lobar | Broncho |
|---|---|---|
| Organism | *Streptococcus pneumoniae* | Staph. aureus, Klebsiella, H. influenzae |
| Pattern | Whole lobe, uniform | Patchy, both lung bases |
| Patients | Healthy adults | Infants, elderly, bed-bound |
**Stages of lobar pneumonia:** congestion (day 1-2) -> **red hepatization** (2-4; red cells, fibrin, neutrophils) -> **grey hepatization** (4-8; red cells break down) -> resolution (8-10). Features: fever, rusty sputum, pleuritic pain. Complications: abscess, empyema, pleuritis.

**Lung abscess:** localised pus collection; causes: aspiration (alcoholics, unconscious), necrotising pneumonia, obstruction by tumour. Foul-smelling sputum, clubbing.

**Pulmonary tuberculosis** (*Mycobacterium tuberculosis*, droplet spread)
- *Primary TB:* **Ghon focus** (subpleural, mid-lung) + caseous hilar nodes = **Ghon complex**; usually heals by fibrosis and calcification.
- *Secondary (reactivation) TB:* **apex** of lung (high oxygen); caseating granulomas, cavitation, fibrosis; haemoptysis. Spread: bronchogenic, **miliary** (blood), pleural.
- Features: evening fever, night sweats, weight loss, chronic cough. Diagnosis: sputum AFB (Ziehl-Neelsen), chest X-ray, CBNAAT, Mantoux.

**COPD (chronic obstructive pulmonary disease)**
| Disease | Key points |
|---|---|
| Chronic bronchitis | Productive cough for at least 3 months in 2 successive years; mucous gland hypertrophy (Reid index >0.5); smoking |
| Emphysema | Permanent enlargement of air spaces beyond the terminal bronchiole with wall destruction; *centriacinar* (smokers), *panacinar* (alpha-1 antitrypsin deficiency); barrel chest, "pink puffer" |
| Bronchial asthma | Reversible airway narrowing, type I hypersensitivity, eosinophils, Curschmann spirals, Charcot-Leyden crystals; wheeze |
| Bronchiectasis | Permanent bronchial dilatation after infection (TB, measles, cystic fibrosis); large amounts of foul sputum, clubbing |

**Tumours of lung:** smoking is the main cause.
| Type | Site | Points |
|---|---|---|
| Squamous cell | Central | Keratin; hypercalcaemia; cavitation |
| Adenocarcinoma | Peripheral | Commonest overall; also in non-smokers |
| Small cell | Central | Neuroendocrine; ectopic ADH/ACTH; most aggressive, early spread |
Spread: hilar nodes, brain, liver, bone, adrenal. Symptoms: persistent cough, haemoptysis, weight loss, hoarseness.
""", dots=[(S + r'"M. tuberculosis\ninhaled"->"Ghon focus + hilar nodes\n(Ghon complex)"->"Healing:\nfibrosis, calcification";'
                r'"Ghon focus + hilar nodes\n(Ghon complex)"->"Miliary TB\n(blood spread)";"Healing:\nfibrosis, calcification"->"Reactivation\n(apex)"->"Cavity, haemoptysis"}', "Primary and secondary tuberculosis")],
     example="A 30-year-old man from a crowded locality has 4 weeks of evening fever, weight loss and blood-streaked sputum; X-ray shows an upper-lobe cavity and sputum is AFB positive: secondary TB. "
             "The nurse collects an early-morning sputum sample, teaches cough hygiene and stresses uninterrupted DOTS treatment."),
dict(t="2. Cardiovascular system", imp=True, txt="""
**Atherosclerosis:** thickening and hardening of arteries by lipid-rich plaques in the intima.
- *Risk factors:* high LDL cholesterol, hypertension, smoking, diabetes, obesity, age, male sex, family history, sedentary life.
- *Sites:* abdominal aorta, coronary, carotid, femoral arteries.
- *Evolution:* endothelial injury -> **fatty streak** (foam cells) -> **fibrofatty plaque** (fibrous cap, lipid core) -> **complicated plaque** (calcification, ulceration, haemorrhage, thrombosis, aneurysm).

**Ischaemia and infarction (ischaemic heart disease)**
- *Angina:* reversible ischaemia; chest pain on effort, relieved by rest or nitrates.
- **Myocardial infarction (MI):** necrosis of heart muscle, mostly from thrombosis on a ruptured plaque in a coronary artery (left anterior descending is most often involved).
- Morphology (coagulative necrosis): <12 h nothing visible; 1 day pale; 3-7 days yellow and soft (peak risk of rupture); 2 weeks granulation tissue; 6 weeks white scar.
- Diagnosis: severe chest pain over 20-30 min with sweating, ECG changes, **troponin I/T** (rise in 3-4 h) and CK-MB.
- Complications: **arrhythmia (commonest cause of death)**, cardiogenic shock, heart failure, rupture, mural thrombus, pericarditis, ventricular aneurysm.

**Rheumatic heart disease (RHD):** follows group A beta-haemolytic streptococcal pharyngitis by 2-3 weeks; antibodies cross-react with heart tissue (type II hypersensitivity).
- **Aschoff nodule** (pathognomonic): giant cells, Anitschkow ("caterpillar") cells, lymphocytes.
- Acute: pancarditis; small vegetations along valve closure lines. Chronic: **mitral stenosis** (fish-mouth valve), then aortic.
- **Jones criteria (major):** carditis, migratory polyarthritis, chorea, erythema marginatum, subcutaneous nodules. Prevention: benzathine penicillin.

**Infective endocarditis:** infection of the valves with friable vegetations.
| | Acute | Subacute |
|---|---|---|
| Organism | *Staph. aureus* | Viridans streptococci |
| Valve | Normal | Already damaged |
| Course | Days, severe | Weeks, mild |
Features: fever, new murmur, splinter haemorrhages, Osler nodes, Janeway lesions, Roth spots, emboli to brain, kidney, spleen.
""", dots=[(S + r'"LDL, smoking,\nhypertension, diabetes"->"Endothelial injury"->"Fatty streak"->"Fibrofatty plaque"->"Plaque rupture\nand thrombus"->"Myocardial\ninfarction";'
                r'"Fibrofatty plaque"->"Angina\n(narrowed lumen)"}', "Atherosclerosis to angina and myocardial infarction")],
     example="A 58-year-old diabetic smoker has crushing chest pain for 40 minutes with sweating; ECG shows ST elevation and troponin is raised: MI. The nurse gets an ECG, gives ordered aspirin, oxygen if hypoxic, "
             "monitors continuously for arrhythmia and keeps the patient at rest. A 10-year-old with migratory joint pain and a new murmur 3 weeks after a sore throat has acute rheumatic fever."),
dict(t="3. Gastrointestinal tract", imp=True, txt="""
**Peptic ulcer (gastric and duodenal):** breach of the mucosa reaching the muscularis, from acid-pepsin plus reduced defence.
- Causes: **H. pylori** (about 90% duodenal, 70% gastric), NSAIDs, smoking, stress, Zollinger-Ellison syndrome.
| | Duodenal | Gastric |
|---|---|---|
| Site | First part | Lesser curvature |
| Frequency | Commoner | Less |
| Pain | Relieved by food, night pain | Worsened by food |
| Malignancy | Almost never | Possible - biopsy always |
Gross: round, punched-out, clean base. Complications: **haemorrhage (commonest; haematemesis, melaena)**, perforation, pyloric obstruction, penetration; malignant change (gastric).

**Gastritis:** *acute* (NSAIDs, alcohol, stress); *chronic* - *H. pylori* (antral), autoimmune (body, pernicious anaemia); risk of gastric cancer and MALT lymphoma.

**Oral mucosa:** *leukoplakia* = white patch that cannot be scraped off; pre-malignant (tobacco, betel quid). **Squamous cell carcinoma** of the mouth is common in India (tobacco, betel, alcohol).

**Oesophageal cancer:** squamous carcinoma (middle third; tobacco, alcohol, hot beverages) and adenocarcinoma (lower third, Barrett's oesophagus). Progressive dysphagia (solids then liquids), weight loss.

**Gastric cancer:** adenocarcinoma; *H. pylori*, smoked/salted foods; diffuse type = **linitis plastica** (leather-bottle stomach). Spread: **Virchow's node** (left supraclavicular), **Krukenberg tumour** (ovary).

**Intestinal lesions**
- **Typhoid ulcer** (*Salmonella typhi*): Peyer's patches of ileum; ulcers lie **along the long axis** of the bowel (in TB they are transverse). Complications in week 3: haemorrhage and perforation.
| | Crohn's disease | Ulcerative colitis |
|---|---|---|
| Site | Any part; terminal ileum | Rectum upward, colon only |
| Pattern | Skip lesions | Continuous |
| Depth | Transmural | Mucosa and submucosa |
| Hallmark | Granulomas, fistulae, strictures | Crypt abscesses, pseudopolyps |
| Symptoms | Pain, diarrhoea, weight loss | Bloody diarrhoea |
| Cancer risk | Small | Higher |
- **Colorectal cancer:** adenoma-carcinoma sequence (polyps); adenocarcinoma of rectosigmoid commonest; risk: low fibre, red meat, polyposis (FAP), IBD. Right-sided: anaemia; left-sided: obstruction, altered bowel habit. Marker CEA; staging Dukes'.
""", dots=[(S + r'"H. pylori\nor NSAIDs"->"Mucosal defence\nfalls"->"Acid and pepsin"->"Peptic ulcer"->"Bleeding,\nperforation,\nobstruction"}', "Pathogenesis and complications of peptic ulcer")],
     example="A 40-year-old has burning epigastric pain at night that eases after a meal: duodenal ulcer, H. pylori positive; treated with acid suppression and antibiotics. "
             "Black tarry stools with dizziness mean bleeding (melaena) and need urgent care. In a chronic tobacco-betel user, a white non-scrapable patch in the cheek is leukoplakia and needs biopsy."),
dict(t="4. Liver, gall bladder and pancreas", imp=True, txt="""
**Viral hepatitis**
| Virus | Spread | Course |
|---|---|---|
| A, E | Faeco-oral | Acute only; E severe in pregnancy |
| B, C, D | Blood, sexual, mother-to-child | Can become chronic -> cirrhosis, liver cancer |
Features: jaundice, dark urine, pale stools, raised ALT/AST. Morphology: ballooned hepatocytes, **Councilman bodies** (apoptotic cells), inflammation. Markers: HBsAg (infection), anti-HBs (immunity). Prevention: HBV vaccine, hepatitis A vaccine, safe injection.

**Amoebic liver abscess** (*Entamoeba histolytica*): usually single, large, in the **right lobe**; pus is thick reddish-brown, **"anchovy sauce"**, and is sterile on bacterial culture. Fever, right upper abdominal pain, tender hepatomegaly. Treatment: metronidazole.

**Cirrhosis:** diffuse fibrosis with regenerative nodules and loss of normal architecture (irreversible).
- Causes: alcohol (commonest in West), hepatitis B and C (India), non-alcoholic fatty liver, biliary disease, haemochromatosis.
- *Portal hypertension:* ascites, splenomegaly, **oesophageal varices** (haematemesis), caput medusae, haemorrhoids.
- *Liver failure:* jaundice, spider naevi, palmar erythema, gynaecomastia, coagulopathy, **hepatic encephalopathy** (flapping tremor, confusion).
- Complication: hepatocellular carcinoma.

**Gall bladder - cholecystitis:** about 90% from **gallstones** (cholesterol stones commonest; "fair, fat, female, forty, fertile"). Right upper quadrant pain, fever, Murphy's sign; complications: empyema, perforation, gangrene.

**Pancreatitis**
- *Acute:* gallstones and alcohol; enzymes digest the gland (autodigestion), **fat necrosis**, haemorrhage. Severe epigastric pain radiating to back; raised **serum amylase and lipase**. Complications: shock, pseudocyst, ARDS.
- *Chronic:* repeated alcohol injury; fibrosis, calcification, diabetes, malabsorption.

**Tumours:** *hepatocellular carcinoma* (cirrhosis, HBV, aflatoxin; **AFP** raised); *carcinoma of head of pancreas* (painless progressive jaundice, Courvoisier's sign, CA 19-9, smoking); *gall bladder carcinoma* (gallstones, poor prognosis).
""", dots=[(S + r'"Alcohol, hepatitis B/C,\nfatty liver"->"Hepatocyte injury"->"Fibrosis and nodules\n(cirrhosis)"->"Portal hypertension"->"Ascites, varices,\nsplenomegaly";'
                r'"Fibrosis and nodules\n(cirrhosis)"->"Liver failure"->"Jaundice,\nencephalopathy";"Fibrosis and nodules\n(cirrhosis)"->"Hepatocellular\ncarcinoma"}', "Cirrhosis and its complications")],
     example="A 50-year-old with long-term alcohol use has jaundice, abdominal distension, spider naevi and vomits blood from oesophageal varices: cirrhosis with portal hypertension. "
             "The nurse measures abdominal girth and weight daily, watches for confusion (encephalopathy), follows salt and fluid restriction and takes bleeding precautions."),
dict(t="5. Skeletal system", imp=True, txt="""
**Bone healing (fracture):** (1) **haematoma** (hours-days); (2) **soft callus** - granulation tissue and fibrocartilage (1-3 weeks); (3) **hard callus** - woven bone (3-12 weeks); (4) **remodelling** - lamellar bone (months-years). Delayed by infection, poor immobilisation, poor blood supply, malnutrition, smoking, diabetes, old age.

**Osteoporosis:** reduced bone mass with *normal* mineralisation. Postmenopausal (oestrogen loss), senile, steroids, immobility. Fractures: vertebral compression, **neck of femur**, Colles' (wrist). DEXA T-score -2.5 or lower. Prevention: calcium, vitamin D, weight-bearing exercise, stopping smoking.

**Osteomyelitis:** bone infection, commonest organism *Staph. aureus* (Salmonella in sickle cell disease). In children, haematogenous spread to the **metaphysis** of long bones. Acute: fever, bone pain, pus -> subperiosteal abscess -> **sequestrum** (dead bone) surrounded by **involucrum** (new bone) with draining sinus (cloacae). Chronic if untreated. TB of spine = Pott's disease.

**Bone tumours**
| Tumour | Age / site | Features |
|---|---|---|
| Osteochondroma | Adolescents | Commonest benign |
| Osteosarcoma | 10-25 yrs, around knee | Codman's triangle, sunburst; lung metastasis |
| Ewing sarcoma | Children, diaphysis | Small round blue cells, onion-skin |
| Giant cell tumour | 20-40 yrs, epiphysis | Soap-bubble appearance |
| Multiple myeloma | Elderly | Punched-out skull lesions, Bence Jones protein |

**Arthritis**
| | Rheumatoid arthritis | Osteoarthritis |
|---|---|---|
| Nature | Autoimmune, systemic | Degenerative, wear and tear |
| Joints | Small, symmetrical (hands) | Weight-bearing (knee, hip), hand DIP |
| Stiffness | Morning, over 1 hour | Short, worse after activity |
| Pathology | Synovitis, **pannus**, erosion | Cartilage loss, osteophytes |
| Tests | Rheumatoid factor, anti-CCP | X-ray only |
""", dots=[(S + r'"Fracture"->"Haematoma"->"Soft callus\n(1-3 weeks)"->"Hard callus\n(3-12 weeks)"->"Remodelling\n(months)"}', "Stages of fracture healing")],
     example="A 65-year-old postmenopausal woman slips and breaks her neck of femur with minimal force: osteoporosis. An 8-year-old boy with fever, severe pain and a tender swollen lower thigh has acute osteomyelitis; "
             "early antibiotics and rest prevent a sequestrum. A woman with symmetrical swollen small hand joints and morning stiffness over an hour has rheumatoid arthritis."),
dict(t="6. Endocrine system", imp=True, txt="""
**Diabetes mellitus:** chronic hyperglycaemia from absent or ineffective insulin.
| | Type 1 | Type 2 |
|---|---|---|
| Cause | Autoimmune destruction of beta cells | Insulin resistance with relative deficiency |
| Age / build | Young, thin | Adults, obese |
| Insulin | Essential | Diet, tablets, later insulin |
| Acute crisis | Ketoacidosis (DKA) | Hyperosmolar state |
**Diagnosis:** fasting glucose 126 mg/dL or more; 2-hour OGTT 200 or more; HbA1c 6.5% or more; random glucose 200 or more with symptoms. Classic symptoms: polyuria, polydipsia, polyphagia, weight loss.
**Complications:** *acute* - DKA, hypoglycaemia, hyperosmolar state; *microvascular* - retinopathy, nephropathy (Kimmelstiel-Wilson nodules), neuropathy; *macrovascular* - MI, stroke, peripheral vascular disease, **diabetic foot** (neuropathy + ischaemia + infection -> gangrene).

**Goitre:** enlargement of the thyroid. *Simple/endemic* - iodine deficiency (sub-Himalayan belt); diffuse then multinodular. *Toxic* - Graves' disease (diffuse, exophthalmos, thyroid-stimulating antibodies), toxic nodular goitre. *Hashimoto thyroiditis* - autoimmune, hypothyroid.

**Carcinoma thyroid**
| Type | Points |
|---|---|
| **Papillary** (commonest) | Young women; radiation; "Orphan Annie eye" nuclei, psammoma bodies; spreads to nodes; excellent prognosis |
| Follicular | Blood spread to bone and lung; iodine-deficient areas |
| Medullary | Parafollicular C cells; **calcitonin**; amyloid; MEN 2 |
| Anaplastic | Elderly; very aggressive |
""", dots=[(S + r'"Insulin deficiency\nor resistance"->"Hyperglycaemia"->"Microvascular:\nretinopathy, nephropathy,\nneuropathy";'
                r'"Hyperglycaemia"->"Macrovascular:\nMI, stroke, foot gangrene";"Hyperglycaemia"->"Acute:\nDKA, hypoglycaemia"}', "Complications of diabetes mellitus")],
     example="A 12-year-old with weight loss, polyuria, thirst, fruity breath, vomiting and drowsiness has type 1 diabetes in ketoacidosis; the nurse checks glucose and ketones, gives fluids and insulin as ordered and monitors potassium. "
             "A villager in a sub-Himalayan area with a slowly growing neck swelling and no iodised salt has simple endemic goitre."),
]

P2 = dict(
    id="P2", subject="Pathology", title="Unit II - Special Pathology (systems)", hrs=5, topics=TOPICS,
    mcq=[
        ("Ghon complex in primary tuberculosis consists of", ["Cavity plus fibrosis", "Ghon focus plus hilar lymph node involvement", "Apical focus plus pleural effusion", "Miliary nodules"], 1),
        ("Emphysema associated with alpha-1 antitrypsin deficiency is", ["Centriacinar", "Panacinar", "Paraseptal", "Irregular"], 1),
        ("Lung cancer with ectopic ADH/ACTH secretion and very aggressive course", ["Squamous cell carcinoma", "Small cell carcinoma", "Adenocarcinoma", "Bronchial adenoma"], 1),
        ("Aschoff bodies are pathognomonic of", ["Rheumatic carditis", "Infective endocarditis", "Atherosclerosis", "Viral myocarditis"], 0),
        ("Commonest cause of death after myocardial infarction", ["Cardiac rupture", "Arrhythmia", "Pericarditis", "Ventricular aneurysm"], 1),
        ("Typhoid ulcers of the ileum lie", ["Transversely", "Longitudinally along Peyer's patches", "Circularly", "In the caecum only"], 1),
        ("Skip lesions with transmural inflammation and granulomas suggest", ["Ulcerative colitis", "Crohn's disease", "Typhoid", "Amoebiasis"], 1),
        ("Pus of amoebic liver abscess resembles", ["Green fluid", "Anchovy sauce", "Black tar", "Cheese"], 1),
        ("Dead bone in chronic osteomyelitis is called", ["Involucrum", "Sequestrum", "Callus", "Osteophyte"], 1),
        ("Commonest thyroid carcinoma", ["Follicular", "Papillary", "Medullary", "Anaplastic"], 1),
    ],
    long=[
        ("Define pulmonary tuberculosis. Describe the pathology of primary and secondary TB. (PYQ pattern)",
         "Organism and spread; Ghon focus and complex; healing; secondary TB at apex with caseation and cavity; complications (miliary, haemoptysis); diagnosis."),
        ("Define atherosclerosis. Describe risk factors and the pathology of myocardial infarction. (PYQ pattern)",
         "Definition; risk factors; fatty streak to complicated plaque; MI causes, morphology timeline, markers, complications."),
        ("Describe peptic ulcer: causes, pathology, complications and differences between gastric and duodenal ulcer. (PYQ pattern)",
         "H. pylori, NSAIDs; site, pain pattern, malignancy; haemorrhage, perforation, obstruction."),
        ("Define cirrhosis of liver. Describe causes, pathology and complications. (Important topic)",
         "Fibrosis plus nodules; causes; portal hypertension (ascites, varices, splenomegaly); liver failure; HCC."),
        ("Describe the types and complications of diabetes mellitus. (Important topic)",
         "Type 1 vs 2 table; diagnosis criteria; acute and chronic (micro and macrovascular) complications; diabetic foot."),
    ],
    imp=["Tuberculosis and COPD", "Atherosclerosis and MI", "Rheumatic heart disease", "Peptic ulcer, Crohn's vs UC", "Cirrhosis and hepatitis", "Diabetes mellitus"],
)