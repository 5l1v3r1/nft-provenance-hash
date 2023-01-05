import io
import os
import json
import shutil
from PIL import Image
from main import ProvenanceHash

from loguru import logger

import streamlit as st

ph = ProvenanceHash()

st.set_page_config(layout="wide", page_title="NFT and Metadata Generator")
st.markdown(
    "<h1 style='text-align: center'>Provenance Hash</h1>",
    unsafe_allow_html=True,
)

with st.form("my-form", clear_on_submit=True):
    uploaded_images = st.file_uploader(
        "Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=True
    )
    submitted = st.form_submit_button("Upload and Generate Hash(es)")

if submitted and uploaded_images is not None:
    if os.path.exists("images"):
        shutil.rmtree("images")
    os.mkdir("images")

    for uploaded_image in uploaded_images:
        bytes_data = uploaded_image.read()
        current_image = Image.open(io.BytesIO(bytes_data))
        current_image.save(f"images/{uploaded_image.name}")

    logger.info("Getting provenance hash(es)")
    provenance_hashes = ph.get_multiple_provenance_hashes("images")
    if provenance_hashes:
        st.markdown(
            f"<h5 style='text-align: center'>"
            f"{json.dumps(provenance_hashes, indent=4)}</h5>",
            unsafe_allow_html=True,
        )
        logger.info("Provenance hash(es) obtained")
    st.balloons()
else:
    st.write("Please upload image(s) to generate hash(es)!")
