S = 'digraph{rankdir=LR;node[shape=box,style="rounded,filled",fillcolor="#eef3f8",fontsize=11];'

TOPICS = [
dict(t="1. Introduction: genetics in nursing and its impact on families", imp=False, txt="""
**Genetics** is the study of heredity (transmission of traits from parents to offspring) and variation (differences between individuals).

**Basic terms:** *gene* (unit of heredity; a DNA segment coding for a protein or RNA), *genome* (all genetic material; about 3 billion base pairs and roughly 20,000 genes), *locus* (position of a gene), *allele* (alternative form of a gene), *genotype* (genetic make-up), *phenotype* (observed trait), *homozygous* (two identical alleles), *heterozygous* (two different alleles), *dominant* (expressed in heterozygote), *recessive* (expressed only in homozygote), *carrier* (heterozygote who does not show a recessive disease), *proband* (first affected person who brings the family to attention), *pedigree* (family tree).
**Genetic vs congenital vs familial:** *genetic* = caused by gene or chromosome change; *congenital* = present at birth (may or may not be genetic, e.g. rubella defects); *familial* = occurs in more than one family member (may be genetic or environmental).

**Classes of genetic disease:** chromosomal (Down syndrome), single-gene/Mendelian (cystic fibrosis), multifactorial (cleft lip, diabetes), mitochondrial.

**Application of genetics in nursing**
- Taking a **three-generation family history** and drawing a pedigree.
- Recognising signs of genetic disorders in newborns, children and adults.
- Educating about prenatal screening, newborn screening and carrier testing.
- Supporting informed decisions, consent, confidentiality and non-discrimination.
- Assisting genetic counselling and referral; caring for the patient with a genetic disorder.

**Impact of a genetic condition on the family:** shock, guilt and blame between parents; grief and anxiety; financial burden of long-term care; effect on siblings; stigma and social isolation; fear about future pregnancies and about testing relatives; decisions about marriage and reproduction; need for lifelong support. The nurse listens without judgement and links the family to counselling and support groups.
""", example="A woman comes for antenatal care and says her first baby had a heart defect and her brother has intellectual disability. The nurse draws a three-generation pedigree, notes the details and refers the couple for genetic counselling, while reassuring the mother that this is not her fault."),
dict(t="2. Cell division: mitosis and meiosis", imp=True, txt="""
**Cell cycle:** G1 (growth) -> **S** (DNA replication) -> G2 (preparation) -> **M** (mitosis and cytokinesis). Resting cells leave the cycle in G0.

**Mitosis** (somatic cells; growth, repair, replacement) - one division gives **2 genetically identical diploid (46) cells**.
1. *Prophase:* chromosomes condense, nuclear membrane breaks, spindle forms.
2. *Metaphase:* chromosomes line up on the equator.
3. *Anaphase:* **sister chromatids separate** and move to the poles.
4. *Telophase and cytokinesis:* nuclei re-form, cytoplasm divides.

**Meiosis** (germ cells; gametes) - two divisions give **4 genetically different haploid (23) cells**.
- *Meiosis I (reductional):* prophase I with **synapsis and crossing over** (exchange between homologous chromosomes); homologous pairs separate; 46 to 23 chromosomes.
- *Meiosis II (equational):* like mitosis; **chromatids separate**.
- Variation arises from **crossing over** and **independent assortment**.
- *Spermatogenesis:* one cell gives 4 sperms, continuous from puberty. *Oogenesis:* one cell gives **1 ovum and polar bodies**; begins before birth, arrested in prophase I until ovulation, finished only if fertilised.
- **Non-disjunction** = failure of chromosomes to separate; gives gametes with 24 or 22 chromosomes and causes trisomy or monosomy.

| Feature | Mitosis | Meiosis |
|---|---|---|
| Cells | Somatic | Germ cells |
| Divisions | One | Two |
| Daughter cells | 2, diploid | 4, haploid |
| Crossing over | No | Yes |
| Genetic identity | Identical | Different |
| Purpose | Growth, repair | Gametes, variation |
""", dots=[(S + r'"G1: growth"->"S: DNA\nsynthesis"->"G2: preparation"->"M: mitosis"->"G1: growth"}', "Cell cycle"),
           (S + r'"Diploid cell\n(46)"->"Meiosis I:\ncrossing over, pairs\nseparate"->"2 haploid cells\n(23, doubled)"->"Meiosis II:\nchromatids separate"->"4 haploid cells\n(23)"}', "Stages of meiosis")],
     example="A cut on the finger heals because skin cells divide by mitosis, giving identical daughter cells. A sperm and an egg, each with 23 chromosomes, are produced by meiosis, so the fertilised egg has 46 again."),
dict(t="3. DNA, genes and how they work", imp=True, txt="""
**DNA** (deoxyribonucleic acid): a **double helix** (Watson and Crick, 1953) of two antiparallel strands. A **nucleotide** = deoxyribose sugar + phosphate + nitrogenous base. Bases: **A pairs with T (2 hydrogen bonds), G pairs with C (3 bonds)**. The base sequence is the genetic code.
**RNA:** single strand, ribose sugar, **uracil** instead of thymine. Types: **mRNA** (carries the message), **tRNA** (brings amino acids), **rRNA** (part of ribosomes).

**Central dogma:** DNA -> (transcription, in nucleus) -> mRNA -> (translation, at ribosome) -> protein.
- A **codon** = 3 bases coding for one amino acid; 64 codons; AUG = start; UAA, UAG, UGA = stop; the code is degenerate (many amino acids have more than one codon).
- **Replication** is semi-conservative: each new DNA has one old and one new strand.

**Gene structure:** a stretch of DNA with a promoter (control), **exons** (coding parts) and **introns** (non-coding parts removed by splicing). Humans have about 20,000 genes; only about 1.5% of DNA codes for protein. Every person has two copies of each gene (one from each parent). Genes differ between individuals in tiny sequence variants (polymorphisms), and harmful variants cause disease.
""", dots=[(S + r'"DNA (gene)"->"mRNA"[label="transcription\n(nucleus)"];"mRNA"->"Protein"[label="translation\n(ribosome)"];"DNA (gene)"->"DNA (gene)"[label="replication"]}', "Flow of genetic information")],
     example="A single base change in the beta-globin gene alters one amino acid in haemoglobin and produces sickle cell disease, showing how a change in DNA becomes a change in protein and then in the patient."),
dict(t="4. Chromosomes and sex determination", imp=True, txt="""
Humans have **46 chromosomes = 23 pairs**: **22 pairs of autosomes** and **1 pair of sex chromosomes** (XX female, XY male). One of each pair comes from each parent.
**Structure:** two chromatids joined at the **centromere**; short arm **p**, long arm **q**. By centromere position: metacentric, submetacentric, acrocentric (chromosomes 13, 14, 15, 21, 22).
**Karyotype:** arrangement of chromosomes by size into groups A-G (banding stains such as G-banding). Made from blood lymphocytes (culture, arrest in metaphase), amniotic fluid cells or chorionic villi. Written as number, sex chromosomes, abnormality: **46,XY** normal male; **47,XX,+21** Down syndrome female.

**Sex determination**
- The egg always carries X; the **sperm carries X or Y**, so **the father's sperm decides the sex**.
- The **SRY gene** on the Y chromosome starts male development; without it the embryo becomes female.
- Chance of a boy or girl is 50% each.
- **Lyon hypothesis / X-inactivation:** in females one X is randomly inactivated in each cell; the inactive X is seen as a **Barr body** in the nucleus (number of Barr bodies = number of X chromosomes minus one). Normal female 1, normal male 0, Turner 0, Klinefelter 1.
- **Mitochondrial DNA** is inherited only from the mother.
""", dots=[(S + r'"Egg (22+X)"->"XX: girl";"Sperm (22+X)"->"XX: girl";"Egg (22+X)"->"XY: boy";"Sperm (22+Y)"->"XY: boy"}', "Sex is decided by the sperm")],
     example="A couple ask whether the mother 'caused' the birth of another girl. The nurse explains that the mother's egg always carries X, and only the father's sperm (X or Y) decides the baby's sex."),
dict(t="5. Chromosomal aberrations", imp=True, txt="""
**Numerical:** *euploidy* = complete sets (polyploidy: triploidy 69, incompatible with life); *aneuploidy* = one chromosome extra (**trisomy**, 47) or missing (**monosomy**, 45), mostly from **non-disjunction**; *mosaicism* = two cell lines.
**Structural:** deletion (cri-du-chat, 5p-), duplication, inversion, ring chromosome, **translocation** (Robertsonian 14;21 gives familial Down syndrome; Philadelphia chromosome t(9;22) in chronic myeloid leukaemia).

| Syndrome | Karyotype | Main features |
|---|---|---|
| **Down (trisomy 21)** | 47,XX or XY,+21 (95% non-disjunction, more with **maternal age over 35**) | Flat face, upslanting eyes, epicanthic folds, protruding tongue, single palmar (simian) crease, hypotonia, intellectual disability, heart defect (AV canal), duodenal atresia, leukaemia, early Alzheimer's |
| **Edwards (trisomy 18)** | 47,+18 | Rocker-bottom feet, clenched fists with overlapping fingers, small jaw, heart defects; most die in first year |
| **Patau (trisomy 13)** | 47,+13 | Cleft lip and palate, extra fingers (polydactyly), small eyes, brain malformation; early death |
| **Turner** | 45,X | Female; short stature, webbed neck, shield chest, streak ovaries, **primary amenorrhoea**, coarctation of aorta; normal intelligence; Barr body absent |
| **Klinefelter** | 47,XXY | Male; tall, small firm testes, infertility (azoospermia), gynaecomastia; Barr body present |
| Triple X / XYY | 47,XXX / 47,XYY | Often mild or unnoticed |
Risk of trisomy rises sharply with mother's age; diagnosis: karyotype, prenatal screening and amniocentesis.
""", dots=[(S + r'"Non-disjunction\nin meiosis"->"Gamete with 24 or\n22 chromosomes"->"Fertilised by\nnormal gamete"->"Trisomy (47) or\nmonosomy (45)"}', "How aneuploidy arises")],
     example="A 41-year-old primigravida is told that the risk of Down syndrome rises with age; the nurse explains screening (nuchal scan, blood tests) and the option of amniocentesis. A short girl with a webbed neck who has not started periods at 15 needs a karyotype: Turner syndrome (45,X)."),
dict(t="6. Mendel's laws and patterns of inheritance", imp=True, txt="""
**Gregor Mendel** (pea plants, 1865) is the **father of genetics**.
1. **Law of dominance:** in a heterozygote the dominant allele masks the recessive.
2. **Law of segregation:** the two alleles of a gene separate during gamete formation, so each gamete gets one.
3. **Law of independent assortment:** genes on different chromosomes are inherited independently.
- *Monohybrid cross* (Tt x Tt): phenotype **3 : 1**, genotype **1 : 2 : 1**. *Dihybrid cross:* **9 : 3 : 3 : 1**. *Test cross:* unknown dominant individual crossed with a homozygous recessive to reveal genotype.

| Pattern | How to recognise it | Risk | Examples |
|---|---|---|---|
| **Autosomal dominant** | Every generation (vertical), both sexes, one affected parent enough | **50%** each child | Huntington disease, Marfan, achondroplasia, neurofibromatosis, familial hypercholesterolaemia |
| **Autosomal recessive** | Skips generations, siblings, parents unaffected carriers, consanguinity | Carrier x carrier: **25% affected, 50% carriers, 25% normal** | Cystic fibrosis, sickle cell disease, thalassaemia, PKU, albinism, Tay-Sachs |
| **X-linked recessive** | Mostly males; no male-to-male transmission; passes through carrier females | Carrier mother: 50% sons affected, 50% daughters carriers | Haemophilia A and B, Duchenne muscular dystrophy, colour blindness, G6PD deficiency |
| X-linked dominant | Affected father passes to all daughters, no sons | - | Vitamin D-resistant rickets |
| Y-linked | Father to all sons | - | Rare |
| Mitochondrial | Mother to all children | - | Some myopathies |
| **Multifactorial** | Gene + environment | Recurrence 2-5% | Cleft lip, neural tube defect, diabetes, hypertension |
**Exceptions:** incomplete dominance, codominance, variable expressivity, reduced penetrance, genomic imprinting, anticipation.

**Pedigree symbols:** square male, circle female, filled = affected, half-filled = carrier, horizontal line = mating, double line = consanguineous mating, arrow = proband, diamond = sex unknown.
""", dots=[(S + r'"Carrier father (Aa)"->"AA: 25% normal";"Carrier father (Aa)"->"Aa: 50% carrier";"Carrier father (Aa)"->"aa: 25% affected";'
                r'"Carrier mother (Aa)"->"AA: 25% normal";"Carrier mother (Aa)"->"Aa: 50% carrier";"Carrier mother (Aa)"->"aa: 25% affected"}', "Autosomal recessive: risk in each pregnancy of two carriers"),
           (S + r'"Carrier mother (XHXh)"->"Normal son 25%";"Carrier mother (XHXh)"->"Affected son 25%";"Carrier mother (XHXh)"->"Normal daughter 25%";"Carrier mother (XHXh)"->"Carrier daughter 25%";'
                r'"Normal father (XHY)"->"Normal son 25%";"Normal father (XHY)"->"Affected son 25%";"Normal father (XHY)"->"Normal daughter 25%";"Normal father (XHY)"->"Carrier daughter 25%"}', "X-linked recessive: carrier mother and normal father")],
     example="Two healthy parents who are both cystic fibrosis carriers have a 1 in 4 chance of an affected child in every pregnancy. A healthy woman whose brother has haemophilia may be a carrier; each of her sons has a 50% chance of haemophilia."),
dict(t="7. Multiple alleles, blood groups and sex-linked inheritance", imp=True, txt="""
**Multiple alleles:** more than two alleles of one gene exist in the population, though each person has only two. Example: the **ABO blood group gene** with alleles **IA, IB and i**.
- IA and IB are **codominant** (both expressed in AB); both are dominant over i.
| Phenotype | Genotypes |
|---|---|
| A | IAIA or IAi |
| B | IBIB or IBi |
| AB | IAIB |
| O | ii |
**Rh factor:** D allele (Rh positive) dominant over d (Rh negative).

**Predicting children:** A x B (IAi x IBi) can give A, B, AB and O; **O x O gives only O**; **AB x O gives only A or B** (never AB or O); AB x AB gives A, B, AB. Blood groups can **exclude** paternity but never prove it.
**Clinical link:** an **Rh-negative mother with an Rh-positive fetus** can form anti-D antibodies and cause haemolytic disease in later pregnancies; prevention with **anti-D immunoglobulin** within 72 hours of delivery.

**Sex-linked (X-linked) inheritance**
- A male has only one X, so **one recessive allele is enough** to show the disease (hemizygous); females need two.
- **Father to son cannot pass an X-linked gene**; an affected father passes the allele to all his daughters (carriers).
- **Colour blindness** (red-green), **haemophilia A** (factor VIII), **Duchenne muscular dystrophy**, G6PD deficiency.
- A carrier mother: each son 50% affected; each daughter 50% carrier.
""", example="A mother with blood group O and a father with group AB will never have an AB or O child; a child with group A or B is possible. An Rh-negative mother delivering an Rh-positive baby gets anti-D injection within 72 hours."),
dict(t="8. Mutation and errors in transmission", imp=True, txt="""
**Mutation** = a permanent, heritable change in the DNA base sequence. Errors of transmission also include **non-disjunction** and translocations.
**Gene (point) mutations**
- *Substitution:* **silent** (no amino-acid change), **missense** (different amino acid; **sickle cell disease: glutamic acid to valine at position 6 of beta-globin, GAG to GTG**), **nonsense** (creates a stop codon; early termination).
- *Insertion or deletion:* not a multiple of 3 bases causes a **frameshift** (Tay-Sachs from insertion).
- *Triplet repeat expansion:* repeated 3-base sequences enlarge with each generation (**Huntington CAG, fragile X CGG**), causing **anticipation** (earlier and more severe disease in later generations).
**Chromosomal mutations:** deletion, duplication, translocation, inversion, aneuploidy.

**Germline vs somatic:** germline mutations (in sperm or egg) are passed to children; somatic mutations occur in body cells and may cause cancer but are not inherited.
**Causes:** *spontaneous* (errors in DNA copying); *induced* by **mutagens** - ionising radiation (X-rays, gamma), ultraviolet light, chemicals (tobacco smoke, benzene, mustard gas, nitrites), viruses, some drugs. Cells repair most DNA damage; failure of repair leads to disease (e.g. xeroderma pigmentosum).
**Effects:** most harmful or neutral; a few beneficial, which drives evolution.
**Nursing:** counsel about radiation protection in pregnancy, smoking cessation and avoiding known teratogens.
""", dots=[(S + r'"DNA change\n(mutation)"->"Point mutation";"Point mutation"->"Silent";"Point mutation"->"Missense\n(sickle cell)";"Point mutation"->"Nonsense";'
                r'"DNA change\n(mutation)"->"Insertion or deletion\n(frameshift)";"DNA change\n(mutation)"->"Triplet repeat\nexpansion\n(Huntington)"}', "Types of gene mutation")],
     example="A radiographer who is pregnant is moved away from X-ray duties because radiation is a mutagen. In sickle cell disease the codon GAG becomes GTG, replacing glutamic acid by valine, so the red cell sickles under low oxygen."),
]

