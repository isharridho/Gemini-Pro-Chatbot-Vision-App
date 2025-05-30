# Gemini Pro Chatbot & Vision App

This project demonstrates how to build an end-to-end chatbot and image analysis application using Google's Gemini Pro (Generative AI) models with [Streamlit](https://streamlit.io/).

## Features

- **Text Chatbot:** Ask questions and get responses from Gemini Pro.
- **Vision Chatbot:** Upload an image and ask questions about it, or get a detailed description.
- **Token Usage:** The chatbot displays token usage for each response.
- **Streamlit UI:** Simple, interactive web interface.

## Project Structure

```
.
├── .env
├── app.py          # Text-based chatbot
├── vission.py      # Vision (image) chatbot
├── requirements.txt
```

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   - Create a `.env` file in the project root:
     ```
     GOOGLE_API_KEY="your-google-api-key"
     ```

4. **Run the apps**

   - For the text chatbot:
     ```sh
     streamlit run app.py
     ```
   - For the vision chatbot:
     ```sh
     streamlit run vission.py
     ```

## Usage

- **Text Chatbot:** Enter your question and click "Submit" to get a response from Gemini Pro.
- **Vision Chatbot:** Upload an image, enter a question (or leave blank for a description), and click "Submit" to get a response.

## Requirements

See [requirements.txt](requirements.txt).

## Credits

Made with ❤️ by [Isharridho](https://Linkedin.com/in/isharridho)

## License

This project is for educational purposes.
