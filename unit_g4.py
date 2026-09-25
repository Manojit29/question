S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Cancer genetics: familial cancer", imp=True, txt="""
Most cancers are **sporadic** (acquired somatic mutations over a lifetime, no strong family pattern). About **5-10% of cancers are hereditary**, caused by a **germline mutation** inherited from a parent, usually as autosomal dominant with reduced penetrance.

**Two-hit hypothesis (Knudson):** a tumour suppressor gene needs **both copies** to be inactivated for cancer to develop. In hereditary cancer, the person is **born with one already-mutated copy** (first hit) in every cell, so only **one further somatic hit** is needed in any cell to trigger cancer - explaining why hereditary cancers occur **earlier in life**, are often **bilateral or multiple**, and cluster in families, compared with sporadic cancer which needs two separate somatic hits in the same cell (rare, so it occurs later and is usually single).

**Key hereditary cancer syndromes**
| Syndrome / gene | Cancers | Features |
|---|---|---|
| **BRCA1 / BRCA2** | Breast, ovarian (also prostate, pancreatic) | Early-onset, often bilateral breast cancer; strong family history |
| **Li-Fraumeni (p53)** | Breast, sarcoma, brain, leukaemia, adrenal | Multiple different cancers at a young age in the same family |
| **Lynch syndrome (HNPCC)** | Colorectal, endometrial | Mismatch-repair genes; early colorectal cancer without many polyps |
| **Familial adenomatous polyposis (FAP), APC gene** | Colorectal | Hundreds to thousands of colon polyps from adolescence; colorectal cancer almost inevitable without colectomy |
| **Retinoblastoma (RB1)** | Retinoblastoma | Hereditary form is often bilateral, in infancy |
| MEN 1 and MEN 2 | Multiple endocrine tumours | Parathyroid, pancreas, thyroid (medullary), adrenal (phaeochromocytoma) |

**Warning features of a hereditary cancer in a family history:** cancer at a young age, the same type of cancer in several close relatives, bilateral or multiple primary cancers in one person, cancer in an unusual sex (for example male breast cancer), a known cancer-cluster syndrome.

**Nursing role:** take a detailed three-generation family history of cancer, recognise warning features, refer for genetic counselling and testing, support decisions about **surveillance** (earlier and more frequent screening), **risk-reducing surgery** (for example prophylactic mastectomy/oophorectomy in BRCA carriers), and provide emotional support, since genetic cancer risk affects the whole family, not just the person tested.
""", dots=[(S + r'"Hereditary cancer:\nborn with 1st hit\nin every cell"->"Only 1 more hit\nneeded in any cell"->"Cancer at younger age,\noften multiple/bilateral";'
                r'"Sporadic cancer:\nno inherited hit"->"Needs 2 hits in the\nsame cell (rare)"->"Cancer usually later,\nsingle"}', "Knudson's two-hit hypothesis: hereditary vs sporadic cancer")],
     example="A 32-year-old woman with breast cancer whose mother and aunt also had breast and ovarian cancer at a young age is referred for BRCA testing; if positive, her sisters are offered testing and, if also positive, earlier mammography or risk-reducing surgery is discussed."),
dict(t="2. Inborn errors of metabolism", imp=True, txt="""
**Definition:** inherited (usually **autosomal recessive**) defects of a single enzyme in a metabolic pathway, causing build-up of a toxic substrate, deficiency of an essential product, or both. Individually rare, but collectively an important cause of illness and death in infants and children, and some persist or first appear in adolescence/adulthood.

**Presentation:** often normal at birth, then, after starting feeds, **poor feeding, vomiting, lethargy, seizures, unusual odour, failure to thrive, developmental delay or regression**; some present later in childhood or adult life with milder or episodic symptoms (triggered by fasting, infection or specific foods).

