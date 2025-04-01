
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hedge Strategy Dashboard", layout="wide")

try:
    st.title("📊 Hedge Strategy Dashboard")
    st.markdown("Upload your **Option Chain CSV** and **Spot/Futures CSV** to begin.")

    with st.expander("ℹ️ What this strategy does"):
        st.markdown("""
        **Strategy Logic**
        - At start of expiry: Sell Call 5% above spot, Buy Put 5% below
        - Exit 1 week before expiry
        - Works on all liquid F&O stocks
        """)

    # File Uploaders
    spot_file = st.file_uploader("📁 Upload Spot & Futures CSV", type=["csv"], key="spot")
    option_file = st.file_uploader("📁 Upload Option Chain CSV", type=["csv"], key="option")

    if spot_file and option_file:
        spot_df = pd.read_csv(spot_file)
        option_df = pd.read_csv(option_file)

        st.success("✅ Files Uploaded! Previewing data:")
        st.subheader("Spot / Futures Data")
        st.dataframe(spot_df.head())

        st.subheader("Option Chain Data")
        st.dataframe(option_df.head())

        # Placeholder for strategy logic
        st.info("📌 Strategy logic coming soon...")

    else:
        st.warning("Please upload both CSV files to proceed.")

except Exception as e:
    st.error(f"❌ An error occurred: {e}")
