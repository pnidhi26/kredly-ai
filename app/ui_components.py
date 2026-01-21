import streamlit as st


def render_answer(answer, confidence_text):
    st.subheader("Answer")
    st.markdown(
        f"<span class='accent'>{answer}</span>",
        unsafe_allow_html=True
    )
    st.markdown(confidence_text)


def render_why_answer(file_name, distance):
    with st.expander("Why this answer?"):
        st.markdown(
            f"""
            - Matched sentence from **{file_name}**
            - Semantic similarity score: **{distance:.2f}**
            - Generated strictly from retrieved documents
            """
        )


def render_sources(docs, distances, metas):
    st.subheader("Sources")
    for doc, dist, meta in zip(docs, distances, metas):
        st.markdown(
            f"""
            <div class="source-box">
                <strong>{meta['file']}</strong><br/>
                <span class="distance">Distance: {dist:.2f}</span><br/><br/>
                <span class="highlight">{doc}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
