import streamlit as st

# Unit conversion dictionary
conversion_factors = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Inch": 39.3701, "Foot": 3.28084},
    "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
    "Temperature": {"Celsius": 1, "Fahrenheit": 1, "Kelvin": 1},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
    "Volume": {"Liter": 1, "Milliliter": 1000, "Gallon": 0.264172, "Cup": 4.22675}
}

# Function to convert units
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Streamlit UI
st.title("🔢 Unit Converter")
st.write("### by uzair khan")

# Step 1: Select category
category = st.selectbox("Select a category", list(conversion_factors.keys()))

# Step 2: Enter value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f", key="value")

# Step 3: Create two columns for "From" and "To"
col1, col2 = st.columns([1, 1])  # Equal width columns

# Left Column - "From" section
with col1:
    st.subheader("From")
    from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()), key="from_unit")

# Right Column - "To" section (same row as "From")
with col2:
    st.subheader("To")
    to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()), key="to_unit")

# Convert Button
st.markdown("<br>", unsafe_allow_html=True)  # Adds some spacing
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Add spacing
st.markdown("---")

# Clear button
if st.button("Clear All"):
    st.experimental_rerun()
