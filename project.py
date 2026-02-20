import streamlit as st
import pandas as pd
import matplotlib.pyploy as plt
st.title("ML Model Demo")
st.header("predictive System")
st.subheader("Enter Inputs Below")
st.write("This app demonstrates ML model Deployment")
name=st.text_input("Enter Customer Name")
age=st.number_input("Enter Age", min_value=0, max_value=100)
salary=st.slider("select salary",min_value=10000,max_value=100000,value=25000)
gender=st.selectbox("select Gender",["male","Female"])
education=st.radio("Education Level",["UG",["PG","PHD"]])
agree=st.checkbox("I agree to terms")
uploded_file=st.file_uploader("upload Image", type=["jpg","png"])
if st.button("predict"):
       st.success("Predict Successful")
       st.warning("warning")
       st.error("Error, enter valid input")
df= pd.DataFrame({"A":[1,2],"B":[3,4]})
st.dataframe(df)
appointment=st.date_input("select the appointment date")
st.write("Appointment Date:", appointment )
time=st.time_input("Select Appointment time")
st.write("Appointment Time:",time)
st.metric("Acuracy","92%","+2")
st.image("peacock1.jpg", caption="pecock")


#sidebar
st.sidebar.title("Navigation")
page=st.sidebar.selectbox("choose Page",["Home","prediction"])


col1, col2=st.columns(2)
with col1:
       st.write("Left")

with col2:
       st.write("Right")
with st.spinner("preprocessing.."):
       st.progress(50)
#t.cache_resource
#
#ef load_model():
#      return joblib.load("model.pkl")
#odel=load_model()


data=(
    'Name':['Abdul Aziz','Anna','Bob','peter',],
    'Age':[28,24,35,32,54,56,67],
    'city':["Hyd","Mumbai","kolkata","bhopal","chennai","Delhi","jaipur"])

data_df=pd.DataFrame(data)
st.dataframe(data_df)
st.pyplot()


rand=np.random.normal(1,2,size=20)
fig, ax=plt.subplots()
ax.hist(rand,bins=15)
st.pyplot(fig)