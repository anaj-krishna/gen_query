import os
import json
import google.generativeai as genai
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv

# Load API Key and configure
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# MongoDB Connection
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["studentDB"]
collection = db["students"]

# Function to Convert Prompt to Query
def prompt_to_query(prompt):
    try:
        # Use gemini-1.5-flash model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        system_prompt = """
        You are a MongoDB query generator. Convert natural language prompts to MongoDB query JSON.
        Return ONLY the query JSON without any explanation or markdown.
        Example: For "Find all students with grade A", return {"grade": "A"}
        """
        
        response = model.generate_content([system_prompt, f"Convert this prompt into a MongoDB query JSON: {prompt}"])
        
        # Clean and parse the response
        query_text = response.text.strip()
        if query_text.startswith("```") and query_text.endswith("```"):
            query_text = query_text[3:-3].strip()
        if query_text.startswith("```json") and query_text.endswith("```"):
            query_text = query_text[7:-3].strip()
            
        return json.loads(query_text), None
    except Exception as e:
        return None, f"Error: {str(e)}"

# Streamlit Web App
st.title("🔥 Prompt to MongoDB Query Generator")
user_prompt = st.text_input("Enter your prompt (e.g., 'Find all students with grade A')")

if st.button("Generate Query"):
    if user_prompt:
        with st.spinner("Generating query..."):
            query_dict, error = prompt_to_query(user_prompt)
            
            if error:
                st.error(error)
            else:
                st.subheader("Generated MongoDB Query:")
                st.code(json.dumps(query_dict, indent=2), language='json')
                
                try:
                    # Execute the query safely
                    st.subheader("Query Results:")
                    results = list(collection.find(query_dict).limit(10))
                    
                    if results:
                        for doc in results:
                            if '_id' in doc:
                                doc['_id'] = str(doc['_id'])
                            st.json(doc)
                    else:
                        st.info("No matching documents found")
                except Exception as e:
                    st.error(f"Error executing query: {str(e)}")
    else:
        st.warning("Please enter your prompt first")

# Example prompts in sidebar
st.sidebar.header("Example Prompts")
examples = [
    "Find all students named John",
    "Get students with grade above B",
    "Find students in Computer Science department",
    "List students who scored above 90 in Math"
]
for example in examples:
    if st.sidebar.button(example):
        st.session_state.user_prompt = example