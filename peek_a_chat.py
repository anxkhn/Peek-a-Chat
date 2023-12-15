import streamlit as st
import pyperclip

def create_text_clipboard(part1, part2, filler):
    """
    Concatenates part1, filler, and part2 to form a text snippet.
    Copies the resulting snippet to the clipboard.

    Parameters:
    - part1 (str): The content displayed initially in the message.
    - part2 (str): The content hidden until the user clicks 'Read More.'
    - filler (str): A string used to achieve a specific length for the combined message.
    """
    result = f"{part1}{filler}{part2}"

    # Copy the result to the clipboard
    pyperclip.copy(result)

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Peek-a-Chat",
        page_icon="🔍💬",
        layout="wide",
    )

    # Main title and information
    st.title("Peek-a-Chat: WhatsApp Read More Generator")

    st.info(
        "Welcome to Peek-a-Chat! Create engaging WhatsApp messages with a 'Read More' feature. "
        "Hide the second part of your message until the user clicks 'Read More.'"
    )

    # User input fields
    part1 = st.text_input("Enter the visible part of your message:").strip()
    part2 = st.text_input("Enter the hidden part of your message:").strip()

    # Button to generate and copy to clipboard
    if st.button("Generate and Copy to Clipboard"):
        # Check if both inputs are provided
        if not part1 or not part2:
            st.warning("Please enter both the visible and hidden parts of your message.")
        else:
            # Calculate the filler to reach a total length of 1000 characters
            filler = (1000 - len(part2)) * "‎" + " "
            create_text_clipboard(part1, part2, filler)
            st.success("Message copied to clipboard successfully")

    # Footer
    st.markdown(
        """
        ---
        Made with ❤️ by [Anas Khan](https://github.com/anxkhn)
        """
    )
    st.markdown(
        f"**GitHub Repository:** [github.com/anxkhn/Peek-a-Chat](https://github.com/anxkhn/Peek-a-Chat)"
    )

if __name__ == "__main__":
    main()
