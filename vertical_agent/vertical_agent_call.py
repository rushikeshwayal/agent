from config import DomainIntelligenceAgent
from vertical_prompt import VerticalPrompt
from dotenv import load_dotenv
import json
import os
import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer
from database import SessionLocal
from model import DomainEmbedding
from sqlalchemy.orm import Session

load_dotenv()


# Formating user input and system input using VerticalPrompt class

vertical_prompt = VerticalPrompt()

Client_Name = "MediCare Solutions"
Client_Description = "MediCare Solutions is a global healthcare technology company providing AI-driven diagnostics and remote patient monitoring solutions. Their innovative platform helps hospitals, clinics, and healthcare providers enhance patient care, reduce costs, and streamline operations."
url = "https://www.medicare-solutions.com"

system_input = vertical_prompt.system_prompt()

user_input = vertical_prompt.user_prompt(client_name=Client_Name,client_description=Client_Description,website_url=url)

# Classify the business domain using DomainIntelligenceAgent class

# Initialize DomainIntelligenceAgent
domain_agent = DomainIntelligenceAgent()

response = domain_agent._classify_business_domain( system_input=system_input,
                                                    user_input=user_input,
                                                    model_name="google",
                                                    model_variant="gemini-1.5-flash",
                                                    verbose=True,
                                                    output_parser="json")


# Storing responce in local file 

file_path = './vertical_agent/verticalAgent_output.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        existing_data = json.load(file)

        if not isinstance(existing_data, list):
            existing_data = [existing_data]
else:
    existing_data = []

existing_data.append(response)


# Write the updated data back to the file
with open(file_path, 'w') as file:
    json.dump(existing_data, file, indent=4)


# Update the database with the domain classification

# hugging face model for convert json to embedding
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Convert text data to a single input string
text_to_embed = response["domain_name"]+" "+ response["domain_description"] + " " + " ".join(response["keywords"])+" Confidance Score By AI"+str(response["confidence_score"])

# Generate embedding using Hugging Face
embedding = model.encode(text_to_embed).tolist()

# Function to insert data into the database
def insert_data(db: Session, json_data, embedding):
    new_entry = DomainEmbedding(
        domain_name=json_data["domain_name"],
        domain_description=json_data["domain_description"],
        keywords=json_data["keywords"],
        confidence_score=json_data["confidence_score"],
        embedding=embedding
    )
    db.add(new_entry)
    db.commit()
    print("✅ Data inserted successfully!")


# Run the insertion process
if __name__ == "__main__":
    db = SessionLocal()
    insert_data(db, response, embedding)
    db.close()