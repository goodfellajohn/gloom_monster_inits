import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Leanne's Gloom Dashboard",
                   page_icon=":bear:",
                   layout="wide",
                   initial_sidebar_state = "expanded"
                    )
 
#@st.cache 
#def get_data_from_excel():
df = pd.read_excel(
    io='https://github.com/goodfellajohn/gloom_monster_inits/blob/c8c5eb9ba4794034b4b01a42089c1573230ec3ff/Gloomhaven%20Monster%20Stats.xlsx?raw=true',#'D:\gloomhaven_streamlit\Gloomhaven Monster Stats.xlsx',
    engine='openpyxl',
    sheet_name='Monsters',
    skiprows=0,
    usecols='A:L',
    nrows=545,
    )
    
df2 = df[['Monster','Initiatives ','Attributes','Scenario Level', 'Monster Level']]
#df = get_data_from_excel()

def color_elite(val):
    color = 'yellow' if "Elite" in val else ''
    return f'background-color: {color}'
  
def highlight_elite(s):
    return ['background-color: yellow']*len(s) if "Elite" in s.['Monster Level'] else ['background-color: ']*len(s)

htp="https://raw.githubusercontent.com/goodfellajohn/gloom_monster_inits/main/jeez.jpg"
#st.image(htp, caption= 'logo', width=350)
#image = Image.open('https://raw.githubusercontent.com/goodfellajohn/gloom_monster_inits/main/jeez.jpg')

#--- SIDEBAR ----
st.sidebar.header("Select Scenario Level & Monsters:")
scenario_level = st.sidebar.multiselect(
    "Select the Scenario Level:",
    options=df["Scenario Level"].unique(),
    default=df["Scenario Level"].unique()[2]
)

monster_type = st.sidebar.multiselect(
    "Select the Monster:",
    options=df["Monster"].unique(),
    default=df["Monster"].unique()[7]
)

df_selection_filtered = df2.query(
    "`Scenario Level` == @scenario_level & Monster == @monster_type"
)

df_selection = df.query(
    "`Scenario Level` == @scenario_level & Monster == @monster_type"
)



#--- MAINPAGE -----
st.title(":hocho: Sister Mary Clarence & Vlad II Killéu's Conquest :droplet::bear:")
st.markdown("## Minimal List")
#st.dataframe(df_selection_filtered)
st.dataframe(df_selection_filtered.style.apply(highlight_elite, axis=1))
st.dataframe(df_selection_filtered.style.applymap(color_elite, subset=['Monster Level']))
st.markdown("## :bar_chart: Detailed List of all values below")
st.dataframe(df_selection)
st.image(htp, caption='When Sister Mary Clarence exhausts....', width=350)



# Hiding the hamburger menu, banner color, and footer mentioning streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none;}
            .blank {display:none;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
