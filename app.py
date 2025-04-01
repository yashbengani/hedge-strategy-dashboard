
import streamlit as st
import pandas as pd
from strategy import run_hedge_strategy

st.set_page_config(page_title="Hedge Strategy Dashboard", layout="wide")

st.title("📊 Hedge Strategy Dashboard")
st.markdown("Upload your **Option Chain CSV** and **Spot/Futures CSV** to run the hedge strategy.")

with st.expander("ℹ️ Strategy Overview"):
    st.markdown("""
    - 🔹 **Sell Call** 5% above spot price  
    - 🔹 **Buy Put** 5% below spot price  
    - 🔄 Entry: Start of expiry, Exit: 1 week before  
    - 🧪 Supports testing across liquid F&O stocks  
    """)

# File Uploaders
spot_file = st.file_uploader("📁 Upload Spot & Futures CSV", type=["csv"], key="spot")
option_file = st.file_uploader("📁 Upload Option Chain CSV", type=["csv"], key="option")

if spot_file and option_file:
    spot_df = pd.read_csv(spot_file)
    option_df = pd.read_csv(option_file)

    st.success("✅ Files Uploaded! Running strategy...")
    result_df = run_hedge_strategy(spot_df, option_df)

    if not result_df.empty:
        st.subheader("📈 Strategy Output")
        st.dataframe(result_df)

        total_pnl = result_df['net_pnl'].sum()
        st.metric(label="Total Net PnL", value=f"₹{total_pnl:,.2f}")
    else:
        st.warning("No matching options found for strategy execution.")
else:
    st.info("Please upload both files to begin.")
