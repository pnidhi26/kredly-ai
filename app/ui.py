import streamlit as st

from .ingestion import ingest_files
from .rag_pipeline import answer_question
from .reasoning import answer_numerical_question
from .conflict_detection import detect_refund_conflict


# ---------------- Session state ----------------
if "structured_data" not in st.session_state:
    st.session_state["structured_data"] = []


def confidence_label(distance: float) -> str:
    if distance <= 0.3:
        return "High"
    elif distance <= 0.6:
        return "Medium"
    else:
        return "Low"


def render_ui():
    st.title("Kredly AI")
    st.caption("Document Intelligence with RAG")

    # ---------------- Sidebar ----------------
    with st.sidebar:
        st.header("Upload documents")

        files = st.file_uploader(
            "PDF, image, or text",
            type=["pdf", "png", "jpg", "jpeg", "txt"],
            accept_multiple_files=True
        )

        if st.button("Ingest"):
            if files:
                structured = ingest_files(files)
                st.session_state["structured_data"] = structured

                st.success("Documents ingested successfully")

                st.subheader("📊 Extracted Structured Data")
                for item in structured:
                    st.markdown(f"**File:** {item['file_name']}")
                    st.json(item)

    # ---------------- Main QA ----------------
    question = st.text_input("Ask a question about your documents")

    if st.button("Ask"):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        structured_data = st.session_state.get("structured_data", [])

        # ---- STEP 2: Numerical reasoning ----
        answer, handled = answer_numerical_question(
            question, structured_data
        )

        if handled:
            st.subheader("Answer")
            st.write(answer)
            st.caption("Answered from structured data (no LLM used)")
            return

        # ---- STEP 4: RAG retrieval ----
        answer, docs, distances, metas = answer_question(question)

        # ---- STEP 5: Conflict detection ----
        conflict = detect_refund_conflict(docs, metas, distances)

        if conflict:
            st.subheader("⚠️ Conflict detected")

            st.markdown(
                "The documents contain conflicting information about "
                "**gift card refundability**."
            )

            st.markdown("### ❌ Refunds NOT available")
            for item in conflict["negative"]:
                st.markdown(
                    f"- **{item['file']}**: {item['text']}"
                )

            st.markdown("### ✅ Refunds AVAILABLE")
            for item in conflict["positive"]:
                st.markdown(
                    f"- **{item['file']}**: {item['text']}"
                )

            st.caption(
                "The system cannot determine a single correct answer "
                "because the documents disagree."
            )
            return  # ⬅️ important: stop here

        # ---- Normal RAG answer ----
        st.subheader("Answer")
        st.write(answer)

        best_distance = min(distances)
        st.markdown(
            f"**Confidence:** {confidence_label(best_distance)} "
            f"(distance: {best_distance:.2f})"
        )

        st.subheader("Sources")
        for doc, dist, meta in zip(docs, distances, metas):
            st.markdown(
                f"**File:** {meta['file']} | "
                f"Distance: {dist:.2f}\n\n"
                f"{doc}"
            )
