S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Kidney and urinary tract", imp=True, txt="""
**Glomerulonephritis (GN):** immune-mediated inflammation of the glomeruli.
| | Nephritic syndrome | Nephrotic syndrome |
|---|---|---|
| Main feature | Haematuria (smoky / cola urine), hypertension, oedema, oliguria | Proteinuria over 3.5 g/day, low albumin, gross oedema, high cholesterol |
| Example | **Acute post-streptococcal GN** | Minimal change disease (children), membranous GN |
**Acute post-streptococcal GN:** child, 1-3 weeks after streptococcal pharyngitis (3-6 weeks after skin infection). Antigen-antibody (immune) complexes lodge in glomeruli; complement (C3) falls; glomeruli are enlarged and hypercellular. Most children recover; a few progress to **chronic GN** with shrunken scarred kidneys and chronic renal failure.

**Pyelonephritis:** infection of the renal pelvis and kidney. Organism *E. coli*; ascends from the bladder (women, reflux, obstruction, catheters, diabetes). *Acute:* fever, chills, flank pain, dysuria, pus cells and WBC casts in urine; complications: abscess, papillary necrosis (diabetes), pyonephrosis. *Chronic:* repeated infection with reflux gives a scarred, contracted kidney.

**Renal calculi:** calcium oxalate (commonest, about 75%), triple phosphate/struvite (*Proteus*, alkaline urine, staghorn), uric acid (gout, radiolucent), cystine (rare). Features: **renal colic** (severe loin-to-groin pain), haematuria, vomiting; complications: obstruction, hydronephrosis, infection. Prevention: plenty of fluids (over 2.5-3 litres/day).

**Cystitis:** bladder infection, mostly *E. coli*; commoner in women (short urethra), also pregnancy, catheters. Dysuria, frequency, urgency, suprapubic pain; cloudy urine; confirm by urine culture and sensitivity.

**Renal cell carcinoma:** adult kidney cancer from tubule cells (clear cell type; smoking, obesity). Classic: haematuria, flank pain, mass; yellow tumour; may invade the renal vein and vena cava; spreads to lungs and bone; paraneoplastic polycythaemia, hypercalcaemia.

**Renal failure**
| | Acute (AKI) | Chronic (CKD) |
|---|---|---|
| Onset | Hours to days, often reversible | Months to years, irreversible |
| Causes | Pre-renal (shock, dehydration), renal (acute tubular necrosis, toxins), post-renal (obstruction) | Diabetes, hypertension, chronic GN |
| Definition | Urine under 400 mL/day (oliguria) with rising creatinine | GFR under 60 mL/min for 3 months or more |
| Phases | Oliguric, diuretic, recovery | Stages 1-5 |
CKD features: uraemia (nausea, itching, drowsiness), anaemia (low erythropoietin), hyperkalaemia, acidosis, high BP, bone disease, pericarditis. Treatment: diet control, dialysis, transplantation.
""", dots=[(S + r'"Streptococcal\nthroat or skin infection"->"Immune complexes\nin glomeruli"->"Acute\nglomerulonephritis"->"Haematuria, oedema,\nhypertension";'
                r'"Acute\nglomerulonephritis"->"Recovery\n(most children)";"Acute\nglomerulonephritis"->"Chronic GN, then\nrenal failure"}', "Acute post-streptococcal glomerulonephritis")],
     example="A 7-year-old boy with cola-coloured urine, puffy face and BP 140/90 two weeks after a sore throat has acute post-streptococcal GN. The nurse records intake-output and daily weight, restricts salt and fluids as advised and checks BP. "
             "A young man with sudden severe loin-to-groin pain and haematuria has ureteric colic from a stone."),
dict(t="2. Male genital system", imp=True, txt="""
**Cryptorchidism (undescended testis):** testis not in the scrotum (3% of full-term boys; most descend by 3-6 months). Risks: infertility, **torsion**, hernia and a raised risk of **testicular germ cell tumour (seminoma)**. Treatment: **orchidopexy at 6-18 months**.

**Testicular atrophy:** shrinkage from cryptorchidism, mumps orchitis, ischaemia or torsion, radiation, oestrogen therapy, cirrhosis, hypopituitarism and old age; leads to infertility.

**Benign prostatic hyperplasia (BPH):** nodular overgrowth of the periurethral (transition) zone in men over 50 (dihydrotestosterone effect). Symptoms: frequency, nocturia, hesitancy, weak stream, incomplete emptying. Complications: **acute retention**, infection, stones, hydronephrosis, renal failure. Treatment: alpha blockers, 5-alpha-reductase inhibitors, TURP (transurethral resection of prostate).

**Carcinoma penis:** squamous cell carcinoma; associated with **poor hygiene, phimosis, absence of circumcision**, HPV and smoking; rare in circumcised men. Precursors: leukoplakia, Bowen's disease. Presents as a non-healing ulcer or growth on the glans; spreads to inguinal nodes.