| Disorder | Enzyme / defect | Key features | Management |
|---|---|---|---|
| **Phenylketonuria (PKU)** | Phenylalanine hydroxylase | Intellectual disability, seizures, fair skin/hair, musty odour, eczema | Lifelong **low-phenylalanine diet**, detected on newborn screening |
| **Galactosaemia** | Galactose-1-phosphate uridyltransferase | Vomiting, jaundice, liver failure, cataract, *E. coli* sepsis after milk feeds | **Lactose/galactose-free diet** from birth |
| **Maple syrup urine disease** | Branched-chain ketoacid dehydrogenase | Sweet, "maple syrup" smelling urine; poor feeding, lethargy, seizures | Restrict branched-chain amino acids (leucine, isoleucine, valine) |
| **Glycogen storage disease (von Gierke, type I)** | Glucose-6-phosphatase | Severe hypoglycaemia, hepatomegaly, growth failure | Frequent feeding, cornstarch therapy |
| **Tay-Sachs disease** | Hexosaminidase A | Progressive neurodegeneration, **cherry-red spot** on macula, exaggerated startle; fatal in early childhood | No cure; supportive care; carrier screening important (higher frequency in some populations) |
| **Wilson's disease** | ATP7B (copper transport) | Copper accumulation in liver and brain; **Kayser-Fleischer rings**, liver disease, tremor, psychiatric symptoms; **presents in adolescence/young adulthood** | Copper-chelating drugs (penicillamine), zinc, low-copper diet |
| **Alkaptonuria** | Homogentisate oxidase | Urine darkens on standing/exposure to air; black pigmentation of cartilage (ochronosis), arthritis in adulthood | No specific cure; symptomatic |

**Nursing role:** recognise early warning signs, support strict dietary therapy and monitoring, provide genetic counselling for future pregnancies, and give emotional support, since many of these conditions need lifelong, demanding management.
""", dots=[(S + r'"Enzyme defect\n(inherited)"->"Toxic substrate\naccumulates\nor product missing"->"Organ and brain\ndamage if untreated"->"Early detection\nand treatment\n(diet, drugs)"->"Prevented or\nreduced damage"}', "General pattern of an inborn error of metabolism")],
     example="A breastfed newborn who was well for the first few days develops vomiting, jaundice and lethargy and is found to have galactosaemia; strict avoidance of all milk and lactose from then on prevents further liver and brain damage. "
             "A teenager with tremor, liver disease and a golden-brown ring around the cornea is found to have Wilson's disease."),
dict(t="3. Blood group alleles and haematological genetic disorders", imp=True, txt="""
(Multiple alleles of the ABO system and Rh inheritance were covered under Mendelian inheritance in Unit I; here the focus is on inherited **haematological disease**, common and important in India.)

**Thalassaemia:** reduced or absent synthesis of a globin chain of haemoglobin (autosomal recessive).
- **Beta-thalassaemia trait (minor):** one abnormal gene; usually asymptomatic or mild anaemia; important because two trait carriers marrying have a **25% risk per pregnancy of beta-thalassaemia major**.
- **Beta-thalassaemia major:** both genes abnormal; presents in infancy with **severe anaemia, failure to thrive, hepatosplenomegaly, bony deformities ("chipmunk facies", from marrow expansion)**; needs **lifelong blood transfusion** and **iron chelation therapy** (to prevent transfusion-related iron overload damaging the heart, liver and endocrine glands); curative option is bone marrow/stem cell transplant.
- **Prevention:** **premarital and antenatal carrier screening** (especially important given the high carrier rate in parts of India), genetic counselling of carrier couples, prenatal diagnosis if both partners are carriers.

**Sickle cell disease:** point mutation in beta-globin (glutamic acid to valine, see Unit I); autosomal recessive; red cells sickle under low oxygen, causing haemolysis and **vaso-occlusion**.
- Features: chronic haemolytic anaemia, recurrent **painful vaso-occlusive crises**, dactylitis (hand-foot swelling) in infants, increased infection risk (functional asplenia), stroke risk in children, acute chest syndrome.
- Sickle cell **trait** (carrier) is usually asymptomatic but can occasionally cause problems at very low oxygen (high altitude, severe dehydration).
- Management: hydration, pain relief, folic acid, vaccination and prophylactic penicillin in children, hydroxyurea, blood transfusion for severe crises; carrier screening and counselling are important, as with thalassaemia.

