# Content for WBUHS 2nd-year B.Sc. Nursing: Applied Pathology & Genetics
# Notes are original summaries. Verify MCQs / 5-mark questions against your real WBUHS papers.
# Refs: Harsh Mohan "Textbook of Pathology" / "Pathology for Nursing"; Robbins "Basic Pathology";
#       Indian nursing texts (Lippincott India / Elsevier India) for Genetics.

from unit_p1_theory import TOPICS
from unit_p2 import P2
from unit_p3 import P3
from unit_p4 import P4
from unit_p5 import P5
from unit_g1 import G1
from unit_g2 import G2
from unit_g3 import G3
from unit_g4 import G4
from unit_g5 import G5


def stub(uid, subject, title, topics, hrs):
    return dict(id=uid, subject=subject, title=title, hrs=hrs, topics=[dict(t=t, imp=False, txt="") for t in topics],
                mcq=[], long=[], imp=[])

P1 = dict(
    id="P1", subject="Pathology", title="Unit I - General Pathology", hrs=8,
    topics=TOPICS,
    mcq=[
        ("Commonest cause of cell injury is", ["Hypoxia", "Chemical agents", "Genetic defects", "Immunologic reactions"], 0),
        ("Coagulative necrosis is typically seen in infarct of the", ["Brain", "Heart", "Lung abscess", "Pancreas fat"], 1),
        ("Caseous necrosis is a feature of", ["Tuberculosis", "Diabetes", "Pancreatitis", "Typhoid"], 0),
        ("Replacement of one adult cell type by another is", ["Hyperplasia", "Hypertrophy", "Metaplasia", "Atrophy"], 2),
        ("Commonest type of embolus is", ["Air", "Fat", "Thromboembolus", "Amniotic fluid"], 2),
        ("First cells to arrive at the site of acute inflammation", ["Lymphocytes", "Neutrophils", "Eosinophils", "Plasma cells"], 1),
        ("Hallmark cells of granulomatous inflammation", ["Neutrophils", "Epithelioid cells and giant cells", "Mast cells", "Eosinophils"], 1),
        ("Healing by first intention occurs in", ["Gaping ulcer", "Clean, apposed surgical wound", "Burn with tissue loss", "Infected wound"], 1),
        ("Malignant cells confined above the basement membrane =", ["Metastasis", "Carcinoma in situ", "Adenoma", "Sarcoma"], 1),
        ("Protein content of a transudate is", ["<3 g/dL", ">3 g/dL", ">5 g/dL", ">8 g/dL"], 0),
    ],
    long=[
        ("Define inflammation. Describe the vascular events in acute inflammation. (PYQ pattern)",
         "Definition; cardinal signs; vasoconstriction -> vasodilation; increased permeability; stasis; emigration of neutrophils; outcomes."),
        ("Differentiate necrosis from apoptosis. Name the types of necrosis. (PYQ pattern)",
         "Table: cell size, energy, inflammation, membrane; then coagulative, liquefactive, caseous, fat, fibrinoid."),
        ("Explain wound healing by primary and secondary intention. (PYQ pattern)",
         "Definition; steps (clot, inflammation, granulation, fibrosis, remodelling); differences; factors delaying healing."),
        ("Differentiate benign from malignant tumours. (Important topic)",
         "Table: growth rate, capsule, differentiation, invasion, metastasis, recurrence, prognosis; examples."),
        ("Define thrombosis. Explain Virchow's triad and fate of a thrombus. (Important topic)",
         "Definition; three factors; propagation, embolism, organisation, recanalisation, lysis; thrombus vs clot."),
    ],
    imp=["Types of necrosis and gangrene", "Acute inflammation", "Wound healing", "Benign vs malignant tumours", "Thrombosis / embolism / shock"],
)

UNITS = [
    P1,
    P2,
    P3,
    P4,
    P5,
    G1,
    G2,
    G3,
    G4,
    G5,
]