**Carcinoma prostate:** adenocarcinoma of the **peripheral zone** (felt on rectal examination as a hard, irregular nodule); elderly men; PSA raised (over 4 ng/mL, but also rises in BPH and prostatitis); Gleason score grades the tumour. Spreads to pelvic nodes and **bone (osteoblastic, dense) especially vertebrae**. Treatment: surgery, radiotherapy, androgen deprivation therapy.
| | BPH | Carcinoma prostate |
|---|---|---|
| Zone | Transition (central) | Peripheral |
| Gland on DRE | Smooth, enlarged | Hard, nodular |
| Spread | None | Bone, nodes |
""", dots=[(S + r'"Age and\ndihydrotestosterone"->"Prostate\nhyperplasia"->"Urethral\nobstruction"->"Weak stream,\nretention"->"Infection,\nhydronephrosis"}', "Consequences of benign prostatic hyperplasia")],
     example="A 65-year-old has to get up 4 times at night, has a weak stream and today cannot pass urine: BPH with acute retention. The nurse relieves distension by catheterisation as ordered, records volume drained and watches for post-obstructive diuresis. "
             "A boy of 2 years with an empty right scrotum needs referral for orchidopexy."),
dict(t="3. Female genital system", imp=True, txt="""
**Carcinoma of the cervix:** among the commonest cancers of Indian women; caused by persistent **human papillomavirus (HPV 16 and 18)**.
- *Risk factors:* early sexual activity or marriage, multiple partners, multiparity, smoking, HIV, poor hygiene, low socio-economic status.
- *Sequence:* **CIN I-III** (cervical intra-epithelial neoplasia, dysplasia) at the squamocolumnar junction -> carcinoma in situ -> invasive **squamous cell carcinoma** (cervical adenocarcinoma is less common). Takes 10-15 years.
- *Features:* post-coital or inter-menstrual bleeding, foul discharge, pelvic pain; late: ureteric obstruction (a major cause of death).
- *Spread:* local, pelvic nodes, then lungs and bone.
- *Prevention:* **HPV vaccine** (best at 9-14 years), **screening by Pap smear or VIA** (visual inspection with acetic acid), treatment of CIN.

**Carcinoma of the endometrium:** commonest cancer of the uterine body in post-menopausal women; unopposed oestrogen (obesity, diabetes, nulliparity, late menopause, tamoxifen); preceded by endometrial hyperplasia. Sign: **post-menopausal bleeding**; diagnosis by endometrial biopsy. Adenocarcinoma, often early stage.

**Uterine fibroids (leiomyoma):** commonest benign tumour of the female genital tract; oestrogen-dependent, in women 30-50 years; types: submucosal, intramural, subserosal. Firm, whorled, well-circumscribed. Features: heavy periods (menorrhagia), pressure symptoms, infertility, pain (red degeneration in pregnancy). Malignant change (leiomyosarcoma) is very rare.

**Gestational trophoblastic disease**
| | Vesicular (hydatidiform) mole | Choriocarcinoma |
|---|---|---|
| Nature | Benign, swollen villi ("bunch of grapes"); complete (46,XX, no fetus) or partial | Malignant trophoblast without villi |
| Features | Bleeding, uterus larger than dates, hyperemesis, very high beta-hCG, "snowstorm" on ultrasound | Bleeding after abortion/mole/delivery; high beta-hCG |
| Spread | May persist or turn malignant | Blood to lung (cannonball shadows), vagina, brain |
| Treatment | Suction evacuation; hCG follow-up for a year | Chemotherapy (methotrexate) with excellent cure |

**Ovarian cysts and tumours**
| Lesion | Points |
|---|---|
| Functional (follicular, luteal) cysts | Common, resolve alone |
| Endometriotic ("chocolate") cyst | Endometriosis; pain, infertility |
| Serous cystadenoma | Commonest benign tumour |
| Mucinous cystadenoma | Very large, multilocular |
| Dermoid (mature cystic teratoma) | Young women; hair, teeth, fat; torsion |
| **Serous cystadenocarcinoma** | Commonest malignant; CA-125 raised; late presentation; ascites; transcoelomic spread |
| Krukenberg tumour | Bilateral metastasis from stomach (signet-ring cells) |
""", dots=[(S + r'"HPV 16 and 18\ninfection"->"CIN I to III\n(dysplasia)"->"Carcinoma\nin situ"->"Invasive carcinoma"->"Nodes, ureters,\nlungs";'
                r'"Pap smear or VIA\nscreening"->"CIN I to III\n(dysplasia)"[label="detects"];"HPV vaccine"->"HPV 16 and 18\ninfection"[label="prevents"]}', "Natural history of cervical cancer and where prevention acts")],
     example="A 45-year-old mother of four has bleeding after intercourse; VIA is positive and biopsy shows CIN III, treated before it becomes invasive. The nurse counsels on screening every few years and HPV vaccination for daughters. "
             "A 24-year-old in early pregnancy has bleeding, a uterus larger than dates and a very high hCG: suspect hydatidiform mole; the nurse prepares for evacuation and explains why hCG follow-up is needed."),
dict(t="4. Breast", imp=True, txt="""
**Fibrocystic change:** commonest benign breast condition, women 30-50, oestrogen effect. Cysts (blue-domed), fibrosis, adenosis, epithelial hyperplasia. Cyclical, bilateral pain and lumpiness before periods. Risk of cancer rises only with atypical hyperplasia.

