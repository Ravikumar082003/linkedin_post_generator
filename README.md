# LinkedIn Post Generator

A **LinkedIn Post Generator** built using **Streamlit** and **LangChain** to help users create professional, engaging, and tone-specific LinkedIn posts effortlessly. This tool utilizes a preloaded dataset of examples for fine-tuning the generation process and ensures the output aligns with the user's preferences.

---

## Features

- Generate LinkedIn posts based on user-provided content and preferences.
- Customizable options for:
  - **Length**: Short, Medium, Long.
  - **Language**: English, Hinglish (Hindi-English mix, but the output remains in English).
  - **Tone**: Formal, Informal, Professional, Motivational, Friendly.
  - **Style**: Inspirational, Informative, Question-based.
- Feedback loop for improving post quality.
- Uses preloaded examples for generating contextual outputs.

---

## Technology Stack

- **Python**
- **Streamlit**: For building the web-based user interface.
- **LangChain**: For seamless integration with the ChatGroq API.
- **Pandas**: For data manipulation and preprocessing.
- **dotenv**: For managing environment variables securely.

---

## Project Structure

```plaintext
.
├── data/
│   └── processed_posts.json     # Preloaded examples for generating posts
├── post_generator.py            # Core logic for generating posts
├── main.py                      # Streamlit-based application
├── .env                         # Environment variables (API Key)
└── README.md                    # Documentation
```

---

## Setup Instructions

### Prerequisites

1. **Python 3.8 or higher.**
2. A valid ChatGroq API key.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate      # On Linux/Mac
   env\Scripts\activate         # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your ChatGroq API key to the `.env` file:**

   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Ensure the `processed_posts.json` file is located in the `data/` directory.**

---

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run main.py
   ```

2. **Open the provided URL** (e.g., http://localhost:8501) in your web browser.
3. **Select your preferences:**
   - **Topic:** From the dropdown list of tags.
   - **Length:** Short, Medium, or Long.
   - **Language:** English or Hinglish.
   - **Tone:** Formal, Informal, etc.
   - **Style:** Inspirational, Informative, etc.
4. **Enter the content** you want to revise or use for the post.
5. **Click “Generate Post”** to get the output.
6. **Provide feedback** (“Yes” or “No”) to improve the generated post.

---

## Streamlit

![image](https://github.com/user-attachments/assets/33b2ee8a-f9bf-4a59-b145-9f9e8cff2dc8)
![image](https://github.com/user-attachments/assets/dd560d70-57e6-40ac-8e31-2fd7f631b782)

---
