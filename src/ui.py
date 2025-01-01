import streamlit as st
from image_processing import mask_to_bytes


def setup_page():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="Dishynator - Image Analysis", page_icon="🌿", layout="wide"
    )
    st.title("Dishynator")
    st.subheader("Plant Image Analysis")


def sidebar_settings():
    """Create and return sidebar settings."""
    with st.sidebar:
        st.header("Settings")
        settings = {
            "show_original": st.checkbox("Show original image", value=True),
            "show_red_mask": st.checkbox("Show red pixels mask", value=True),
        }
    return settings


def display_results(image, settings, red_ratio=None, red_mask=None):
    """Display the image processing results."""
    cols = st.columns(2)

    if settings["show_original"]:
        with cols[0]:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)
            if red_ratio is not None:
                st.metric(
                    "Red Pixel Ratio",
                    f"{red_ratio:.2%}",
                    help="Percentage of pixels identified as red in the image",
                )

    if settings["show_red_mask"]:
        with cols[1]:
            st.subheader("Generated Mask")
            st.image(red_mask, caption="Red Pixels Mask", use_column_width=True)


def add_download_button(mask, original_filename):
    """Add a download button for the mask."""
    if mask is not None:
        mask_bytes = mask_to_bytes(mask)
        st.download_button(
            label="Download Mask",
            data=mask_bytes,
            file_name=f"mask_{original_filename}",
            mime="image/png",
        )


def add_batch_download_button(masks, filenames):
    """Add a button to download all masks as ZIP."""
    if masks and filenames:
        from io import BytesIO
        import zipfile

        # Create ZIP file in memory
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for mask, filename in zip(masks, filenames):
                mask_bytes = mask_to_bytes(mask)
                zip_file.writestr(f"mask_{filename}", mask_bytes)

        # Add download button for ZIP
        st.download_button(
            label="Download All Masks",
            data=zip_buffer.getvalue(),
            file_name="all_masks.zip",
            mime="application/zip",
        )
