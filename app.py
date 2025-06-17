
import streamlit as st

st.set_page_config(page_title="Kripto Alarm Paneli", layout="wide")

st.title("📈 Kripto Alarm Paneli")
st.markdown("Bu panel ile anlık olarak coin fiyatlarını takip edebilir, yapay zeka destekli al-sat sinyalleri alabilirsiniz.")

# Giriş kontrolü örneği
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Şifre", type="password")
    if password == "kriptogiris":
        st.session_state.authenticated = True
        st.experimental_rerun()
    else:
        st.stop()

# Sahte verilerle gösterim örneği
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AVAX", "19.68", "+2.5%")
with col2:
    st.metric("ADA", "0.644", "-1.2%")
with col3:
    st.metric("ETH", "2570", "+0.8%")

st.info("⚙️ Gelişmiş alarm, sinyal ve grafik sistemleri bu panelde entegre edilebilir.")

