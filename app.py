import json
import os
import random
import time

import streamlit as st
from content import UNITS
from gita_quotes import QUOTES
from krishna_theme import (
    inject_theme, welcome_message, unit_complete_message,
    course_complete_message, gita_screen, banner,
)

# ---- Change this one line to the person's name ----
NAME = "Ri🌻🌻"
# ----------------------------------------------------

MCQ_SEC, WRITE_SEC, GITA_SEC = 10 * 60, 90 * 60, 30
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

st.set_page_config(page_title=f"{NAME}'s Nursing Study Journey", layout="wide")
inject_theme()


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed": [], "scores": {}}


def save_progress(p):
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump(p, f)
    except Exception:
        pass


S = st.session_state
S.setdefault("progress", load_progress())
S.setdefault("page", "home")     # home -> unit
S.setdefault("u", None)          # current unit index
S.setdefault("stage", "theory")  # theory -> mcq -> result -> written -> gita
S.setdefault("scores", {})
S.setdefault("review", {})
S.setdefault("deadline", 0.0)
S.setdefault("reveal", False)
S.setdefault("gita_quote", None)


def go(stage, seconds=0):
    S.stage = stage
    S.deadline = time.time() + seconds
    S.reveal = False
    st.rerun()


def go_home():
    S.page = "home"
    S.u = None
    st.rerun()


def start_unit(idx):
    S.page = "unit"
    S.u = idx
    S.stage = "theory"
    st.rerun()


@st.fragment(run_every=1)
def timer(label, stop_app=False):
    left = max(0, int(S.deadline - time.time()))
    st.metric(label, f"{left // 60:02d}:{left % 60:02d}")
    if left == 0 and stop_app:
        st.rerun()


@st.fragment(run_every=1)
def gita_timer():
    left = max(0, int(S.deadline - time.time()))
    ref, meaning = S.gita_quote
    gita_screen(ref, meaning, left)
    if left == 0:
        go_home()


def grade(u):
    picks = [S.get(f"a_{u['id']}_{i}") for i in range(len(u["mcq"]))]
    S.review[u["id"]] = picks
    S.scores[u["id"]] = sum(1 for (q, o, a), p in zip(u["mcq"], picks) if p == o[a])


def markdown_report():
    lines = [f"# Progress report for {NAME}\n"]
    done = S.progress["completed"]
    for x in UNITS:
        mark = "x" if x["id"] in done else " "
        score = S.progress["scores"].get(x["id"])
        score_txt = f" - MCQ score {score}/{len(x['mcq'])}" if score is not None else ""
        lines.append(f"- [{mark}] **{x['id']}**: {x['title']}{score_txt}")
    remaining = len(UNITS) - len(done)
    lines.append(f"\nCompleted: {len(done)} / {len(UNITS)} units. Remaining: {remaining}.")
    return "\n".join(lines)


# ============================== HOME PAGE ==============================
if S.page == "home":
    banner()
    welcome_message(NAME)

    done = S.progress["completed"]
    if len(done) == len(UNITS):
        course_complete_message(NAME)

    st.subheader("Choose any unit to start or continue")
    cols = st.columns(2)
    for i, x in enumerate(UNITS):
        is_done = x["id"] in done
        score = S.progress["scores"].get(x["id"])
        label = f"{'✅' if is_done else '▶️'} {x['id']}: {x['title']}"
        if score is not None:
            label += f"  (MCQ {score}/{len(x['mcq'])})"
        with cols[i % 2]:
            if st.button(label, key=f"home_{x['id']}", use_container_width=True):
                start_unit(i)

    st.divider()
    with st.expander("📋 My progress (markdown)"):
        report = markdown_report()
        st.markdown(report)
        st.download_button("Download progress as .md", report, file_name="progress.md")

# ============================== UNIT FLOW ==============================
else:
    u = UNITS[S.u]
    with st.sidebar:
        st.header(f"{NAME}'s progress")
        for x in UNITS:
            icon = "✅" if x["id"] in S.progress["completed"] else "▫️"
            st.write(f"{icon} {x['id']}: {x['title']}")
        if st.button("🏠 Back to home"):
            go_home()

    banner()
    st.title(u["title"])
    st.caption(f"{u['subject']} · {u['hrs']} theory hours · WBUHS B.Sc. Nursing")

    if S.stage == "theory":
        if u["imp"]:
            st.info("⭐ **Important topics:** " + " · ".join(u["imp"]))
        for t in u["topics"]:
            with st.expander(("⭐ " if t["imp"] else "") + t["t"], expanded=False):
                st.markdown(t["txt"] or "_Notes for this sub-topic are not added yet._")
                for dot, cap in t.get("dots", []):
                    st.graphviz_chart(dot, use_container_width=True)
                    st.caption("Diagram: " + cap)
                for src, cap in t.get("figs", []):
                    st.image(src, caption=cap)
                if t.get("example"):
                    st.info("**Worked example:** " + t["example"])
        if u["mcq"]:
            if st.button(f"Start MCQ test ({len(u['mcq'])} questions, 10 min)", type="primary"):
                go("mcq", MCQ_SEC)
        else:
            st.warning("This unit has no test content yet.")

    elif S.stage == "mcq":
        if time.time() >= S.deadline:
            grade(u)
            go("result")
        timer("Time left", stop_app=True)
        for i, (q, opts, _) in enumerate(u["mcq"]):
            st.radio(f"**Q{i + 1}.** {q}", opts, index=None, key=f"a_{u['id']}_{i}")
        if st.button("Submit MCQs", type="primary"):
            grade(u)
            go("result")

    elif S.stage == "result":
        sc, n = S.scores[u["id"]], len(u["mcq"])
        st.subheader(f"MCQ score: {sc} / {n}")
        st.progress(sc / n)
        for i, ((q, opts, a), p) in enumerate(zip(u["mcq"], S.review[u["id"]])):
            ok = p == opts[a]
            st.markdown(f"{'✅' if ok else '❌'} **Q{i + 1}.** {q}  \n"
                        f"Your answer: {p or 'not attempted'} · Correct: **{opts[a]}**")
        S.progress["scores"][u["id"]] = sc
        save_progress(S.progress)
        if st.button("Continue to 5-mark questions (1.5 h)", type="primary"):
            go("written", WRITE_SEC)

    elif S.stage == "written":
        timer("Writing time left")
        st.write("Write each answer on your own paper (about 5 marks each). Key points appear after you finish.")
        for i, (q, pts) in enumerate(u["long"]):
            st.markdown(f"**Q{i + 1}.** {q}")
            if S.reveal:
                st.success("Key points: " + pts)
        if not S.reveal:
            if st.button("I have finished writing: show key points", type="primary"):
                S.reveal = True
                st.rerun()
        else:
            if st.button("Mark this unit complete", type="primary"):
                if u["id"] not in S.progress["completed"]:
                    S.progress["completed"].append(u["id"])
                    save_progress(S.progress)
                S.gita_quote = random.choice(QUOTES)
                go("gita", GITA_SEC)

    elif S.stage == "gita":
        unit_complete_message(NAME, u["title"])
        gita_timer()
        if st.button("Continue now"):
            go_home()