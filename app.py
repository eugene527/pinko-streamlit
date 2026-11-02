from pathlib import Path

import streamlit as st


st.set_page_config(page_title="여러분 제 고양이 좀 보세요")

st.title("여러분 제 고양이 좀 보세요")
st.image(str(Path(__file__).parent / "pinko.jpg"), width="stretch")

st.session_state.setdefault("hearts", 0)


def add_heart():
    st.session_state.hearts += 1


st.button(f"❤️ {st.session_state.hearts}", on_click=add_heart)
