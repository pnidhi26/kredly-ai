import streamlit as st

from .ingestion import ingest_files
from .rag_pipeline import answer_question
from .reasoning import answer_numerical_question
from .conflict_detection import detect_refund_conflict
from .consensus import compute_consensus
from .export import export_answer_pdf

from .ui_components import (
    render_answer,
    render_sources,
    render_why_answer
)


# ---------- Session State ----------
if "structured_data" not in st.session_state:
    st.session_state["structured_data"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "enabled_files" not in st.session_state:
    st.session_state["enabled_files"] = {}


def confidence_label(distance):
    if distance <= 0.3:
        return "High"
    elif distance <= 0.6:
        return "Medium"
    return "Low"


def load_css():
    with open("app/styles/theme.css") as f:
        st.markdown("<hr style='border-color:#222;'>", unsafe_allow_html=True)

def render_ui():
    load_css()

    st.title("Kredly AI")
    st.caption("Startup-grade Document Intelligence")

    # ---------- Sidebar ----------
    with st.sidebar:
        st.header("Documents")

        files = st.file_uploader(
            "Upload documents",
            type=["pdf", "png", "jpg", "jpeg", "txt"],
            accept_multiple_files=True
        )

        if st.button("Ingest"):
            with st.spinner("Analyzing documents..."):
                structured = ingest_files(files)
                st.session_state["structured_data"] = structured

                for f in structured:
                    st.session_state["enabled_files"][f["file_name"]] = True

        st.subheader("Active Documents")
        for fname in st.session_state["enabled_files"]:
            st.session_state["enabled_files"][fname] = st.checkbox(
                fname,
                value=st.session_state["enabled_files"][fname]
            )

    if not st.session_state["structured_data"]:
        st.info("Upload documents to begin.")
        return

    question = st.text_input("Ask a question")

    if not st.button("Ask") or not question:
        return

    enabled = [
        f for f, v in st.session_state["enabled_files"].items() if v
    ]

    history = ""
    for q, a in st.session_state["chat_history"][-3:]:
        history += f"Q: {q}\nA: {a}\n"

    full_question = history + question

    answer, docs, distances, metas = answer_question(
        full_question,
        enabled_files=enabled
    )

    st.session_state["chat_history"].append((question, answer))

    consensus = compute_consensus(metas, distances)

    best_distance = min(distances) if distances else 1.0
    confidence = (
        "Not enough evidence"
        if answer.lower() == "i don't know"
        else f"{confidence_label(best_distance)} (distance {best_distance:.2f})"
    )

    render_answer(answer, f"**Confidence:** {confidence}")
    render_why_answer(metas[0]["file"], distances[0])
    render_sources(docs, distances, metas)

    pdf = export_answer_pdf(
        question,
        answer,
        [m["file"] for m in metas]
    )

    st.download_button(
        "📄 Download Answer as PDF",
        pdf,
        file_name="kredly_answer.pdf",
        mime="application/pdf"
    )