**Fibroadenoma:** commonest benign tumour, women under 30. **Painless, firm, rubbery, well-defined, very mobile lump ("breast mouse")**; may enlarge in pregnancy. Treatment: observation or excision.

**Carcinoma of the breast:** commonest cancer in women.
- *Risk factors:* increasing age, family history, **BRCA1/BRCA2** mutations, early menarche, late menopause, nulliparity, late first pregnancy, not breastfeeding, obesity, hormone therapy, alcohol, radiation.
- *Types:* ductal carcinoma in situ (DCIS), **invasive ductal carcinoma (about 75%)**, invasive lobular, medullary, inflammatory.
- *Site:* **upper outer quadrant** most often.
- *Features:* painless, hard, irregular, fixed lump; skin dimpling, nipple retraction, blood-stained discharge, **peau d'orange**, ulceration, enlarged axillary nodes.
- *Spread:* lymphatic to axillary nodes; blood to **bone, lung, liver, brain**.
- *Prognosis:* stage, grade, and receptor status (oestrogen, progesterone, HER2).
- *Diagnosis - triple assessment:* clinical examination, imaging (ultrasound, mammography), FNAC or core biopsy.
- *Treatment:* surgery (lumpectomy or mastectomy with node clearance), radiotherapy, chemotherapy, hormone therapy (tamoxifen), targeted therapy (trastuzumab).
- *Screening:* monthly **breast self-examination** (a few days after periods end), clinical breast examination, mammography after 40 to 50 years.
""", dots=[(S + r'"Breast lump"->"Clinical\nexamination"->"Imaging:\nultrasound, mammogram"->"FNAC or\ncore biopsy"->"Diagnosis and\nreceptor status"}', "Triple assessment of a breast lump")],
     example="A 24-year-old finds a painless, smooth, mobile marble-like lump; ultrasound and FNAC show fibroadenoma. A 52-year-old finds a hard, fixed lump in the upper outer quadrant with skin dimpling and a palpable axillary node: "
             "suspect carcinoma and arrange triple assessment urgently. The nurse teaches breast self-examination."),
dict(t="5. Central nervous system", imp=True, txt="""
**Meningitis:** inflammation of the meninges. Triad: fever, headache, **neck stiffness**; also vomiting, photophobia, positive **Kernig's and Brudzinski's signs**, petechial rash in meningococcal disease.
| | Bacterial | Viral | Tuberculous |
|---|---|---|---|
| Organisms | Pneumococcus, meningococcus, *H. influenzae* (neonates: *E. coli*) | Enteroviruses | *M. tuberculosis* |
| CSF appearance | Turbid | Clear | Clear, cobweb clot |
| Cells | Many neutrophils | Lymphocytes | Lymphocytes |
| Protein | High | Mild rise | High |
| Glucose | **Low** | Normal | Low |
Complications: hydrocephalus, brain abscess, cranial nerve palsies, seizures, deafness. Bacterial meningitis is an emergency: **antibiotics at once**, droplet isolation (meningococcus), fluids, seizure care.

**Encephalitis:** inflammation of brain tissue - fever, headache, altered consciousness, seizures, focal signs. Causes: **herpes simplex** (temporal lobes; treat with acyclovir), **Japanese encephalitis** (mosquito, pigs; vaccine available in India), rabies (Negri bodies), measles.

**Stroke (cerebrovascular accident):** sudden focal neurological deficit from vascular cause.
- **Ischaemic (about 85%):** thrombosis on atheroma or embolism (atrial fibrillation, recent MI); brain shows liquefactive necrosis (infarct).
- **Haemorrhagic (about 15%):** intracerebral (hypertension; basal ganglia) or **subarachnoid** (rupture of berry aneurysm; sudden "worst headache of life").
- *Risk factors:* hypertension, diabetes, smoking, atrial fibrillation, high cholesterol.
- *Features (FAST):* Face droop, Arm weakness, Speech difficulty, Time - sudden weakness of one side, loss of speech, vision. Transient ischaemic attack (TIA) resolves within 24 hours and is a warning.
- CT scan separates the two types; clot-dissolving therapy only for ischaemic stroke within 4.5 hours.

