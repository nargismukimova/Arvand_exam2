import numpy as np
import pickle
import pandas as pd 
import streamlit as st
import joblib

model_selected = st.radio('What analysis do you want to use', ('DecisionTreeClassifier', 'LogisticRegression', 'KNeighborsClassifier'))


if model_selected == 'DecisionTreeClassifier':
    pickle_in = open("scoring_Arvand_ModelTree.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['LogisticRegression', 'Default']:
    pickle_in = open("scoring_Arvand_LogReg.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['KNeighborsClassifier', 'Default']:
    pickle_in = open("scoring_Arvand_KNeighborsClassifier.pkl","rb")
    classifier=pickle.load(pickle_in)

def predict_note_authentication(FamilySize, BusExper, Credit_Sum, Credit_period, Month_Sum, Lgot_period, Credit_Stage, isMale, family_condition, Education, Filial_code, level, typeofcredit, Nationality_code, Activity_Direction, Sector, Region_code, Age, finish_date):
    prediction=classifier.predict([[FamilySize, BusExper, Credit_Sum, Credit_period, Month_Sum, Lgot_period, Credit_Stage, isMale, family_condition, Education, Filial_code, level, typeofcredit, Nationality_code, Activity_Direction, Sector, Region_code, Age, finish_date]])
    print(prediction)
    return prediction    
             

def main():
    st.title("Прогноз выдачи кредита")
    st.markdown("Учебная модель поможет предсказать одобрение выдачи кредита на основе введенных данных.")
    
    
    FamilySize = st.radio ('Сколько людей в семье?')  
    BusExper = st.radio ('Опыт работы? (6 - 6-мох, 4 - 4-мох, 21 - 20+', (4,6,21))
    Credit_Sum = st.radio ('Сумма кредита')
    Credit_period = st.radio ('Срок кредита')
    Month_Sum = st.radio ('Сумма погашения в месяц')
    Lgot_period = st.radio ('Льготный период')
    Credit_Stage = st.radio ('Этап кредитования')
    isMale = st.radio ('Ваш пол? (0 - Женский, 1 - Мужской', (0,1))
    family_condition = st.radio ('Семейное состояние? (1 - Оиладор, 2 - Беоила, 3 - Бевамард, 4 - Чудошуда', (1,2,3,4))
    Education = st.radio ('Уровень образования? (1 - Миёна, 2 - Оли, 3 - Миёнаи махсус, 4 - Олии нопурра, 5 - Миёнаи нопурра', (1,2,3,4,5))
    Filial_code = st.radio ('Расположение филиала? (1 - Ч. Расулов, 2 - Хучанд, 3 - Истаравшан, 4 - Исфара, 5 - Душанбе, 6 - Панчакент', (1,2,3,4,5,6)) 
    level = st.radio ('Уровень клиента? (1 - Хамкори, 2 - Шарик, 3 - VIP, 4 - Бовари', (1,2,3,4))
    typeofcredit = st.radio ('Тип кредита? (1 - Кредит на предпринимательскую деятельность, 2 - Потребительский кредит, 3 - Энергосберегающие технологии, 4 - Жилищный кредит', (1,2,3,4))
    Nationality_code = st.radio ('Национальность? (0 - Другие, 1 - Точик, 2 - Узбек, 3 - Тотор, 4 - Рус, 5 - Киргиз, 6 - Украин, 7 - Карис, 8 - Карачои', (0,1,2,3,4,5,6,7,8))
    Activity_Direction = st.radio ('Ваша деятельность?')
    Sector = st.radio ('Ваш сектор?')
    Region_code = st.radio ('Ваш регион?')
    Age = st.radio ('Ваш возраст?')
    finish_date = st.radio ('Дата завершения?')
                                                                                                                                           
      
     
    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(FamilySize, BusExper, Credit_Sum, Credit_period, Month_Sum, Lgot_period, Credit_Stage, isMale, family_condition, Education, Filial_code, level, typeofcredit, Nationality_code, Activity_Direction, Sector, Region_code, Age, finish_date)) 
          
    st.success('Результат системы (1 - Кредит ободрен, 0 - Кредиту отказано) {}'.format(result))
           
    
    
    
 
if __name__ == '__main__':
    main()


