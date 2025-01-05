# Generative AI Workshop Series - LangChain Guide

A practical introduction to building AI applications using LangChain and Large Language Models (LLMs). This repository contains the code examples and notebooks demonstrated during the Generative AI workshop series at GDG On Campus EMSI Casablanca.

## Overview

This repository serves as a starting point for learning how to build AI applications using LangChain. It follows a hands-on approach with practical examples and is designed to be beginner-friendly while using the latest LangChain version.

## Key Features

This repo takes a unique approach focusing on:
- Latest LangChain version implementations
- Practical, hands-on examples
- Beginner-friendly explanations
- Step-by-step building of AI applications

## Who is it for?
Perfect for students and developers looking to get started with:
- LangChain framework
- Large Language Models (LLMs)
- Prompt engineering
- Building AI-powered applications

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (not free, requires payment) otherwise use Groq (free tier!!)
- Basic understanding of Python programming

## Getting Started

1. Clone this repository
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Create a `.env` file in the root directory and add your OpenAI API key. You can use any LLM, both local and API provided ones:
```
OPENAI_API_KEY=your_api_key_here
```


## Project Structure

- `1_intro_concepts/`: Contains Jupyter notebooks with basic concepts
  - Basic implementation
  - Alternative chat models
  - Conversation handling
  - Memory management
  - Example application in Jupyter notebook
  - Example application with Streamlit

## Running the Examples

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to the `1_intro_concepts` directory and open the desired notebook

## Resources
- [LangChain Master Class For Beginners 2024, by @codewithbrandon](https://www.youtube.com/watch?v=yF9kGESAi3M)
- [Generative AI For Beginners, by Microsoft](https://microsoft.github.io/generative-ai-for-beginners/#/)

## About the Author

**Wahib** - AI Lead at GDG On Campus EMSI Casablanca
- [GDG Profile](https://gdg.community.dev/u/mz9b9h/)
- [GDG On Campus EMSI Casablanca](https://gdg.community.dev/gdg-on-campus-ecole-marocaine-des-sciences-de-lingenieur-casablanca-morocco/)


## Documentation

- [LangChain Documentation](https://python.langchain.com/docs/introduction/)
- [OpenAI Integration Documentation](https://python.langchain.com/docs/integrations/chat/openai/)
- [Alternative Chat Models](https://python.langchain.com/docs/integrations/chat/)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

Created with 🫶️ by GDG On Campus EMSI Casablanca