**Haemophilia A and B:** X-linked recessive deficiency of factor VIII (A) or factor IX (B); covered in Unit I inheritance patterns; recurrent joint and muscle bleeding, prolonged APTT, treated with factor replacement.

**G6PD deficiency:** X-linked; red cells are vulnerable to oxidative stress; **haemolysis triggered by certain drugs (antimalarials, sulfonamides), fava beans, and infection**; important to screen before giving oxidant drugs in known or at-risk populations.
""", dots=[(S + r'"Carrier (trait)\nfather"->"25% normal";"Carrier (trait)\nfather"->"50% carrier (trait)";"Carrier (trait)\nfather"->"25% affected (major)";'
                r'"Carrier (trait)\nmother"->"25% normal";"Carrier (trait)\nmother"->"50% carrier (trait)";"Carrier (trait)\nmother"->"25% affected (major)"}', "Risk when both parents carry beta-thalassaemia trait")],
     example="A young couple, both found to have beta-thalassaemia trait on a routine premarital blood test, are counselled that each pregnancy carries a 25% risk of thalassaemia major and are offered prenatal diagnosis in future pregnancies. "
             "A child with recurrent painful swelling of the hands and a known family history of sickle cell disease is investigated and confirmed to have sickle cell disease on haemoglobin electrophoresis."),
dict(t="4. Genetic haemochromatosis", imp=True, txt="""
**Definition:** an inherited disorder of **excess iron absorption and accumulation** in the body, most often **autosomal recessive** (commonly linked to mutations in the **HFE gene**, especially in populations of European descent, though it is described in other populations too).

**Mechanism:** the normal regulatory control of intestinal iron absorption fails, so iron is absorbed in excess over many years and is progressively deposited in the liver, heart, pancreas, joints, skin and endocrine glands, causing organ damage from iron toxicity.

**Clinical features (usually appear in mid-adulthood, often later in women because menstrual blood loss delays iron build-up):**
- **Liver:** hepatomegaly, fibrosis, cirrhosis, increased risk of hepatocellular carcinoma.
- **Pancreas:** diabetes mellitus ("bronze diabetes" - the classic description combining skin pigmentation and diabetes).
- **Skin:** slate-grey or bronze pigmentation.
- **Heart:** cardiomyopathy, arrhythmias, heart failure.
- **Joints:** arthropathy, especially of the small joints of the hand.
- **Endocrine:** hypogonadism, other hormone deficiencies.

**Diagnosis:** raised **serum ferritin** and **transferrin saturation**; confirmed by genetic testing (HFE mutation analysis) and, if needed, liver biopsy to assess iron loading and damage.

**Management:** regular **therapeutic phlebotomy (venesection)** - removing blood regularly to reduce total body iron - is the mainstay and, started early, allows a normal life expectancy; iron-chelating drugs are used if venesection is not possible; a low-iron diet and avoidance of alcohol and vitamin C supplements (which increase iron absorption) are advised; screening of first-degree relatives is important since early treatment before organ damage occurs gives the best outcome.
""", example="A 45-year-old man presents with fatigue, joint pains, new-onset diabetes and bronze-coloured skin; markedly raised ferritin and transferrin saturation lead to a diagnosis of genetic haemochromatosis, and he is started on regular phlebotomy, with his siblings also offered screening."),
dict(t="5. Huntington's disease", imp=True, txt="""
**Definition:** a progressive, fatal, inherited **neurodegenerative disorder** affecting movement, cognition and behaviour.

**Genetics:** **autosomal dominant**, caused by an expanded **CAG trinucleotide repeat** in the **HTT (huntingtin) gene** on chromosome 4 (the same type of mutation mechanism introduced in Unit I under "triplet repeat expansion"). A person with one affected parent has a **50% risk** of inheriting the expanded gene. The disease shows **anticipation**: the repeat can lengthen further when passed on (especially through the father), so **onset tends to occur earlier and disease can be more severe in successive generations**.

