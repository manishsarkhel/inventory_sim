import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Inventory Management Simulation")

# Input parameters
st.sidebar.header("Input Parameters")
demand = st.sidebar.number_input("Annual Demand (units)", min_value=1, value=1000)
ordering_cost = st.sidebar.number_input("Ordering Cost per Order (Rs)", min_value=1, value=50)
holding_cost = st.sidebar.number_input("Holding Cost per Unit per Year (Rs)", min_value=1, value=2)
lead_time = st.sidebar.number_input("Lead Time (days)", min_value=1, value=5)
unit_cost = st.sidebar.number_input("Unit Cost (Rs)", min_value=1, value=10)

# Calculate EOQ and related costs
def calculate_eoq(demand, ordering_cost, holding_cost):
    eoq = np.sqrt((2 * demand * ordering_cost) / holding_cost)
    return eoq

def calculate_total_cost(demand, ordering_cost, holding_cost, eoq):
    total_ordering_cost = (demand / eoq) * ordering_cost
    total_holding_cost = (eoq / 2) * holding_cost
    total_cost = total_ordering_cost + total_holding_cost
    return total_ordering_cost, total_holding_cost, total_cost

eoq = calculate_eoq(demand, ordering_cost, holding_cost)
total_ordering_cost, total_holding_cost, total_cost = calculate_total_cost(demand, ordering_cost, holding_cost, eoq)

# Display results
st.header("Results")
st.write(f"Economic Order Quantity (EOQ): {eoq:.2f} units")
st.write(f"Total Ordering Cost: Rs {total_ordering_cost:.2f}")
st.write(f"Total Holding Cost: Rs {total_holding_cost:.2f}")
st.write(f"Total Cost: Rs {total_cost:.2f}")

# Plotting the tradeoffs
order_quantities = np.linspace(1, 2 * eoq, 100)
ordering_costs = (demand / order_quantities) * ordering_cost
holding_costs = (order_quantities / 2) * holding_cost
total_costs = ordering_costs + holding_costs

plt.figure(figsize=(10, 6))
plt.plot(order_quantities, ordering_costs, label="Ordering Cost")
plt.plot(order_quantities, holding_costs, label="Holding Cost")
plt.plot(order_quantities, total_costs, label="Total Cost")
plt.axvline(eoq, color='r', linestyle='--', label="EOQ")
plt.xlabel("Order Quantity (units)")
plt.ylabel("Cost (Rs)")
plt.title("Tradeoffs Between Ordering, Holding, and Total Costs")
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Reorder Point
reorder_point = (demand / 365) * lead_time
st.write(f"Reorder Point: {reorder_point:.2f} units")