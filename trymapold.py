import streamlit as st

st.title('Map Iframe Generator')

city1 = st.text_input('Enter first city:')
city2 = st.text_input('Enter second city:')

if st.button('Generate Map'):

  map_html = f"""
    <b>Directions from:</b> {city1} 
    <br>
    <b>To:</b> {city2}
  """

  iframe = f'<iframe width="600" height="450" frameborder="0" srcdoc="{map_html}"></iframe>'

  st.markdown(iframe, unsafe_allow_html=True)