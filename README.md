# Peek-a-Chat: WhatsApp Read More Generator

Peek-a-Chat is a straightforward tool that enables you to craft engaging WhatsApp messages with a 'Read More' feature. With this generator, you can cleverly hide a portion of your message, revealing it only when the user clicks 'Read More.' This tool is perfect for creating suspenseful or detailed messages within the character limit imposed by WhatsApp.


## How to Use

1. Enter the visible part of your message in the first input field.
2. Enter the hidden part of your message in the second input field.
3. Click the "Generate and Copy to Clipboard" button.

The tool calculates the required filler to reach a total length of 1000 characters and copies the resulting message to your clipboard. You can then seamlessly paste the generated message into WhatsApp.

**Note:** Ensure you enter content in both the visible and hidden parts of your message before generating.

## Technical Details

### Dependencies

- [Streamlit](https://streamlit.io/)
- [Pyperclip](https://pypi.org/project/pyperclip/)

### How It Works

The `create_text_clipboard` function concatenates the visible part (`part1`), a filler string (composed of the Unicode character U+200E, also known as the left-to-right mark or LRM), and the hidden part (`part2`) to form the final message. The use of the LRM character allows for counting characters without adding visible spaces, ensuring the message fits within the WhatsApp character limit.

### Unicode Character U+200E

The left-to-right mark (LRM) is represented as follows:

- Octal: 020016
- Decimal: 8206
- Hexadecimal: 0x200E
- HTML Entity: `&lrm;`

Including the LRM in the filler string helps maintain the character count without introducing visible spacing.

### Page Configuration

The Streamlit page is configured with a title ("Peek-a-Chat"), an icon (🔍💬), and a wide layout for an enhanced user experience.

## Getting Started

1. Clone the repository: [github.com/anxkhn/Peek-a-Chat](https://github.com/anxkhn/Peek-a-Chat)
2. Install dependencies: `pip install streamlit pyperclip`
3. Run the application: `streamlit run peek_a_chat.py`

**Update:**
Unfortunately, due to limitations with the Streamlit deployment, it is not possible to deploy with the Pyperclip dependency. However, an alternative web version written in JavaScript is available and can be accessed at [https://anxkhn.xyz/Peek-a-Chat/](https://anxkhn.xyz/Peek-a-Chat/). The Streamlit version can still be run locally.


## Author

Made with ❤️ by [Anas Khan](https://github.com/anxkhn)

## Feedback and Contributions

Feel free to open issues or contribute to the project on [GitHub](https://github.com/anxkhn/Peek-a-Chat). Your feedback and contributions are highly appreciated.

---

**Disclaimer:** This tool is not affiliated with WhatsApp. Use it responsibly and be aware of the terms of service of the platform.
