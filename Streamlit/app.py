import streamlit as st
import pandas as pd
import numpy as np


#Title of the app
st.title('Hello Streamlit')

#Display a simple text
st.write('This is a simple page')

df=pd.DataFrame({
    'first column': [1,2,3],
    'second column': [3,4,5]
})

#Display the df
st.write(f'Heres the df: {df}')

# create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)







