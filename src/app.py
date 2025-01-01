import streamlit as st

# Set page config
st.set_page_config(page_title="My First Streamlit App", page_icon="✨", layout="wide")

# Add a title
st.title("Dishynator")

# Add a sidebar
st.sidebar.header("Settings")

# Add some input widgets to the sidebar
user_name = st.sidebar.text_input("Enter your name", "Guest")
number = st.sidebar.slider("Select a number", 0, 100, 50)

# Main content
st.write(f"Hello, {user_name}!")

with st.container():

    st.header("Data analysis")

    # Add a multi-file uploader
    uploaded_files = st.file_uploader(
        "Choose files", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
    )
    if uploaded_files:
        st.write(f"Number of files uploaded: {len(uploaded_files)}")

        # You can process each file
        for file in uploaded_files:
            st.write(f"Filename: {file.name}")
            st.write(f"File size: {file.size} bytes")  # Size in bytes
            st.write(f"File type: {file.type}")
            st.write("---")

    # ... existing code ...


# Add a button
if st.button("Click me!"):
    st.balloons()
    st.success("Thanks for clicking!")
