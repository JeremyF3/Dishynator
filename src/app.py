import streamlit as st
from ui import setup_page, sidebar_settings, display_results, add_download_button
from image_processing import load_image, calculate_red_ratio


def main():
    # Setup the page
    setup_page()

    # Get settings from sidebar
    settings = sidebar_settings()

    # Main content
    with st.container():
        st.header("Upload Images")

        # Add a file uploader
        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            st.write(f"Processing {len(uploaded_files)} images...")

            # Process each file
            for uploaded_file in uploaded_files:
                with st.expander(f"Image: {uploaded_file.name}", expanded=True):
                    # Load and process image
                    image = load_image(uploaded_file)
                    red_ratio, red_mask = calculate_red_ratio(image)

                    # Display results
                    display_results(
                        image, settings, red_ratio=red_ratio, red_mask=red_mask
                    )

                    # Add download button
                    add_download_button(red_mask, uploaded_file.name)

    # Footer
    st.markdown("---")
    st.markdown("Upload plant images to generate object masks.")


if __name__ == "__main__":
    main()
