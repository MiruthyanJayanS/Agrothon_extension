import streamlit as st
from streamlit_chat import message
import requests
import chat
from analysis import analyze
from disease import *
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit as st
from real_time import real_time
from trends import *
from pred_yield import *

arhar = Commodity(commodity_dict["arhar"])
commodity_list.append(arhar)
bajra = Commodity(commodity_dict["bajra"])
commodity_list.append(bajra)
barley = Commodity(commodity_dict["barley"])
commodity_list.append(barley)
copra = Commodity(commodity_dict["copra"])
commodity_list.append(copra)
cotton = Commodity(commodity_dict["cotton"])
commodity_list.append(cotton)
sesamum = Commodity(commodity_dict["sesamum"])
commodity_list.append(sesamum)
gram = Commodity(commodity_dict["gram"])
commodity_list.append(gram)
groundnut = Commodity(commodity_dict["groundnut"])
commodity_list.append(groundnut)
jowar = Commodity(commodity_dict["jowar"])
commodity_list.append(jowar)
maize = Commodity(commodity_dict["maize"])
commodity_list.append(maize)
masoor = Commodity(commodity_dict["masoor"])
commodity_list.append(masoor)
moong = Commodity(commodity_dict["moong"])
commodity_list.append(moong)
niger = Commodity(commodity_dict["niger"])
commodity_list.append(niger)
paddy = Commodity(commodity_dict["paddy"])
commodity_list.append(paddy)
ragi = Commodity(commodity_dict["ragi"])
commodity_list.append(ragi)
rape = Commodity(commodity_dict["rape"])
commodity_list.append(rape)
jute = Commodity(commodity_dict["jute"])
commodity_list.append(jute)
safflower = Commodity(commodity_dict["safflower"])
commodity_list.append(safflower)
soyabean = Commodity(commodity_dict["soyabean"])
commodity_list.append(soyabean)
sugarcane = Commodity(commodity_dict["sugarcane"])
commodity_list.append(sugarcane)
sunflower = Commodity(commodity_dict["sunflower"])
commodity_list.append(sunflower)
urad = Commodity(commodity_dict["urad"])
commodity_list.append(urad)
wheat = Commodity(commodity_dict["wheat"])
commodity_list.append(wheat)


def add_logo(logo_path, width, height):
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

