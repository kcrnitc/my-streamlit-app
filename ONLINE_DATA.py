import streamlit as st
import pandas as pd
import os

# Set the title of the Streamlit app
st.title("Excel Data Viewer")

# Filepath to the Excel file
EXCEL_FILE = "data/EDM_DATA.xlsx"

# Check if the file exists
if not os.path.exists(EXCEL_FILE):
    st.error(f"The file '{EXCEL_FILE}' does not exist. Please ensure the data file is in the correct directory.")
else:
    # Load the Excel data into a DataFrame
    try:
        df = pd.read_excel(EXCEL_FILE)

        # Display the DataFrame in the Streamlit app
        st.write("### Data in the Excel File:")
        st.dataframe(df)

        # Option to filter data by timestamp range
        st.write("### Filter Data by Timestamp Range")
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # Date range input widgets
        start_date = st.date_input("Start Date", df['Timestamp'].min().date())
        end_date = st.date_input("End Date", df['Timestamp'].max().date())

        # Filter the data based on the selected date range
        filtered_df = df[(df['Timestamp'].dt.date >= start_date) & (df['Timestamp'].dt.date <= end_date)]

        # Display filtered data
        st.write("### Filtered Data:")
        st.dataframe(filtered_df)

    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
