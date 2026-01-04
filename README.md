# ✨ AI-Powered Quiz Generator ✨

This Flask-based web application allows users to generate multiple-choice quizzes on any given topic with varying difficulty levels, powered by the Gemini AI. The application features a clean, professional, and responsive user interface.

## 🚀 Features

- **Dynamic Quiz Generation**: Generate quizzes on a wide range of topics using the Gemini AI.
- **Difficulty Levels**: Choose between Easy, Medium, and Hard difficulty levels for your quizzes.
- **Interactive UI**: A modern and user-friendly interface for generating and taking quizzes.
- **Real-time Feedback**: Get immediate feedback on your answers and a final score.
- **Loading Indicator**: A visually appealing loading GIF is displayed while the quiz is being generated.

## 🎨 Color Palette

The UI is designed using a vibrant and appealing color palette:

- **Dark Purple**: `#3B0270` (rgb(59, 2, 112))
- **Bright Purple**: `#6F00FF` (rgb(111, 0, 255))
- **Light Purple**: `#E9B3FB` (rgb(233, 179, 251))
- **Very Light Pink/Off-white**: `#FFF1F1` (rgb(255, 241, 241))

## ⚙️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- A Google Cloud Project with the Gemini API enabled.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Ai_powered_Quiz.git
cd Ai_powered_Quiz
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
./venv/Scripts/activate # On Windows
source venv/bin/activate # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

_(If `requirements.txt` does not exist, you can create it with `pip freeze > requirements.txt` after installing Flask and Requests)_

### 4. Configure your Gemini API Key

Replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key in `app.py`:

```python
# app.py
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY" # ⚡ Replace with your Gemini key (created in Google Cloud)
```

### 5. Run the application

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## 🎮 Usage

1.  **Generate Quiz**:
    - Navigate to the homepage (`http://127.0.0.1:5000/`).
    - Enter a topic for your quiz in the input field.
    - Select the desired difficulty level (Easy, Medium, Hard) from the dropdown.
    - Click "Generate Quiz".
    - A loading indicator will appear while the Gemini AI generates your questions.
2.  **Take Quiz**:
    - Once the quiz is generated, select your answers for each question.
    - Click "Submit Quiz".
3.  **View Results**:
    - The result page will display your score and show which questions you answered correctly or incorrectly, along with the correct answers.
    - You can click "Retake Quiz" to go back to the homepage and generate a new quiz.
