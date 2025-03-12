import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate herd growth
def herd_growth(initial_herd, growth_rate, cull_rate, years):
    herd_size = [initial_herd]
    for t in range(1, years):
        new_herd = herd_size[-1] * (1 + growth_rate) - (herd_size[-1] * cull_rate)
        herd_size.append(new_herd)
    return herd_size

# Function to calculate financials
def financials(initial_income, initial_expenses, growth_rate, cpi, years, boer_share):
    revenue = [initial_income]
    expenses = [initial_expenses]
    net_cash_flow = []

    for t in range(1, years):
        revenue.append(revenue[-1] * (1 + growth_rate) * boer_share)
        expenses.append(expenses[-1] * (1 + cpi))
        net_cash_flow.append(revenue[-1] - expenses[-1])

    return revenue, expenses, net_cash_flow

# Streamlit app
def main():
    st.title("BoerPlan Dynamic Chart")

    # User inputs
    initial_herd = st.slider("Initial Herd Size", 50, 1000, 200)
    growth_rate = st.slider("Herd Growth Rate", 0.0, 0.2, 0.05)
    cull_rate = st.slider("Cull Rate", 0.0, 0.1, 0.02)
    speen_pct = st.slider("Weaning %", 0.0, 1.0, 0.8)
    calf_mortality = st.slider("Calf Mortality %", 0.0, 0.2, 0.05)
    initial_income = st.slider("Initial Revenue", 100000, 5000000, 1000000)
    initial_expenses = st.slider("Initial Expenses", 50000, 3000000, 500000)
    cpi = st.slider("CPI (Inflation)", 0.0, 0.1, 0.047)
    boer_share = st.slider("Boer Share %", 0.0, 1.0, 0.5)
    years = st.slider("Projection Years", 1, 20, 10)

    # Run calculations
    herd_size = herd_growth(initial_herd, growth_rate, cull_rate, years)
    revenue, expenses, net_cash_flow = financials(initial_income, initial_expenses, growth_rate, cpi, years, boer_share)

    # Plot results
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(range(years), herd_size, label="Herd Size", marker="o")
    ax.plot(range(years), revenue, label="Revenue", marker="s")
    ax.plot(range(years), expenses, label="Expenses", marker="^")
    ax.plot(range(years), net_cash_flow, label="Net Cash Flow", marker="x")

    ax.set_xlabel("Years")
    ax.set_ylabel("Values")
    ax.set_title("Herd Growth & Financial Projections")
    ax.legend()

    st.pyplot(fig)

if __name__ == "__main__":
    main()
