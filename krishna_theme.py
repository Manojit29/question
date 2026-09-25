import streamlit as st

CSS = """
<style>
@keyframes bgshift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes float1 { 0%,100% { transform: translateY(0px) rotate(0deg);} 50% { transform: translateY(-22px) rotate(8deg);} }
@keyframes float2 { 0%,100% { transform: translateY(0px) rotate(0deg);} 50% { transform: translateY(18px) rotate(-6deg);} }
@keyframes twinkle { 0%,100% { opacity: 0.25; } 50% { opacity: 0.9; } }
@keyframes glow { 0%,100% { text-shadow: 0 0 8px #ffd782, 0 0 2px #ffd782; } 50% { text-shadow: 0 0 20px #ffd782, 0 0 8px #ffe9c2; } }

.stApp {
    background: linear-gradient(120deg, #0b1e3d, #1a3a6b, #2b2450, #12294f, #0b1e3d);
    background-size: 400% 400%;
    animation: bgshift 22s ease infinite;
}

/* decorative banner strip - rendered inline in normal page flow, so it always shows
   (position:fixed layers get silently clipped inside some Streamlit container versions) */
.krishna-banner {
    position: relative; z-index: 1;
    display: flex; justify-content: center; gap: 1.6rem;
    font-size: 2.2rem; padding: 0.4rem 0 0.8rem 0;
}
.krishna-banner span:nth-child(1) { animation: float1 4s ease-in-out infinite; }
.krishna-banner span:nth-child(2) { animation: twinkle 2.4s ease-in-out infinite; }
.krishna-banner span:nth-child(3) { animation: float2 5s ease-in-out infinite; }
.krishna-banner span:nth-child(4) { animation: twinkle 3s ease-in-out infinite; animation-delay: .6s; }
.krishna-banner span:nth-child(5) { animation: float1 4.6s ease-in-out infinite; animation-delay: .3s; }

.krishna-card {
    position: relative; z-index: 1;
    background: rgba(255, 215, 130, 0.08);
    border: 1px solid rgba(255, 215, 130, 0.55);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.krishna-title { color: #ffd782; font-size: 1.6rem; font-weight: 700; text-align: center; animation: glow 3s ease-in-out infinite; }
.krishna-sub { color: #f5e6c8; text-align: center; font-style: italic; }

.gita-box {
    position: relative; z-index: 1;
    background: radial-gradient(circle at top, #2b2450 0%, #0b1e3d 80%);
    border: 1px solid #ffd782;
    border-radius: 20px;
    padding: 3rem 2rem;
    text-align: center;
    margin-top: 2rem;
}
.gita-verse { color: #ffd782; font-size: 1.3rem; font-weight: 700; margin-bottom: 0.6rem; }
.gita-meaning { color: #f5e6c8; font-size: 1.1rem; line-height: 1.6; }

h1, h2, h3 { color: #ffe9c2 !important; position: relative; z-index: 1;}
.stMarkdown, .stMarkdown p, label, .stCaption { color: #f5e6c8 !important; }
section[data-testid="stSidebar"] { background: rgba(5, 15, 35, 0.85); }
.block-container { position: relative; z-index: 1; }

/* make the sidebar collapse/expand ("hamburger" / chevron) control clearly visible */
[data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"],
header [data-testid="baseButton-headerNoPadding"], header button {
    background: rgba(255, 215, 130, 0.18) !important;
    border-radius: 8px !important;
}
[data-testid="collapsedControl"] svg, [data-testid="stSidebarCollapsedControl"] svg,
header svg, [data-testid="stHeader"] svg {
    fill: #ffd782 !important;
    stroke: #ffd782 !important;
    opacity: 1 !important;
}
[data-testid="stHeader"] { background: rgba(11, 30, 61, 0.6) !important; }
</style>
"""

BANNER = """<div class="krishna-banner">
<span>🦚</span><span>🪷</span><span>ॐ</span><span>🪈</span><span>🦚</span>
</div>"""


def inject_theme():
    st.markdown(CSS, unsafe_allow_html=True)


def banner():
    """A row of animated Krishna-themed icons, visible on any page - call at the top."""
    st.markdown(BANNER, unsafe_allow_html=True)


def welcome_message(name: str):
    st.markdown(
        f"""<div class="krishna-card">
        <div class="krishna-title">🦚 ॐ Welcome, {name}! ॐ 🦚</div>
        <div class="krishna-sub">May Lord Krishna's wisdom light up your path through Pathology and Genetics 🪈🌸</div>
        </div>""",
        unsafe_allow_html=True,
    )


def unit_complete_message(name: str, unit_title: str):
    st.markdown(
        f"""<div class="krishna-card">
        <div class="krishna-title">🌸 Well done, {name}! 🌸</div>
        <div class="krishna-sub">You have completed "{unit_title}". Krishna smiles upon your effort.</div>
        </div>""",
        unsafe_allow_html=True,
    )


def course_complete_message(name: str):
    st.balloons()
    st.markdown(
        f"""<div class="krishna-card">
        <div class="krishna-title">🦚🪷 {name}, you have completed the whole course! 🪷🦚</div>
        <div class="krishna-sub">"You have a right to your work, never to the fruits of it" (Gita 2.47).
        You did the work with your whole heart - Krishna is pleased. ॐ</div>
        </div>""",
        unsafe_allow_html=True,
    )


def gita_screen(verse_ref: str, meaning: str, seconds_left: int):
    st.markdown(
        f"""<div class="gita-box">
        <div style="font-size:2rem;">🪈 🦚 ॐ</div>
        <div class="gita-verse">Bhagavad Gita {verse_ref}</div>
        <div class="gita-meaning">{meaning}</div>
        <div style="color:#f5e6c8; margin-top:1.5rem;">Take a breath... resuming in {seconds_left} seconds</div>
        </div>""",
        unsafe_allow_html=True,
    )