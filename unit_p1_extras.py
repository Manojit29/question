# One dict per topic of Unit I, in the same order as TOPICS. dots = [(graphviz DOT, caption)].
S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

EXTRAS = [
    dict(example="A 45-year-old woman has a breast lump removed. The nurse puts the specimen in 10% formalin within minutes, "
                 "labels the container (name, ID, site, date) and fills the requisition. A dry or unlabelled container lets the "
                 "tissue rot (autolysis), and the pathologist cannot give a reliable diagnosis."),
    dict(dots=[(S + r'"Cell injury"->"Reversible\n(swelling, fatty change)"->"Recovery";'
                    r'"Cell injury"->"Irreversible"->"Necrosis";"Irreversible"->"Apoptosis";'
                    r'"Necrosis"->"Coagulative, liquefactive,\ncaseous, fat, fibrinoid";'
                    r'"Necrosis"->"Gangrene\n(dry, wet, gas)"}', "Course of cell injury and its outcomes")],
         example="A diabetic man has a black, shrunken, painless toe with a sharp line between black and normal skin: dry gangrene "
                 "(arterial block). If the foot is swollen, foul-smelling and blistered with fever, it is wet gangrene and needs urgent "
                 "surgery. A cheese-like necrotic lymph node in a TB patient is caseous necrosis."),
    dict(dots=[(S + r'"Stress"->"Adaptation";"Adaptation"->"Atrophy\n(smaller)";"Adaptation"->"Hypertrophy\n(bigger cells)";'
                    r'"Adaptation"->"Hyperplasia\n(more cells)";"Adaptation"->"Metaplasia\n(cell type changes)"->"Dysplasia"->"Neoplasia\n(if stress persists)";'
                    r'"Adaptation"->"Injury / cell death"[label="stress too severe"]}', "Cellular adaptations")],
         example="A 50-year-old chronic smoker: bronchial columnar cells turn squamous (metaplasia), which can reverse if he quits. "
                 "If smoking continues, dysplasia and then carcinoma can follow. A hypertensive patient shows left ventricular "
                 "hypertrophy; the pregnant uterus shows both hypertrophy and hyperplasia."),
    dict(dots=[(S + r'"Tissue injury"->"Vasodilation"->"Increased permeability"->"Exudate and oedema";'
                    r'"Tissue injury"->"Margination"->"Emigration"->"Chemotaxis"->"Phagocytosis"->"Resolution, abscess,\nfibrosis or chronic"}',
                "Vascular (top) and cellular (bottom) events of acute inflammation")],
         example="A child steps on a nail. Within minutes the foot is red, warm and swollen (vasodilation, permeability) and painful. "
                 "By 6 to 24 hours neutrophils fill the wound; pus means suppurative inflammation, and an untreated collection becomes an abscess."),
    dict(dots=[(S + r'"Haemostasis\n(minutes)"->"Inflammation\n(to 3-5 days)"->"Proliferation:\ngranulation tissue\n(to 3 weeks)"->"Remodelling\n(weeks to months)"}',
                "Phases of wound healing")],
         example="A clean appendectomy wound with sutured edges heals by primary intention in 7 to 10 days. A diabetic heel ulcer heals by "
                 "secondary intention over weeks. A keloid can follow an ear piercing, with a scar growing beyond the original wound."),
    dict(dots=[(S + r'"Normal cell"->"Genetic damage\n(carcinogen)"->"Dysplasia"->"Carcinoma in situ"->"Invasion"->"Metastasis";'
                    r'"Metastasis"->"Lymphatic\n(carcinoma)";"Metastasis"->"Blood\n(sarcoma)";"Metastasis"->"Transcoelomic";"Metastasis"->"Implantation"}',
                "Development and spread of a malignant tumour")],
         example="A Pap smear detects carcinoma in situ of the cervix (CIN III) before invasion, so it is curable. Breast carcinoma spreads to "
                 "axillary lymph nodes (lymphatic route); osteosarcoma spreads to the lungs through the blood."),
    dict(dots=[(S + r'"Endothelial injury"->"Thrombus";"Stasis or turbulence"->"Thrombus";"Hypercoagulability"->"Thrombus";'
                    r'"Thrombus"->"Embolus";"Embolus"->"Pulmonary embolism\n(from leg veins)";"Embolus"->"Stroke, renal infarct\n(from heart)";'
                    r'"Thrombus"->"Organisation and\nrecanalisation"}', "Virchow's triad and the fate of a thrombus")],
         example="A woman on oral contraceptives develops a swollen calf after a long flight (deep vein thrombosis), then sudden breathlessness "
                 "and chest pain: pulmonary embolism. A man with a fractured femur becomes confused with petechiae on day 2: fat embolism. "
                 "A trauma patient with BP 80/50, pulse 130 and cold skin is in hypovolaemic shock."),
    dict(dots=[(S + r'"Raised venous pressure\n(heart failure)"->"Transudate\nprotein <3 g/dL";"Low albumin\n(nephrotic, cirrhosis)"->"Transudate\nprotein <3 g/dL";'
                    r'"Sodium and water\nretention"->"Transudate\nprotein <3 g/dL";"Inflammation\n(increased permeability)"->"Exudate\nprotein >3 g/dL";'
                    r'"Transudate\nprotein <3 g/dL"->"Oedema or effusion";"Exudate\nprotein >3 g/dL"->"Oedema or effusion"}', "Causes of oedema and the type of fluid formed")],
         example="A child with nephrotic syndrome has a puffy face in the morning (low albumin). An elderly man with heart failure has pitting ankle "
                 "oedema by evening and breathlessness lying flat. Pleural fluid with protein 4.5 g/dL and high LDH is an exudate (pneumonia, TB); "
                 "protein 2 g/dL is a transudate (heart failure)."),
]