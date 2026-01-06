import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/DELL/Downloads/Multiple Disease Detection/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/DELL/Downloads/Multiple Disease Detection/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/DELL/Downloads/Multiple Disease Detection/parkinsons_model.sav','rb'))
 
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           default_index=0
                           )
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    Pregnancies	= st.text_input('Number of Pregnancies')
    Glucose	= st.text_input('Glucose Level')
    BloodPressure =	st.text_input('Blood Pressure Level')
    SkinThickness =	st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI')	
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the person')
    
    diabetes_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis = 'The person is Diabetic.'
        else:
            diabetes_diagnosis = 'The person is not Diabetic.'
    st.success(diabetes_diagnosis)
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    age	= st.text_input('Age of the person')
    sex	= st.text_input('Sex of the person')
    cp =	st.text_input('CP value')
    trestbps =	st.text_input('TRESTBPS value')
    chol = st.text_input('CHOL value')
    fbs = st.text_input('FBS value')	
    restecg = st.text_input('RESTECG value')
    thalach = st.text_input('THALACH value')
    exang = st.text_input('EXANG value')
    oldpeak	= st.text_input('OLDPEAK value')
    slope = st.text_input('SLOPE value')
    ca	= st.text_input('CA value')
    thal = st.text_input('THAL value')
    
    heart_disease_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_disease_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_disease_prediction[0]==1):
            heart_disease_diagnosis = 'The person has Heart Disease.'
        else:
            heart_disease_diagnosis = 'The person has no Heart Disease.'
    st.success(heart_disease_diagnosis)
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction using ML')