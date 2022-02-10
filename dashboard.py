import pandas as pd
#import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Leanne's Bent Carrot Dashboard",
                   page_icon=":eggplant:",
                   layout="wide"
                    )
 
#@st.cache 
#def get_data_from_excel():
df = pd.read_excel(
    io='https://github.com/goodfellajohn/gloom_monster_inits/blob/c8c5eb9ba4794034b4b01a42089c1573230ec3ff/Gloomhaven%20Monster%20Stats.xlsx',#'D:\gloomhaven_streamlit\Gloomhaven Monster Stats.xlsx',
    engine='openpyxl',
    sheet_name='Monsters',
    skiprows=0,
    usecols='A:L',
    nrows=545,
    )
    
#df = get_data_from_excel()

#--- SIDEBAR ----
st.sidebar.header("Select Scenario Level & Monsters:")
scenario_level = st.sidebar.multiselect(
    "Select the Scenario Level:",
    options=df["Scenario Level"].unique(),
    default=df["Scenario Level"][1]
)

monster_type = st.sidebar.multiselect(
    "Select the Monster:",
    options=df["Monster"].unique(),
    default=df["Monster"][10]
)


df_selection = df.query(
    "`Scenario Level` == @scenario_level & Monster == @monster_type"
)

st.dataframe(df_selection)

#--- MAINPAGE -----
st.title(":eggplant: Sister Mary Clarence & Vlad II Killue's Conquest")
st.markdown("##")




# Hiding the hamburger menu, banner color, and footer mentioning streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
