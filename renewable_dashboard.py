# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 14:04:21 2025

@author: evolu
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data generation
def generate_sample_data():
    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
    data = {
        "Date": dates,
        "Solar (MWh)": np.random.uniform(50, 150, len(dates)),
        "Wind (MWh)": np.random.uniform(70, 200, len(dates)),
        "Hydro (MWh)": np.random.uniform(30, 100, len(dates)),
    }
    df = pd.DataFrame(data)
    df["Total"] = df["Solar (MWh)"] + df["Wind (MWh)"] + df["Hydro (MWh)"]
    return df

# Load data
df = generate_sample_data()

# Sidebar
st.sidebar.title("Renewable Energy Dashboard")
source_filter = st.sidebar.multiselect("Select Energy Sources", options=["Solar", "Wind", "Hydro"], default=["Solar", "Wind", "Hydro"])

st.title("🌍 Renewable Energy Overview")

# Summary stats
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Energy (MWh)", f"{df['Total'].sum():,.0f}")
col2.metric("Avg Daily Output (MWh)", f"{df['Total'].mean():.2f}")
col3.metric("Days Recorded", len(df))

# Time series plot
st.subheader("Daily Energy Output Over Time")
fig = px.line(df, x="Date", y=[f"{src} (MWh)" for src in source_filter], title="Energy Output by Source")
st.plotly_chart(fig)

# Pie chart
st.subheader("Proportional Contribution")
latest_data = df.iloc[-1]
contrib = {src: latest_data[f"{src} (MWh)"] for src in source_filter}
pie_fig = px.pie(names=list(contrib.keys()), values=list(contrib.values()), title="Latest Day Energy Mix")
st.plotly_chart(pie_fig)

# Data table
st.subheader("Raw Data")
st.dataframe(df.tail(10))

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

