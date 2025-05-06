import streamlit as st
import pandas as pd

st.set_page_config(page_title=" Data Explorer", layout="wide")

# Sidebar UI
st.sidebar.title("🔧 Controls")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

view_option = st.sidebar.selectbox(
    "Select data view:",
    ("Header (First 10 Rows)", "Tail (Last 10 Rows)", "Middle (Custom Range)")
)

# Placeholder for inputs
start = end = None
if view_option == "Middle (Custom Range)":
    st.sidebar.markdown("#### 🔢 Select Range")
    start = st.sidebar.number_input("Start Index", min_value=0, value=0)
    end = st.sidebar.number_input("End Index", min_value=start+1, value=start+10)

# Main screen content
st.title("📊 CSV Data Explorer")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Info section
    st.subheader("📌 Dataset Info")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.write("**Data Types:**")
    st.write(df.dtypes)

    # Data display section
    st.subheader("🔍 Data View")
    if view_option == "Header (First 10 Rows)":
        st.dataframe(df.head(10))

    elif view_option == "Tail (Last 10 Rows)":
        st.dataframe(df.tail(10))

    elif view_option == "Middle (Custom Range)":
        if end <= df.shape[0]:
            st.dataframe(df.iloc[start:end])
        else:
            st.warning(f"End index exceeds dataset length ({df.shape[0]} rows).")
else:
    st.info("Upload a CSV file from the sidebar to get started.")
