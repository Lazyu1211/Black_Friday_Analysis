import pandas as pd
import matplotlib.pyplot as plt

PATH = "/Users/junyuwu/black_friday(First project)/train.csv"

df = pd.read_csv(PATH) 
df["Product_Category_2"].fillna(df["Product_Category_2"][1].mean(),inplace=True)
df["Product_Category_3"].fillna(df["Product_Category_3"][1].mean(),inplace=True)


def get_gender():
    bygender1 = df.groupby("Gender")["Purchase"].sum().to_frame()
    bygender1.reset_index(inplace=True)
    #print(bygender1)
    return bygender1

def get_age():
    male = df["Gender"] == "M"
    all_male = df[male]
    male_age = all_male.groupby(["Age"])["Purchase"].sum().to_frame()
    male_age.reset_index(inplace=True)
    #print(male_age)
    return male_age

def get_mar():
    main_cus = df["Age"].isin(["18-25", "26-35", "36-45"])
    age_cus = df[main_cus]
    male_cus = age_cus["Gender"] == "M"
    age_main_male_cus = age_cus[male_cus]
    bymar_sta = age_main_male_cus.groupby("Marital_Status")["Purchase"].sum().to_frame()
    bymar_sta.reset_index(inplace=True)
    #print(bymar_sta)
    return bymar_sta

def get_occ():
    main_cus = df["Age"].isin(["18-25", "26-35", "36-45"])
    age_cus = df[main_cus]
    male_cus = age_cus["Gender"] == "M"
    age_main_male_cus = age_cus[male_cus]
    byocc = age_main_male_cus.groupby("Occupation")["Purchase"].sum().to_frame()
    byocc.reset_index(inplace=True)
    #print(byocc)
    return byocc

def get_stay_year():
    main_cus = df["Age"].isin(["18-25", "26-35", "36-45"])
    age_cus = df[main_cus]
    male_cus = age_cus["Gender"] == "M"
    age_main_male_cus = age_cus[male_cus]
    bycity_years = age_main_male_cus.groupby("Stay_In_Current_City_Years")["Purchase"].sum().to_frame()
    bycity_years.reset_index(inplace=True)
    #print(bycity_years)
    return bycity_years

def get_city():
    main_cus = df["Age"].isin(["18-25", "26-35", "36-45"])
    age_cus = df[main_cus]
    male_cus = age_cus["Gender"] == "M"
    age_main_male_cus = age_cus[male_cus]
    bycity = age_main_male_cus.groupby("City_Category")["Purchase"].sum().to_frame()
    bycity.reset_index(inplace=True)
    return bycity