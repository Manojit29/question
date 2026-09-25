S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Genetic testing", imp=True, txt="""
**Definition:** laboratory analysis of DNA, RNA, chromosomes, proteins or metabolites to detect a genetic condition, a carrier state, or an inherited risk.

**Types of genetic testing** (by purpose, not by lab method)
| Type | Purpose | Example |
|---|---|---|
| **Diagnostic testing** | Confirm or rule out a suspected genetic disorder in a symptomatic person | Karyotype in a dysmorphic infant |
| **Carrier testing** | Detect a recessive or X-linked allele in a healthy person, mainly for reproductive planning | Thalassaemia carrier screening before marriage |
| **Prenatal testing** | Detect a disorder in the fetus | Amniocentesis, CVS, NIPT (covered in Unit II) |
| **Newborn screening** | Detect a treatable disorder soon after birth | Guthrie test for PKU, hypothyroidism (Unit III) |
| **Predictive / presymptomatic testing** | Detect a gene for a disease that has **not yet appeared** in a currently healthy at-risk person | BRCA testing in an unaffected relative; Huntington's predictive testing |
| **Pharmacogenetic testing** | Predict response to, or risk of side effects from, a drug based on genetic make-up | Testing before certain chemotherapy or anti-epileptic drugs |
| **Preimplantation genetic testing** | Testing embryos created by IVF before transfer to the uterus | For couples at high risk of a serious single-gene disorder |

**Methods (brief):** karyotyping (chromosome number/structure), **FISH** (fluorescence in situ hybridisation, detects specific chromosome regions), PCR-based mutation analysis, DNA sequencing, biochemical/enzyme assays.

