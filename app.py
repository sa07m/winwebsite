import base64
import re
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Winnovate Preview", layout="wide")

root = Path(__file__).parent
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")

def file_to_data_uri(p: Path) -> str:
    mime = "image/png" if p.suffix.lower()==".png" else (
        "image/jpeg" if p.suffix.lower() in (".jpg",".jpeg") else "image/svg+xml"
    )
    data = p.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"

# Inline local assets that your HTML references.
# Start with logo1.png; add more if needed.
assets = {
    "logo1.png": root / "logo1.png",
    # "another.png": root / "another.png",
}

for fname, path in assets.items():
    if path.exists():
        uri = file_to_data_uri(path)
        # replace any src="logo1.png" or src='logo1.png'
        html = re.sub(rf'src=(["\']){re.escape(fname)}\1', f'src="{uri}"', html)

st.markdown("### Winnovate — HTML Preview (Streamlit)")
components.html(html, height=1200, scrolling=True)
