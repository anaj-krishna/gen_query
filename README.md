Gen-Query 🔥🚀

Prompt-to-MongoDB Query Generator using Google Gemini LLM + MongoDB + Streamlit

Project Description 🧠💪

Gen-Query is an AI-powered web app that automatically converts natural language prompts into MongoDB queries using Google's Gemini API. This project is built with ❤️ by Techie Master Anaj Krishna — The Future AI Monk from Kochi 😏🔥.

Tech Stack 🛠️

Google Gemini LLM (Text-to-Query Conversion)

MongoDB (NoSQL Database)

Streamlit (Frontend Web App)

Python

Folder Structure 📁

Gen-Query/
│
├── app.py              # Streamlit Web App 🔥
├── query_generator.py  # Google Gemini Query Conversion API
├── db_connection.py    # MongoDB Connection
├── .env               # API Keys
├── requirements.txt    # All Dependencies
└── README.md           # Project Documentation

Installation Steps 🔥

# Clone the Repository
$ git clone https://github.com/anaj-krishna/Gen-Query.git
$ cd Gen-Query

# Create Virtual Environment
$ python -m venv venv
$ source venv/Scripts/activate (Windows)
$ source venv/bin/activate (Linux/Mac)

# Install Requirements
$ pip install -r requirements.txt

# Set API Key
Create `.env` file inside project folder and add:
GEMINI_API_KEY=your_api_key_here

# Run the App
$ streamlit run app.py

How It Works ⚙️

Enter your natural language prompt (Example: "Find all students in AI/ML course")

Click Generate Query 🔥

Gemini API converts your prompt to MongoDB Query automatically

Query will be executed in MongoDB

Results will be displayed on the screen

Example Prompts 💪

Prompt

MongoDB Query

Find all students in AI/ML

{"course": "AI/ML"}

Students above age 23

{"age": {"$gt": 23}}

Web Development Students

{"course": "Web Development"}

Students with age 22 and AI/ML

{"age": 22, "course": "AI/ML"}

