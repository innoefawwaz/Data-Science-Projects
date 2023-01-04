import streamlit as st
import feature_engine
import pandas as pd
import pickle

st.title("Used car sales price prediction")

# import model
model = pickle.load(open("M2P1_pred.pkl", "rb"))

st.write('Insert features First:')

# user input
odometer = st.slider(label='odometer', min_value=0, max_value=150000, step=1)
powerPS = st.slider(label='powerPS', min_value=1, max_value=923, step=1)
yearOfRegistration = st.slider(label='yearOfRegistration', min_value=1863, max_value=2016, step=1)
gearbox = st.selectbox(label='gearbox', options=['automatik', 'manuell'])
models = st.selectbox(label='model', options=['7er', 'golf', 'a3', 'scirocco', 'e_klasse', 'c_klasse', 'a1',
       'a_klasse', 's_klasse', 'passat', 'corsa', '3er', '1er', '5er',
       'a6', 'a4', 'transporter', 'vito', '100', 'm_klasse', 'lupo',
       'touareg', 'andere', 'touran', 'x_reihe', 'tigra', 'signum',
       'sharan', 'a5', 'beetle', 'phaeton', 'sl', 'insignia', 'up', '80',
       'z_reihe', 'clk', 'vivaro', 'tiguan', 'sprinter', 'astra', 'viano',
       'bora', 'fox', 'polo', 'zafira', 'meriva', 'vectra', 'omega', 'a8',
       'caddy', 'tt', 'eos', 'slk', 'm_reihe', 'glk', 'combo', 'a2',
       'b_klasse', 'cc', 'v_klasse', 'jetta', 'q7', 'cl', '90', 'q3',
       'q5', 'agila', 'calibra', 'kaefer', 'gl', 'amarok', 'antara',
       'kadett', '6er', 'g_klasse', '200'])
fuelType = st.selectbox(label='fuelType', options=['benzin', 'diesel', 'lpg', 'cng', 'andere', 'hybrid', 'elektro'])
brand = st.selectbox(label='brand', options=['volkswagen', 'audi', 'opel', 'mercedes_benz', 'bmw'])


# convert into dataframe
data = pd.DataFrame({'odometer': [odometer],
                'powerPS': [powerPS],
                'yearOfRegistration': [yearOfRegistration],
                'gearbox':[gearbox],
                'model': [models],
                'fuelType': [fuelType],
                'brand': [brand],
                    })
data
# model predict
clas = model.predict(data).tolist()[0]

#Intepretation
if st.button('Predict'):
    st.write('The used car price is : ', clas, 'USD')  