**Tumours of the CNS:** headache worse in the morning, vomiting, papilloedema (raised intracranial pressure), seizures, focal deficits.
| Tumour | Points |
|---|---|
| **Glioma** (astrocytoma) | Commonest primary; glioblastoma is the most malignant, "butterfly" spread, necrosis |
| **Meningioma** | Benign, from arachnoid, women, psammoma bodies, slow |
| Medulloblastoma | Children, cerebellum |
| Schwannoma (acoustic neuroma) | 8th nerve, deafness |
| Pituitary adenoma | Hormone excess, visual field loss |
| **Metastases** | More common than primary tumours (lung, breast) |
Primary brain tumours rarely spread outside the CNS.
""", dots=[(S + r'"Stroke"->"Ischaemic (85%)"->"Thrombosis or embolism";"Stroke"->"Haemorrhagic (15%)"->"Intracerebral (hypertension)\nor subarachnoid (aneurysm)"}', "Types of stroke")],
     example="A 65-year-old hypertensive man suddenly develops right arm weakness, facial droop and slurred speech: stroke. The nurse notes the time of onset, keeps him nil by mouth until swallowing is assessed, positions to protect the airway and arranges an urgent CT. "
             "A child with fever, headache, vomiting and neck stiffness needs immediate lumbar puncture and antibiotics for suspected bacterial meningitis."),
]

P4 = dict(
    id="P4", subject="Pathology", title="Unit IV - Special Pathology (genitourinary, breast, CNS)", hrs=5, topics=TOPICS,
    mcq=[
        ("Acute post-streptococcal glomerulonephritis typically presents with", ["Haematuria, oedema and hypertension", "Massive proteinuria only", "Polyuria and polydipsia", "Painless jaundice"], 0),
        ("Commonest type of renal calculus", ["Uric acid", "Calcium oxalate", "Cystine", "Struvite"], 1),
        ("Commonest organism causing cystitis and acute pyelonephritis", ["Streptococcus", "Escherichia coli", "Pseudomonas", "Candida"], 1),
        ("Cryptorchidism increases the risk of", ["Prostate cancer", "Testicular germ cell tumour (seminoma)", "Penile cancer", "Renal cell carcinoma"], 1),
        ("Benign prostatic hyperplasia arises mainly in the", ["Peripheral zone", "Periurethral (transition) zone", "Seminal vesicle", "Testis"], 1),
        ("HPV types most associated with cervical cancer", ["6 and 11", "16 and 18", "31 only", "1 and 2"], 1),
        ("'Bunch of grapes' appearance of swollen villi is seen in", ["Choriocarcinoma", "Hydatidiform mole", "Dermoid cyst", "Fibroid"], 1),
        ("Commonest benign tumour of the breast in young women", ["Fibrocystic change", "Fibroadenoma", "Phyllodes tumour", "Duct papilloma"], 1),
        ("CSF in bacterial meningitis shows", ["Lymphocytes and normal glucose", "Neutrophils, high protein, low glucose", "Clear fluid with normal protein", "Red cells only"], 1),
        ("Sudden 'worst headache of life' suggests", ["Ischaemic infarct", "Subarachnoid haemorrhage", "Meningioma", "Viral meningitis"], 1),
    ],
    long=[
        ("Define glomerulonephritis. Describe acute post-streptococcal GN: cause, pathology and clinical features. (PYQ pattern)",
         "Nephritic vs nephrotic; strep infection, immune complexes, low C3; haematuria, oedema, hypertension; recovery vs chronic GN."),
        ("Define renal failure. Differentiate acute and chronic renal failure with causes and features. (PYQ pattern)",
         "AKI phases (pre-renal, renal, post-renal); CKD causes and GFR; uraemia, anaemia, hyperkalaemia; dialysis and transplant."),
        ("Describe the pathology of carcinoma of the cervix, with risk factors and screening. (PYQ pattern)",
         "HPV 16/18; CIN I-III to invasive squamous carcinoma; features; spread; Pap smear, VIA, vaccine."),
        ("Describe carcinoma of the breast: risk factors, types, spread and diagnosis. (Important topic)",
         "Risk factors and BRCA; ductal carcinoma; upper outer quadrant; peau d'orange; nodes and bone; triple assessment."),
        ("Define meningitis. Describe causes, features and CSF findings. (Important topic)",
         "Bacterial, viral, TB; triad, Kernig and Brudzinski; CSF comparison table; complications; emergency management."),
    ],
    imp=["Glomerulonephritis and renal failure", "Renal calculi and pyelonephritis", "BPH and carcinoma prostate", "Carcinoma cervix (HPV, screening)", "Hydatidiform mole and choriocarcinoma", "Carcinoma breast", "Meningitis and stroke"],
)