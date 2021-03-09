import streamlit as st

st.text('this is a test app!')

try:
    print("Got: client.showErrorDetails", st.config.get_option("client.showErrorDetails"))
except RuntimeError:
    print("running on a version pre 0.77")

st.text(st.config.show_config())