**Onset and course:** typically appears in **mid-adulthood (commonly 30-50 years)**, though juvenile forms occur with a very large repeat expansion; it is relentlessly progressive over 15-20 years, and there is currently **no cure**.

**Clinical features**
- **Movement:** **chorea** (involuntary, jerky, dance-like movements), progressing to rigidity and bradykinesia in later stages; impaired coordination and gait.
- **Cognitive:** progressive dementia, impaired judgement and planning.
- **Psychiatric:** depression, irritability, personality change, psychosis; **depression and suicide risk are significant** and need active attention.
- Progressive difficulty with speech and swallowing in later stages; eventual complete dependence for care.

**Diagnosis:** clinical features plus family history; confirmed by **genetic testing for the CAG repeat expansion**. **Predictive (presymptomatic) testing** is available for at-risk relatives who are currently well, but is offered only with **extensive pre- and post-test genetic counselling**, given the profound psychological, social and insurance/employment implications of learning one carries a fatal, currently untreatable gene - many at-risk people choose not to be tested.

**Nursing and family care:** there is no cure, so care is supportive and symptomatic - medication for chorea and psychiatric symptoms, physiotherapy and occupational therapy, speech and swallowing support, nutritional care, safety measures as coordination declines, and psychological support for both the patient and the family, who face the emotional burden of a progressive, hereditary, fatal disease affecting multiple family members over generations.
""", dots=[(S + r'"Parent with expanded\nCAG repeat (HTT gene)"->"50% risk to\neach child"->"Repeat can lengthen\nfurther (anticipation)"->"Earlier onset,\nmore severe in\nnext generation"}', "Inheritance and anticipation in Huntington's disease")],
     example="A 40-year-old man whose father died of Huntington's disease develops clumsiness, irritability and jerky involuntary movements; genetic testing confirms an expanded CAG repeat. His adult children are offered predictive testing only after detailed genetic counselling, since each has a 50% risk and the decision to test carries major emotional and practical consequences."),
dict(t="6. Genetic factors in mental illness", imp=True, txt="""
Most common mental illnesses are **not caused by a single gene** but are **multifactorial (polygenic)**: many genes of small effect combine with environmental factors (stress, trauma, substance use, prenatal factors) to produce the disease. Family and twin studies show a clear genetic contribution, but inheritance does not follow simple Mendelian patterns for most conditions.

**Evidence for a genetic component**
- **Family studies:** risk of schizophrenia or bipolar disorder is several times higher in first-degree relatives of an affected person than in the general population.
- **Twin studies:** higher concordance (both twins affected) in **identical (monozygotic)** twins than in **non-identical (dizygotic)** twins, for schizophrenia, bipolar disorder, autism and major depression - this pattern is strong evidence for genetic influence, while the fact that concordance is well below 100% even in identical twins shows environment also matters.
- **Adoption studies:** children of an affected biological parent, even when raised by unaffected adoptive parents, still show increased risk - supporting a genetic rather than purely environmental cause.

**Conditions with a recognised genetic contribution:** schizophrenia, bipolar disorder, major depression, autism spectrum disorder, attention-deficit/hyperactivity disorder (ADHD), and some forms of intellectual disability linked to specific genetic syndromes (for example Fragile X syndrome, Down syndrome).

**Important distinction:** while genetics contributes to *risk*, it is only one factor among several, and having an affected relative does **not mean a person will definitely develop the illness** - this is an important point for patient and family education, to reduce fear, fatalism and stigma.

**Role of genetic counselling in psychiatric/mental illness:** helping families understand that risk is generally modest and not a certainty, that these are complex multifactorial conditions and not simple inherited traits, and that early recognition and treatment substantially improve outcome regardless of genetic contribution.

