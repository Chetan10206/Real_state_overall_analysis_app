import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import ast


st.set_page_config(page_title="analysis of Gurgaon")

st.title("Analysis")     


new_df = pd.read_csv('datasets/data_visualization1.csv')
wordcloud_df = pd.read_csv('datasets/wordcloud_of_features.csv')

#######################################

group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()


st.header('Sector Price per Sqft Geomap')
fig1 = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig1,use_container_width=True)

############################

st.divider()
st.header("Property Features WordCloud")

sectors = ['Overall'] + sorted(wordcloud_df['sector'].dropna().unique().tolist())
sector = st.selectbox("Select Sector", sectors)

if sector == 'Overall':
    features = wordcloud_df['features'].dropna()
else:
    features = wordcloud_df.loc[wordcloud_df['sector'] == sector, 'features'].dropna()

main = []
for item in features.apply(ast.literal_eval):
    main.extend(item)

feature_text = ' '.join(main)

if feature_text.strip():
    wc = WordCloud(width=1000, height=500, background_color='white').generate(feature_text)
    fig2, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig2)
    plt.close(fig2)
else:
    st.warning("No property features available for this selection.")


#############################################

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig3 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig3, use_container_width=True)


##############################################

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig4 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig4, use_container_width=True)
else:

    fig4 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig4, use_container_width=True)



##############################

st.header('Side by Side BHK price comparison')

fig5 = px.box(new_df[new_df['bedRoom'] <= 5], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig5, use_container_width=True)

#######################################


st.header('Side by Side Distribution of price for property type')


fig6 = plt.figure(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig6)