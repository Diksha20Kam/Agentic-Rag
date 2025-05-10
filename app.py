import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


APPLICATION_TOKEN = os.environ.get("AUTH_TOKEN")


def run_flow(message: str) -> dict:
    api_url = f"https://api.langflow.astra.datastax.com/lf/ad303f2f-59d8-428a-acec-4c2a509c6f1b/api/v1/run/ee10b65d-db45-4098-b89e-2ebf28d13c3a"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()