**Key general principles**
- Genetic testing should always be **voluntary**, based on **informed consent**, and, wherever a serious or life-changing result is possible, accompanied by **pre-test and post-test genetic counselling**.
- A test result affects not just the individual but **potentially the whole biological family**, which raises unique ethical questions (discussed later in this unit).
- **Predictive testing for an untreatable adult-onset disease** (such as Huntington's) needs particularly careful counselling, since a positive result cannot be "undone" and has major psychological and social implications; testing of children for adult-onset conditions with no childhood benefit is generally discouraged until the person is old enough to decide for themselves.
""", dots=[(S + r'"Reason for testing"->"Diagnostic\n(symptomatic)";"Reason for testing"->"Carrier\n(reproductive planning)";"Reason for testing"->"Prenatal\n(fetus)";'
                r'"Reason for testing"->"Newborn screening\n(treatable disorder)";"Reason for testing"->"Predictive\n(healthy, at risk)"}', "Types of genetic testing by purpose")],
     example="A healthy 30-year-old woman whose sister has confirmed Huntington's disease requests predictive testing for herself; she is first given extensive genetic counselling to help her consider the implications of a positive result before deciding whether to proceed."),
dict(t="2. Gene therapy", imp=True, txt="""
**Definition:** treatment that introduces, replaces, corrects, or silences genetic material within a person's cells to treat or prevent disease, rather than treating only the resulting symptoms.

**Broad approaches**
1. **Gene addition/replacement:** a normal copy of a gene is delivered into cells to compensate for a faulty or missing gene (commonly using a modified, harmless **viral vector** to carry the gene into cells).
2. **Gene editing:** newer technology (for example **CRISPR-Cas9**) that can directly correct a specific mutation in the DNA sequence itself, rather than just adding an extra copy.
3. **Gene silencing:** switches off or reduces the activity of a harmful gene (for example in some dominant disorders where the abnormal gene product itself is toxic).

**Somatic vs germline gene therapy**
| | Somatic gene therapy | Germline gene therapy |
|---|---|---|
| Target cells | Body (non-reproductive) cells of the patient | Reproductive cells or early embryo |
| Effect | Affects only the treated patient | Would be passed on to future generations |
| Current status | Used and approved for specific conditions | Not currently permitted in clinical practice in most countries because of unresolved safety and ethical concerns |

**Examples of conditions where gene therapy has been developed or is being researched:** certain inherited forms of blindness, spinal muscular atrophy, some inherited immune deficiencies ("bubble baby" disease), haemophilia, and some inherited blood disorders such as sickle cell disease and thalassaemia (using gene addition or gene-editing approaches).

**Challenges and limitations:** delivering the gene efficiently and safely to the right cells, the body's immune response against the vector, the high cost of currently available therapies, ensuring the effect is long-lasting, and the need for long-term follow-up to detect any late complications (for example a small risk of the inserted gene disrupting another important gene).

**Nursing role:** provide accurate information to patients and families about what gene therapy can currently offer (its still-limited but growing role) and what it cannot yet do, support patients through often long and demanding treatment/trial protocols, and help address unrealistic expectations sometimes created by media coverage of gene therapy.
""", dots=[(S + r'"Faulty or missing\ngene"->"Deliver normal gene\n(vector) or edit DNA\n(CRISPR)"->"Corrected gene\nfunction in target cells"->"Disease treated\nor prevented"}', "General principle of gene therapy")],
     example="A child with an inherited severe immune deficiency receives gene therapy in which a corrected copy of the missing gene is delivered into her own stem cells in the laboratory, which are then returned to her body, restoring immune function over subsequent months."),
dict(t="3. Genetic counselling", imp=True, txt="""
**Definition (widely used definition, adapted from the National Society of Genetic Counselors):** the process of helping people understand and adapt to the medical, psychological and family implications of the genetic contribution to a disease.

**Purposes/goals of genetic counselling**
- Accurate diagnosis of the genetic condition in the family.
- Explaining the **pattern of inheritance and recurrence risk** in plain, understandable language.
- Explaining the **options available** - testing, prenatal diagnosis, reproductive choices, treatment, surveillance - **without directing the person toward any particular choice** (a core principle called **non-directiveness**).
- Supporting the person and family **psychologically** in adapting to the diagnosis and in decision-making.
- Providing information about relevant **support groups and resources**.

**The genetic counselling process typically includes**
1. **Detailed family history and construction of a pedigree** (three generations, as introduced in Unit I).
2. **Physical examination and review of relevant investigations.**
3. **Establishing or confirming the diagnosis**, sometimes with the aid of genetic testing.
4. **Risk assessment** - explaining the chance of the condition occurring or recurring.
5. **Information-giving** about the condition's natural history, available management, and reproductive/testing options.
6. **Psychological support and follow-up**, since the news can bring grief, guilt, anxiety or relief, and families often need more than one session to fully process the information.

**Who provides genetic counselling:** trained genetic counsellors, clinical geneticists, and, in many settings, appropriately trained nurses and other health professionals as part of a team, especially in obstetric, paediatric and oncology services.

**Indications for referral:** a couple with a child affected by a genetic or congenital disorder, a family history of a hereditary condition, consanguineous marriage, recurrent miscarriage, advanced maternal age, an abnormal prenatal screening result, and a personal or family history suggestive of hereditary cancer.
""", dots=[(S + r'"Family history\nand pedigree"->"Diagnosis confirmed\n(examination, tests)"->"Risk assessment"->"Explain options,\nnon-directively"->"Psychological support\nand follow-up"}', "Steps in the genetic counselling process")],
     example="A couple who have had one child with spina bifida are referred for genetic counselling before their next pregnancy; the counsellor explains the recurrence risk, the protective role of high-dose folic acid, and the option of a detailed anomaly scan, while leaving the final reproductive decision entirely to the couple."),
dict(t="4. Legal and ethical issues in genetics", imp=True, txt="""
Advances in genetic testing raise ethical questions that go beyond ordinary medical care, mainly because genetic information is **permanent, predictive, and shared with blood relatives** who did not themselves choose to be tested.

**Core ethical principles applied to genetics**
- **Autonomy:** the right of a person to decide, without coercion, whether or not to undergo genetic testing, and to make their own reproductive and treatment choices based on the results.
- **Informed consent:** a person must understand the purpose, benefits, limitations and possible implications of a test **before** agreeing to it - this is especially important in genetics because a result can have implications for the whole family, not only the person tested.
- **Confidentiality and privacy:** genetic information must be kept confidential; because a result also reveals information about blood relatives, situations can arise where a patient's confidentiality conflicts with a relative's "right to know" a risk that could affect their own health - such conflicts require very careful, case-by-case ethical judgement.
- **Non-discrimination:** concern that genetic information could be misused, for example by employers or insurance companies to discriminate against a person based on a genetic risk they carry but have not (or may never) develop symptoms of; many countries have specific laws to prevent such genetic discrimination.
- **Beneficence and non-maleficence:** testing and its use should aim to benefit the person and avoid harm, including psychological harm from receiving distressing information without adequate support.
- **Justice/equity:** ensuring genetic services (testing, counselling, treatment) are **fairly accessible**, and not available only to those who can afford them privately.

**Specific ethical dilemmas commonly discussed**
- **Testing of children** for adult-onset conditions that have no benefit to the child now (for example Huntington's disease) - generally discouraged until the child is old enough to make an informed decision themselves, except where early knowledge changes childhood management.
- **Prenatal diagnosis leading to a decision about continuing or ending a pregnancy** - a deeply personal decision, requiring balanced, non-directive information and respect for the family's own values and beliefs.
- **Sex selection** using prenatal testing is **illegal in India** (under the **PCPNDT Act - Pre-Conception and Pre-Natal Diagnostic Techniques Act**), reflecting strong ethical and social concern about misuse of prenatal genetic technology.
- **Disclosure to relatives** when a test reveals a risk relevant to family members who have not been tested themselves.
- **Genetic discrimination** in employment or insurance based on predictive test results.

**Nursing and legal responsibility:** nurses must maintain strict confidentiality of genetic information, ensure the person has given truly informed consent before any test or procedure, be aware of relevant national law (such as the PCPNDT Act in India), and act as a patient advocate when ethical conflicts arise, referring complex situations to genetic counsellors, ethics committees or senior clinicians as appropriate.
""", dots=[(S + r'"Genetic test result"->"Belongs to the\nindividual (autonomy,\nconfidentiality)";"Genetic test result"->"Also reveals risk to\nblood relatives"->"Possible conflict:\nconfidentiality vs\nrelative\'s right to know"}', "Why genetic information raises unique ethical questions")],
     example="A woman found to carry a BRCA1 mutation is reluctant to tell her sister, who could also be at risk; the healthcare team respects the woman's confidentiality while gently encouraging her, over time, to consider informing at-risk relatives so they too can access testing and counselling. "
             "A couple who reveal they only want to know the sex of the fetus to consider terminating a female pregnancy are firmly informed that sex determination and selection are illegal under the PCPNDT Act in India."),
dict(t="5. Role of the nurse in genetic services", imp=True, txt="""
The nurse is very often the **first point of contact** for a family facing a possible or confirmed genetic condition, and plays an important role across the whole genetic care pathway, even without being a specialist genetic counsellor.

**Key nursing responsibilities**
1. **History-taking and family assessment:** collecting a thorough three-generation family history and constructing a pedigree; recognising "red flag" patterns suggestive of a genetic condition (early-onset disease, multiple affected relatives, consanguinity).
2. **Identification and referral:** recognising infants, children or adults who may need genetic evaluation (dysmorphic features, developmental delay, a strongly suggestive family history) and referring promptly to genetic services.
3. **Patient and family education:** explaining, in simple and accurate language, the purpose of a proposed test, what a result can and cannot tell the family, and what the inheritance pattern and recurrence risk mean in practical terms - always reinforcing, not replacing, the information given by the geneticist or counsellor.
4. **Support during testing procedures:** preparing patients for procedures such as amniocentesis, CVS or blood sampling, ensuring informed consent has been obtained, and providing physical and emotional support before, during and after the procedure.
5. **Psychological and emotional support:** helping the family cope with a new diagnosis, which can bring grief, guilt, shock, anxiety or blame between parents; providing a calm, non-judgemental presence; connecting families to relevant support groups and resources.
6. **Advocacy:** representing the patient's and family's wishes and best interests within the healthcare team, and helping to protect their autonomy, confidentiality and right to make informed, un-coerced decisions.
7. **Coordinated, ongoing care:** since many genetic conditions require lifelong management (for example thalassaemia, cystic fibrosis, inherited metabolic disease), the nurse often provides continuity of care, monitoring, and follow-up over years, working closely with the wider multidisciplinary team (geneticist, counsellor, specialist physician, dietitian, social worker).
8. **Maintaining ethical and legal standards:** upholding confidentiality, obtaining and documenting informed consent, staying aware of relevant law such as the PCPNDT Act, and referring complex ethical situations appropriately.
9. **Community and preventive role:** promoting awareness of premarital and antenatal carrier screening (for example thalassaemia, sickle cell disease) in high-risk communities, promoting folic acid supplementation, participating in newborn screening programmes, and contributing to public health education about avoiding known teratogens.

In summary, the nurse's role spans **prevention, early identification, support through testing and diagnosis, ongoing care, education, and advocacy** - making the nurse a central and continuous presence in the genetic care of patients and families, even though specialised genetic counselling itself is usually provided by a trained genetic counsellor or clinical geneticist.
""", dots=[(S + r'"Family history\nand red-flag\nrecognition"->"Referral to\ngenetic services"->"Support through\ntesting/procedures"->"Education and\nemotional support"->"Long-term follow-up\nand advocacy"}', "The nurse's role across the genetic care pathway")],
     example="A community health nurse notices that several families in her area come from a community with a high rate of consanguineous marriage and a known cluster of thalassaemia; she organises awareness sessions on premarital blood testing, refers couples found to be carriers for genetic counselling, and supports affected families with ongoing transfusion and chelation therapy follow-up over the years."),
]

G5 = dict(
    id="G5", subject="Genetics", title="Unit V - Genetic services related to genetics and counselling", hrs=2, topics=TOPICS,
    mcq=[
        ("Testing an unaffected, currently healthy at-risk relative for a disease-causing gene is called", ["Diagnostic testing", "Predictive (presymptomatic) testing", "Newborn screening", "Carrier testing"], 1),
        ("Testing done before marriage to detect a recessive allele such as for thalassaemia is called", ["Predictive testing", "Carrier testing", "Diagnostic testing", "Pharmacogenetic testing"], 1),
        ("Gene therapy that is passed on to future generations if performed on reproductive cells is called", ["Somatic gene therapy", "Germline gene therapy", "Pharmacogenetic therapy", "Carrier therapy"], 1),
        ("A newer gene-editing technology that can directly correct a mutation in DNA is", ["Viral vector addition only", "CRISPR-Cas9", "Karyotyping", "FISH"], 1),
        ("A core principle of genetic counselling is that the counsellor should", ["Direct the family toward the counsellor's preferred choice", "Remain non-directive and support the family's own decision", "Insist on prenatal testing for every pregnancy", "Refuse to discuss recurrence risk"], 1),
        ("The first step in the genetic counselling process is usually", ["Prescribing treatment", "Taking a detailed family history and constructing a pedigree", "Performing gene therapy", "Reporting to authorities"], 1),
        ("Sex determination and sex selection using prenatal testing in India is regulated/prohibited under the", ["PCPNDT Act", "Right to Information Act", "Consumer Protection Act", "Mental Healthcare Act"], 0),
        ("Genetic information raises unique ethical concern mainly because it", ["Only affects the tested individual", "Also has implications for blood relatives who were not tested", "Is never confidential by law", "Cannot be misused"], 1),
        ("Testing children for an adult-onset condition with no childhood benefit, such as Huntington's disease, is generally", ["Recommended routinely in infancy", "Discouraged until the person can decide for themselves", "Required by law in most countries", "Only done for research purposes"], 1),
        ("A key role of the nurse in genetic services includes", ["Providing the final genetic diagnosis independently", "Taking family history, referring appropriately, and providing education and support", "Performing gene-editing procedures", "Making reproductive decisions for the family"], 1),
    ],
    long=[
        ("Describe the different types of genetic testing with examples of each. (PYQ pattern)",
         "Diagnostic, carrier, prenatal, newborn screening, predictive, pharmacogenetic, preimplantation; examples for each; general principles of consent and counselling."),
        ("Define gene therapy. Describe its approaches and differentiate somatic from germline gene therapy. (PYQ pattern)",
         "Gene addition, editing (CRISPR), silencing; somatic vs germline table; examples of conditions; challenges; nursing role in patient education."),
        ("Define genetic counselling. Describe its goals and the steps involved in the counselling process. (PYQ pattern)",
         "Definition; non-directiveness; steps - history/pedigree, diagnosis, risk assessment, information-giving, psychological support; indications for referral."),
        ("Discuss the legal and ethical issues involved in genetic testing and counselling. (Important topic)",
         "Autonomy, informed consent, confidentiality vs relatives' right to know, non-discrimination, justice; dilemmas - testing children, prenatal decisions, PCPNDT Act, sex selection; nursing responsibility."),
        ("Describe the role of the nurse in genetic services. (Important topic)",
         "History-taking and pedigree; identification and referral; education; support during procedures; psychological support; advocacy; long-term coordinated care; community/preventive role."),
    ],
    imp=["Types of genetic testing", "Predictive testing and its implications", "Gene therapy (somatic vs germline)", "Genetic counselling process and non-directiveness", "Ethical issues and PCPNDT Act", "Role of the nurse in genetic services"],
)