st.set_page_config(
    page_title="Hello World!",
    page_icon=":robot:"
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.sidebar.image(add_logo(logo_path="/Users/linuz/Desktop/samples/grow.png", width=150, height=160)) 
st.sidebar.header("Hello World!")
st.sidebar.subheader("Crop analysis and prediction Bot")
st.sidebar.text("try these: What are the best crops to grow in a dry climate?")
st.sidebar.text("try these: What are some common pests and diseases that affect crops in India?")
st.sidebar.text("try these: What are the government initiatives for Indian farmers?")
st.sidebar.text("try these: suggest me a best suited crop")
st.sidebar.text("try these: what is this disease?")
st.sidebar.text("try these: auto suggest me a best suited crop")
st.sidebar.text("try these: What are the best crops to grow in different regions of India?")
st.sidebar.text("try these: forecast crop price")
st.sidebar.text("try these: crop yield estimation")
st.sidebar.text("try these: trends of crop price")
st.markdown("[Github](https://github.com/linusaltacc/crop-analysis-and-prediction)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hey", key="input")
    return input_text 


user_input = get_text()
if user_input=="auto suggest me a best suited crop":
    form = st.form("my_form",clear_on_submit=False)
    n = form.slider('Select the value of Nitrogen Level',
    0, 150)
    p = form.slider('Select the value of Phosphorus Level',
    0, 100)
    k = form.slider('Select the value of Potassium Level',
    0, 100)
    ph = form.slider('Select the value of PH Level',
    0.0, 10.0)
    rainfall = form.slider('Select the value of Rainfall Level',
    0.0, 300.0)
    humidity, temp, moisture = real_time()
    submit = form.form_submit_button("Submit")
    if submit:
        st.session_state.past.append("suggest me a best suited crop")
        best_crop = "The best crop to grow with these parameters is " + analyze(n,p,k,temp,humidity,ph,rainfall)
        st.session_state.generated.append(best_crop)
if user_input=="feedback":
    old = st.session_state.generated
    old = old[len(old)-1]
    st.session_state.past.append("feedback")
    st.session_state.generated.append(f"The system predicted the following intent for your input: { old }")
    option = st.selectbox(
    'Did the system accurately capture your intent? (yes/no):',
    ('select','yes', 'no'))
    if option!='select':
        if option == "yes":
            st.session_state.generated.append("Thank you for the feedback")
            st.session_state.past.append("Yes")
        elif option == "no":
            with open('feedback.txt', 'w') as f:
                f.write(old[len(old)-1])
                f.write('\n')
            st.session_state.past.append("No")
        
if user_input=="suggest me a best suited crop to grow in future":
    form = st.form("my_form",clear_on_submit=False)
    count = form.slider('Select how many days after to predict',
    0, 30)
    area = form.text_input('Enter the city name')
    n = form.slider('Select the value of Nitrogen Level',
    0, 150)
    p = form.slider('Select the value of Phosphorus Level',
    0, 100)
    k = form.slider('Select the value of Potassium Level',
    0, 100)
    ph = form.slider('Select the value of PH Level',
    0.0, 10.0)
    rainfall = form.slider('Select the value of Rainfall Level',
    0.0, 300.0)
    import requests
    API_KEY = "<Enter API Key>"
    area="Coimbatore"
    count=str(count)
    url = (f"http://pro.openweathermap.org/data/2.5/forecast/climate?q={area}&cnt={count}&appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    submit = form.form_submit_button("Submit")
    if submit:
        st.session_state.past.append("suggest me a best suited crop")
        temp = data["list"][int(count)-1]["temp"]["day"]
        humidity = data["list"][int(count)-1]["humidity"]
        best_crop = "The best crop to grow with these parameters is " + analyze(n,p,k,temp,humidity,ph,rainfall)
        st.session_state.generated.append(best_crop)
if user_input=="crop yield estimation":
    with st.form("my_form"):
        st.write("Inside the form")
        district = st.selectbox('Select District', dist_list)
        Crop = st.selectbox('Select Crop', crop_list)
        Area = st.number_input('Enter area')
        soil_type = st.selectbox('Select soil type', soil_list)
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
    if submitted:
        print(predict_yield(district,Crop,Area,soil_type))
        pred = "The predicted YIELD for given attributes is approximately:  " + str(predict_yield(district,Crop,Area,soil_type)) + " tons"
        st.success(pred)
if user_input=="trends of crop price":
    option = st.selectbox(
    'Select a Crop to forecast',
    ('','arhar', 'bajra', 'barley','copra','cotton','sesamum','gram','groundnut','jowar','maize','masoor','moong','niger','paddy','ragi','rape','jute','safflower','soyabean','sugarcane','sunflower','urad','wheat'))
    if option!='':
        import streamlit as st
        import pandas as pd
        import plotly.express as px
        data = TwelveMonthsForecast(option)[2]

        df = pd.DataFrame(data, columns=['Month', 'Price', 'Change'])

        # Create the chart using Plotly
        fig = px.line(df, x='Month', y='Price', title='Price of a product over time')
        fig.update_traces(mode='markers+lines', marker=dict(size=8, symbol='circle', color='blue'), line=dict(width=2))

        # Add the percentage change as a secondary y-axis
        fig.add_scatter(x=df['Month'], y=df['Change'], name='Percentage Change', mode='lines', yaxis='y2', line=dict(width=2, color='red'))

        # Set the layout of the chart
        fig.update_layout(
            yaxis=dict(title='Price'),
            yaxis2=dict(title='Percentage Change', overlaying='y', side='right', showgrid=False),
            xaxis=dict(tickangle=45),
            title=dict(x=0.5, y=0.9, xanchor='center', yanchor='top')
        )
        st.session_state.past.append('trends of crop price')
        # Display the chart in Streamlit
        st.plotly_chart(fig)


        
if user_input=="forecast crop price":
    option = st.selectbox(
    'Select a Crop to forecast',
    ('','arhar', 'bajra', 'barley','copra','cotton','sesamum','gram','groundnut','jowar','maize','masoor','moong','niger','paddy','ragi','rape','jute','safflower','soyabean','sugarcane','sunflower','urad','wheat'))
    if option!='':
        pro = crop_profile(option)
        forecast = ''
        st.session_state.past.append('forecast crop price')
        st.session_state.generated.append("Price of "+option+ " is estimated as "+ "₹"+str(pro['forecast_y'][0])  + " on "+ str(pro['forecast_x'][0]))

if user_input=="suggest me a best suited crop":
    form = st.form("my_form",clear_on_submit=False)
    n = form.slider('Select the value of Nitrogen Level',
    0, 150)
    p = form.slider('Select the value of Phosphorus Level',
    0, 100)
    k = form.slider('Select the value of Potassium Level',
    0, 100)
    temp = form.slider('Select the value of Temperature Level',
    0.0, 50.0)
    humidity = form.slider('Select the value of Humidity Level',
    0.0, 100.0)
    ph = form.slider('Select the value of PH Level',
    0.0, 10.0)
    rainfall = form.slider('Select the value of Rainfall Level',
    0.0, 300.0)
    submit = form.form_submit_button("Submit")
    if submit:
        st.session_state.past.append("suggest me a best suited crop")
        best_crop = "The best crop to grow with these parameters is " + analyze(n,p,k,temp,humidity,ph,rainfall)
        st.session_state.generated.append(best_crop)
if user_input == "what is this disease?":
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    if uploaded_file:
        with open(os.path.join("temp",uploaded_file.name), mode='wb') as w:
            w.write(uploaded_file.getvalue())
        prediction = predict("temp")
        st.session_state.past.append("what is this disease?")
        disease = "Disease Detected: " + prediction[uploaded_file.name]['prediction'] + "\n" + prediction[uploaded_file.name]['description'] + "\n" + prediction[uploaded_file.name]['symptoms'] + "\n" + prediction[uploaded_file.name]['source']
        st.session_state.generated.append(disease)
        import os
        import glob

        files = glob.glob("temp/*")
        for f in files:
            os.remove(f)
if user_input and user_input not in ["what is this disease?","suggest me a best suited crop","auto suggest me a best suited crop","forecast crop price","crop yield estimation","suggest me a best suited crop to grow in future","feedback","yes","no"]:
    print(chat.initialization(user_input))
    st.session_state.past.append(user_input)
    st.session_state.generated.append(chat.initialization(user_input))

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))