**Nursing role:** avoid stigmatising language, provide accurate information about multifactorial (not simple) inheritance to reduce unnecessary fear in families, encourage early help-seeking in at-risk family members rather than fatalistic avoidance, and support families dealing with a hereditary mental illness with the same care and respect given to any other genetic condition.
""", example="A young woman whose father has schizophrenia is worried that she is 'certain' to develop it too; the nurse explains that while her risk is higher than average because of the genetic contribution, schizophrenia is multifactorial, most relatives of affected people never develop it, and early recognition and support are what matter most if any symptoms do appear."),
]

G4 = dict(
    id="G4", subject="Genetics", title="Unit IV - Genetic conditions of adolescents and adults", hrs=2, topics=TOPICS,
    mcq=[
        ("According to Knudson's two-hit hypothesis, hereditary cancer occurs earlier because", ["Two somatic hits are needed in the same cell", "One hit is already present at birth, so only one further hit is needed", "It is always due to a chromosomal trisomy", "It never involves tumour suppressor genes"], 1),
        ("The gene most associated with hereditary breast and ovarian cancer is", ["APC", "BRCA1/BRCA2", "RB1", "HFE"], 1),
        ("Newborn screening test for phenylketonuria detects a defect in", ["Galactose-1-phosphate uridyltransferase", "Phenylalanine hydroxylase", "Glucose-6-phosphatase", "Hexosaminidase A"], 1),
        ("Kayser-Fleischer rings are characteristic of", ["Tay-Sachs disease", "Wilson's disease", "Galactosaemia", "Alkaptonuria"], 1),
        ("Two beta-thalassaemia trait carriers have, in each pregnancy, a risk of thalassaemia major of", ["10%", "25%", "50%", "75%"], 1),
        ("Sickle cell disease results from a mutation in", ["Alpha-globin", "Beta-globin", "Factor VIII", "HFE gene"], 1),
        ("'Bronze diabetes' with hepatomegaly and skin pigmentation suggests", ["Wilson's disease", "Genetic haemochromatosis", "Thalassaemia major", "Sickle cell disease"], 1),
        ("The mainstay treatment of genetic haemochromatosis is", ["Iron supplementation", "Regular therapeutic phlebotomy", "Bone marrow transplant", "Low-protein diet"], 1),
        ("Huntington's disease is inherited in which pattern, with what molecular change?", ["Autosomal recessive, gene deletion", "Autosomal dominant, CAG trinucleotide repeat expansion", "X-linked recessive, point mutation", "Mitochondrial inheritance"], 1),
        ("Twin studies showing higher concordance in monozygotic than dizygotic twins for schizophrenia mainly demonstrate", ["A purely environmental cause", "A genetic contribution to risk", "A single dominant gene cause", "No relationship to genetics at all"], 1),
    ],
    long=[
        ("Describe hereditary cancer syndromes and explain Knudson's two-hit hypothesis. (PYQ pattern)",
         "Sporadic vs hereditary cancer; two-hit hypothesis explained; BRCA1/2, Lynch, FAP, Li-Fraumeni table; warning features in family history; nursing role in counselling and surveillance."),
        ("Define inborn errors of metabolism. Describe PKU and galactosaemia with their management. (PYQ pattern)",
         "General pattern - enzyme defect, substrate build-up; PKU (phenylalanine hydroxylase, diet); galactosaemia (enzyme, features, lactose-free diet); newborn screening link; nursing role."),
        ("Describe the genetics, clinical features and management of beta-thalassaemia. (Important topic)",
         "Autosomal recessive; trait vs major; 25% risk of two carriers; features of major (anaemia, hepatosplenomegaly, bone changes); transfusion and chelation; premarital/antenatal screening and counselling."),
        ("Describe the cause, clinical features and management of genetic haemochromatosis. (Important topic)",
         "Autosomal recessive, HFE gene; excess iron absorption; organ effects (liver, pancreas, heart, skin, joints); diagnosis (ferritin, transferrin saturation); phlebotomy; family screening."),
        ("Describe Huntington's disease: genetics, clinical features and nursing management. (PYQ pattern)",
         "Autosomal dominant, CAG repeat expansion, anticipation; chorea, dementia, psychiatric features; predictive testing and counselling; supportive nursing and family care."),
    ],
    imp=["Cancer genetics (Knudson two-hit, BRCA)", "Inborn errors: PKU, galactosaemia", "Thalassaemia and sickle cell disease", "Genetic haemochromatosis", "Huntington's disease", "Genetic contribution to mental illness"],
)