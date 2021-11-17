import streamlit as st

def main():
    if 'count' not in st.session_state:
        st.session_state.count = False
    st.header('CMPE 256 - Advanced Data Mining')
    main_option = st.multiselect('Please type the author or the article name to view:',('Swathi', 'Aryan', 'Yash'))
    button_value = st.button('Click to view available filters')
    if button_value: st.session_state.count = True
    if st.session_state.count:
        radio_filter = st.radio(label = 'Use these filters to narrow down the views', options = ['By Author','By Date', 'By Opinion'])
        if radio_filter == 'By Author':
            option = st.multiselect('Please select the author you want to view the news articles of:',('Swathi', 'Aryan', 'Yash'))
        elif radio_filter == 'By Date':
            date_input = st.date_input('start date')
        elif radio_filter == 'By Opinion':
            radio_input = st.radio(label = 'Radio buttons', options = ['Positive','Negative'])
main()
