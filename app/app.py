import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

# Set page configuration
st.set_page_config(page_title="Obesity Prediction", page_icon=":guardsman:", layout="wide")

# Set background image
page_bg_img = '''
<style>
body {
background-image: url(".\image.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved model
with open('arima_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Load the dataset
data = pd.read_csv("S:/UMBC 4th Sem/paData.csv")

# Function to make predictions
def make_predictions(location, question, steps):
    filtered_data = data[(data['LocationDesc'] == location) & (data['Question'] == question)]
    filtered_data = filtered_data.dropna(subset=['YearStart', 'Data_Value'])
    
    if len(filtered_data) < 2:
        st.warning(f"Insufficient data for {location} and {question}")
        return None
    
    filtered_data = filtered_data[['YearStart', 'Data_Value']]
    filtered_data['YearStart'] = pd.to_datetime(filtered_data['YearStart'], format='%Y')
    filtered_data.set_index('YearStart', inplace=True)
    filtered_data = filtered_data.groupby(pd.Grouper(freq='Y')).mean()
    
    last_year = filtered_data.index.max().year
    future_years = range(last_year + 1, last_year + steps + 1)
    
    forecast = loaded_model.forecast(steps=steps)
    
    predicted_values = {}
    for i, year in enumerate(future_years):
        predicted_values[year] = forecast[i]
    
    return predicted_values

# Streamlit app
def main():
    st.title("Obesity Prediction")
    
    # User input for location and question
    location = st.selectbox("Select the location:", data['LocationDesc'].unique())
    question = st.selectbox("Select the question:", data['Question'].unique())
    steps = st.number_input("Enter the number of years to forecast:", min_value=1, max_value=10, value=5)
    
    if st.button("Predict"):
        predictions = make_predictions(location, question, steps)
        
        if predictions:
            st.subheader("Predicted Values")
            for year, value in predictions.items():
                st.write(f"{year}: {value}")

if __name__ == '__main__':
    main()