G1 = dict(
    id="G1", subject="Genetics", title="Unit I - Nature, principles and perspectives of heredity", hrs=2, topics=TOPICS,
    mcq=[
        ("Number of chromosomes in a normal human somatic cell", ["23", "44", "46", "48"], 2),
        ("Crossing over occurs during", ["Prophase of mitosis", "Prophase I of meiosis", "Anaphase II", "Metaphase of mitosis"], 1),
        ("Meiosis produces", ["2 diploid cells", "4 haploid cells", "2 haploid cells", "4 diploid cells"], 1),
        ("The sex of the child is determined by the chromosome carried by the", ["Egg", "Sperm", "Both equally", "Placenta"], 1),
        ("Down syndrome is", ["45,X", "47,XXY", "Trisomy 21", "Trisomy 18"], 2),
        ("Karyotype 45,X is", ["Klinefelter syndrome", "Turner syndrome", "Down syndrome", "Edwards syndrome"], 1),
        ("Risk of an affected child in each pregnancy of two autosomal recessive carriers", ["0%", "25%", "50%", "100%"], 1),
        ("Haemophilia is inherited as", ["Autosomal dominant", "Autosomal recessive", "X-linked recessive", "Mitochondrial"], 2),
        ("A child of an AB mother and an O father cannot have blood group", ["A", "B", "AB", "None can be excluded"], 2),
        ("Sickle cell disease results from", ["Deletion of a chromosome", "A point mutation replacing glutamic acid by valine", "Trisomy", "A frameshift deletion"], 1),
    ],
    long=[
        ("Describe mitosis and meiosis and differentiate between them. (PYQ pattern)",
         "Stages of each; number and type of daughter cells; crossing over; significance; comparison table; non-disjunction."),
        ("Describe chromosomal aberrations with examples of numerical and structural changes. Write about Down syndrome. (PYQ pattern)",
         "Aneuploidy, euploidy, translocation, deletion; karyotype and features of Down, Turner, Klinefelter; maternal age; diagnosis."),
        ("State Mendel's laws and explain with a monohybrid cross. (PYQ pattern)",
         "Dominance, segregation, independent assortment; Tt x Tt Punnett; 3:1 and 1:2:1; dihybrid 9:3:3:1; test cross."),
        ("Describe autosomal dominant, autosomal recessive and X-linked patterns of inheritance with examples and risks. (Important topic)",
         "Recognition features; 50%, 25%, carrier mother; examples; pedigree symbols; multifactorial."),
        ("Define mutation. Describe its types, causes and significance. (Important topic)",
         "Point, frameshift, triplet repeat; sickle cell example; germline vs somatic; mutagens; effects."),
    ],
    imp=["Mitosis vs meiosis", "Chromosomal aberrations (Down, Turner, Klinefelter)", "Mendel's laws", "Patterns of inheritance with risks", "ABO blood group inheritance", "Mutation (types and causes)"],
)