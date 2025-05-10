# Agentic-Rag

# **Agentic RAG:** The Intelligent Product Assistant Chatbot


Agentic RAG is your smart, interactive assistant that combines the power of AI and advanced retrieval systems to provide users with instant access to product information, order status updates, and accurate answers to frequently asked questions, all using Retrieval-Augmented Generation (RAG) technology.
---

## 📋 Overview

Welcome to Agentic RAG, where AI meets productivity! This project creates an intelligent chatbot built on Streamlit and powered by the LangFlow API. It enables users to seamlessly interact with a smart assistant that can look up products, track orders, and answer a variety of customer inquiries by pulling the most relevant data from a knowledge base of products and orders.

This project is designed to enhance user experience by blending real-time data retrieval with AI-powered conversations, allowing users to find information quickly and accurately.

---

## ✨Key Features

- Interactive Chat Interface – A user-friendly interface built on Streamlit for easy interaction with the assistant.

- Product Lookup – Retrieve detailed information about products based on their ID or name.

- Order Tracking – Easily track the status of your orders in real-time, providing updates on delivery or fulfillment.

- FAQ Answering – The assistant answers commonly asked questions about shipping, returns, and more.

- AI-Powered Responses – Uses Retrieval-Augmented Generation (RAG) to provide accurate and contextually aware answers to user queries.

---

**The technology stack behind Agentic RAG ensures a fast, scalable, and secure environment for your chatbot:**

- Built with Streamlit to create an easy-to-use and interactive web application.

- Powered by the LangFlow API to generate AI-based responses and perform data retrieval.

- Utilizes CSV files (such as products.csv and orders.csv) to store product and order information.

- Secured with API tokens stored in environment variables for added safety.tokens  

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.12+
- Get your token to interact with the LangFlow API.

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

The heart of this project is the LangFlow API, which facilitates intelligent responses by integrating data retrieval with generative AI.

- The API call is configured within the run_flow function in app.py, which processes the user's query, retrieves relevant data from the CSV files, and generates accurate responses using the LangFlow service.

---

###**Usage Examples**
To help you get started, here are a few example queries that the chatbot can handle:

- "Tell me about product 201" – Retrieves details like the product name, description, and other features.

- "What’s the status of order 1002?" – Provides real-time order status and tracking updates.

- "How do I return an item?" – Shares the return policy or steps for returning a product.
