import streamlit as st
import requests
import os



st.title("Heart Disease Prediction")

Age    =    st.number_input("Age")
Sex    =      st.selectbox('Sex',
             ["M","F"])
ChestPainType  =st.selectbox("ChestPainType",
            ["ASY","NAP","ATA","TA"])
RestingBP    = st.number_input("RestingBP")
Cholesterol  =  st.number_input("Cholesterol")
FastingBS    =  st.number_input("FastingBS")
RestingECG  =   st.selectbox("RestingECG",
                ["Normal","LVH","ST"])
MaxHR       =  st.number_input("MaxHR")
ExerciseAngina =st.selectbox("ExerciseAngina",
                            ["N","Y"])
Oldpeak =st.number_input("Oldpeak")
ST_Slope =st.selectbox("ST_Slope",
                      ["Flat","Up","Down"])


if st.button("predict disease"):
    
    
    data={
        'Age':Age,
        'Sex':Sex, 
        'ChestPainType':ChestPainType,
        'RestingBP':RestingBP, 
        'Cholesterol':Cholesterol,
        'FastingBS':FastingBS,
       'RestingECG':RestingECG,
       'MaxHR':MaxHR,
       'ExerciseAngina':ExerciseAngina,
       'Oldpeak':Oldpeak,
       'ST_Slope':ST_Slope,
       
    }
    
    try:

        API_URL=os.getenv("API_URL","http://127.0.0.1:8000")
        response=requests.post(f"{API_URL}/predict",json=data)

        if response.status_code==200:
            result=response.json()

            st.subheader("Result")

            if result["prediction"] == 1:
                st.error(
                    f'{result["result"]}\n\n'
                    
                )
            else:
                st.success(
                    f'{result["result"]}\n\n'
                    )
             

        else:
            st.error("Prediction failed")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running.")

            

    