import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_authenticator import Authenticate
import random
import string

# Function to generate a random string to use as a secret key
def generate_secret_key(length=24):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Assuming you've already hashed the passwords using a separate script
users = {
    "user1": {
        "name": "Alice",
        "username": "alice",
        "password": "$2b$12$cp1Eo2n2WxcjmWznnPjbjerdSxmbKzEV8YmYSSf/vpOg1LCj0oH4i",  # Replace with actual hashed value
        "email": "alice@example.com"
    },
    "user2": {
        "name": "Bob",
        "username": "bob",
        "password": "$2b$12$.ZpsS3X7m9GA3rm3PakOdejxKbvgCjBHo51WSJOFkRJq7HKDkqdBa",  # Replace with actual hashed value
        "email": "bob@example.com"
    }
}

# Format the credentials as expected by streamlit-authenticator
credentials = {
    "usernames": {
        user_detail["username"]: {
            "name": user_detail["name"],
            "password": user_detail["password"],
            "email": user_detail["email"]
        } for user_detail in users.values()
    }
}

# Define a cookie name and a secret key
cookie_name = "streamlit_authenticator"
secret_key = generate_secret_key()

# Create an authentication object with the corrected format
authenticator = Authenticate(credentials, cookie_name, secret_key)

# Start the authentication process
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.title('Welcome to CSV/Excel File Analyzer App')

    # File upload and data visualization functionalities here
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        # Read the file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        else:
            df = pd.read_excel(uploaded_file)

        # Display the dataframe
        st.write(df)

        # Select columns for visualization
        st.subheader('Select Columns for Visualization')
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect('Select columns', all_columns, default=all_columns[:2])
        
        if len(selected_columns) < 2:
            st.error('Please select at least two columns for visualization.')
        else:
            # Visualization options
            plot_type = st.selectbox("Select Plot Type", ('Line Plot', 'Bar Chart', 'Scatter Plot', 'Histogram'))

            # Generate and display the plot based on the selected type and columns
            if plot_type == 'Line Plot':
                fig = px.line(df, x=selected_columns[0], y=selected_columns[1])
                st.plotly_chart(fig)

            elif plot_type == 'Bar Chart':
                fig = px.bar(df, x=selected_columns[0], y=selected_columns[1])
                st.plotly_chart(fig)

            elif plot_type == 'Scatter Plot':
                fig = px.scatter(df, x=selected_columns[0], y=selected_columns[1])
                st.plotly_chart(fig)

            elif plot_type == 'Histogram':
                fig = px.histogram(df, x=selected_columns[0], y=selected_columns[1])
                st.plotly_chart(fig)

elif authentication_status == False:
    st.error('Username/password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')
