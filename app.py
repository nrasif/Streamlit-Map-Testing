# Basic libraries
import pandas as pd
import numpy as np
import os
import glob
from statistics import mean

# Map libraries
import folium
from folium import plugins
from folium.plugins import Search
import geopandas as gpd
import branca

# Plotting libraries
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

# Streamlit libraries
import streamlit as st
from streamlit_folium import folium_static
import streamlit_nested_layout


# Dataset
All_Blocks = gpd.read_file(r'GeoJSON Files/All_Blocks.geojson')

# calculate the center of map
bounds = All_Blocks.total_bounds
x = mean([bounds[0], bounds[2]])
y = mean([bounds[1], bounds[3]])
location = (y, x)

# Initial customizations
st.set_page_config(
    page_title="Testing Map",
    layout="wide",
    initial_sidebar_state="auto"
)

# Styling
st.markdown("""
<style>
[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
    gap: 0rem;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
[data-testid=column]:nth-of-type(3) [data-testid=stVerticalBlock]{
    gap: 0rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:7px !important;
}
.other-font {
    font-size:21px !important;
}
.spacing-font {
    font-size:5px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(2)
        {
            border:1px;
            text-align: center;
        }
    """, unsafe_allow_html=True)

hide_menu_style = '''
<style>
#MainMenu {
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)

# styling on tables pop up
def make_popup(df):
    blockname = df["Block_Name"]
    status = df["Status"]
    operator = df["Operator"]
    kilos = df["Sq. Kilometers"]
    miles = df["Sq. Miles"]
        
    left_col_color = "#65b3d0"
    right_col_color = "#ebf2f7"
    
    html = """
    <!DOCTYPE html>
    <html>
    
    <head>
    <strong><h4 style="margin-bottom:30px; width:200px; font-size: 25px;">{}</strong></h4>""".format(blockname) + """

    
    </head>
        <table style="height: 126px; width: 300px;">
    <tbody>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #151515;">Status</span></td>
    <td style="width: 200px;background-color: """ + right_col_color + """;">{}</td>""".format(status) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #151515;">Operator</span></td>
    <td style="width: 200px;background-color: """ + right_col_color + """;">{}</td>""".format(operator) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #151515;">Sq. Kilometers</span></td>
    <td style="width: 200px;background-color: """ + right_col_color + """;">{}</td>""".format(kilos) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #151515;">Sq. Miles</span></td>
    <td style="width: 200px;background-color: """ + right_col_color + """;">{}</td>""".format(miles) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html

text, display = st.columns([1,4])
with text:
    block_title = '<p style="color:#65b3d0; font-size: 45px;"><strong>Dummy Blocks </strong> </p>'
    st.markdown(block_title, unsafe_allow_html=True)
    
    st.markdown('<p class="spacing-font"> &nbsp; </p>',
                unsafe_allow_html=True)
    
    st.markdown('**Summary**')
    st.write('This block data are dummy, intended for testing purposes. All blocks are not representing the real conditions.')
    
    st.markdown('<p class="other-font"> &nbsp; </p>',
                unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(['Info', 'Filter', 'Download'])

    with tab1:
        
        st.markdown('**Detail**')

        col1, mid, col2 = st.columns([1,1, 20])

        with col1:
            st.markdown('<p class="big-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.image(r'icon/data_icon.png', width=25)
            st.markdown('<p class="other-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.image(r'icon/info_icon.png', width=25)
            st.markdown('<p class="other-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.image(r'icon/date_icon.png', width=25)
            st.markdown('<p class="other-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.image(r'icon/world_icon.png', width=25)
            st.markdown('<p class="other-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.image(r'icon/lock_icon.png', width=27)
        
        with col2:
            # st.markdown('<p class="big-font"> </p>',
            #             unsafe_allow_html=True)
            st.caption('Feature Layer')
            st.markdown('**Dataset**')

            st.markdown('<p class="big-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.caption('Updated Info')
            st.markdown('**03 February 2023**')

            st.markdown('<p class="big-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.caption('Publication Date')
            st.markdown('**04 February 2023**')

            st.markdown('<p class="big-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.caption('Anyone can view this content')
            st.markdown('**Public**')

            st.markdown('<p class="big-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            st.caption('Request permission to use')
            st.markdown('**No License**')
            st.markdown('<p class="other-font"> &nbsp; </p>',
                        unsafe_allow_html=True)

        st.button('Get PDF files for more information')
        
    with tab2:

        with st.expander('Block name'):
            option_block = st.multiselect('Select the block name',   (All_Blocks['Block_Name']), default=All_Blocks['Block_Name'], label_visibility='collapsed')
            option_block_ = All_Blocks[All_Blocks['Block_Name'].isin(option_block)]
        
        st.markdown('<p class="big-font"> &nbsp; </p>',
        unsafe_allow_html=True)
        
        with st.expander('Status'):
            checkbox_stat_1 = st.checkbox('Exploration')
            checkbox_stat_2 = st.checkbox('Production')
            
            if checkbox_stat_1:
                option_block_ = option_block_[option_block_['Status'] == 'Exploration']
            elif checkbox_stat_2:
                option_block_ = option_block_[option_block_['Status'] == 'Production']
            elif checkbox_stat_1 and checkbox_stat_2:
                option_block_ = All_Blocks[All_Blocks['Status'].isin(['Exploration','Production'])]
            
        st.markdown('<p class="big-font"> &nbsp; </p>',
        unsafe_allow_html=True)
        
        with st.expander('Operator'):
            option_operator = st.multiselect(' ', (option_block_['Operator'].unique()), default = option_block_['Operator'].unique(), label_visibility='collapsed')
            option_block_ = option_block_[option_block_['Operator'].isin(option_operator)]
        
        st.markdown('<p class="big-font"> &nbsp; </p>',
        unsafe_allow_html=True)

        with st.expander('Shape area in Sq. Kilometers'):
            st.markdown('<p class="big-font"> &nbsp; </p>',
                        unsafe_allow_html=True)
            option_kilos = st.slider('Sq. Kilometers of block area', float(0.0), float(option_block_['Sq. Kilometers'].max() + 50), float(option_block_['Sq. Kilometers'].max()), 
                                    label_visibility='collapsed')
        
            option_block_ = option_block_[option_block_['Sq. Kilometers'] <= option_kilos]
    
    with tab3:
        @st.cache
        def convert_csv(df):
            return df.to_csv().encode('utf-8')
        
        csv = convert_csv(option_block_)
        
        st.download_button(
            label='Download data as CSV',
            data=csv,
            file_name='Data_map.csv'
        )
        
        
with display:
    st.markdown('<p class="spacing-font"> &nbsp; </p>',
                unsafe_allow_html=True)
    # Initialize map (blank layer map with coordinate center in Aceh)
    map1 = folium.Map(location=location,
                    zoom_start=11, control_scale=300, tiles=None)

    # Put ESRI Satellite for the layer map
    tile = folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        overlay=False,
        control=False
    ).add_to(map1)

    # put a minimap on bottom corner of the main map (optional, can be turned off) and other plugins such as szroll zoom toggler, fullscreen, etc
    minimap = plugins.MiniMap(toggle_display=True)
    map1.add_child(minimap)
    plugins.ScrollZoomToggler().add_to(map1)
    plugins.Fullscreen(position="topright").add_to(map1)
    plugins.Draw(position='topright').add_to(map1)
    
    
    def filter_by_name(df, parameter):
        return df[df['Block_Name'].isin(parameter)]
    
    # option_block = st.multiselect('Select the block name', (All_Blocks['Block_Name']), default=All_Blocks['Block_Name'])
    df_filter = filter_by_name(option_block_,option_block)
    
    # Adding blocks to the main map
    def load_map(df_):
        for i, row in df_.iterrows():
            geo_json = folium.features.GeoJson(row.geometry.__geo_interface__, name=str(i), 
                                                style_function=
                                                lambda feature: {
                                                'fillColor':  '#65b3d0',
                                                #    'fillColor': '#F1D581' if 'x' in feature['properties']['Status'] == 'Exploration' else '#65b3d0',
                                                'color': 'black',
                                                'weight': 3,
                                                'fillOpacity': 0.2,
                                                'dashArray': '5,5'
                                            },

                                            highlight_function=lambda x: {
                                                'fillOpacity': 1},

                                            tooltip=folium.features.Tooltip(All_Blocks.iloc[i]['Block_Name'], sticky=False))
                                                # fields=All_Blocks.iloc[i]['Block_Name'], aliases=['Name']))
            
            geo_json.add_child(folium.Popup(make_popup(All_Blocks.iloc[i])))
            return (geo_json.add_to(map1))
    load_map(df_ = df_filter)

    folium_static(map1, width=1350, height=800)