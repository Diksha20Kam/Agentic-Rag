# Agentic-Rag

# **Agentic RAG:** A Smart Chatbot for Your Product Assistant

A smart, interactive chat assistant that helps users find information about products, track orders, and answer FAQs using Retrieval-Augmented Generation (RAG).

---

## 📋 Overview

This project implements a **Streamlit-based chat interface** that connects to a **LangFlow API** to provide intelligent responses about products and orders. The assistant uses RAG to retrieve relevant information from a knowledge base of products and orders.

---

## ✨ Features

- 💬 Interactive chat interface  
- 🔍 Product information lookup  
- 📦 Order status tracking  
- ❓ FAQ answering capabilities  
- 🤖 AI-powered responses using RAG  

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit  
- **Backend**: LangFlow API  
- **Data**: CSV files for products and orders  
- **Authentication**: Environment variables for API tokens  

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.12+
- LangFlow API access token

### 🔧 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/ai-product-assistant.git
cd ai-product-assistant
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Create a .env file with your API token:**

TOKEN=your_langflow_api_token

**Running the Application**:

streamlit run app.py

## 📊 Data Sources

The assistant uses two main data sources:
- **`products.csv`**: Contains product information (ID, name, description)
- **`orders.csv`**: Contains order information (order number, customer details, status)

---

## 🔄 API Integration

The application connects to a **LangFlow API** endpoint to process user queries and generate responses. The API call is configured in the `run_flow` function in `streamlit_ui.py`.

---

## 🧪 Testing

You can test the API connection using the `api_test.py` script:

```bash
python api_test.py
