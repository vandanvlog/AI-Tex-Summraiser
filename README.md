# AI-Tex-Summraiser 


AI Text Summariser
This is an AI-based text summarization project built using the Transformers library. It allows users to input long-form text and receive a concise summary using a fine-tuned transformer model.

Overview
This project demonstrates the implementation of a modern text summarization pipeline using Hugging Face Transformers. It includes data preprocessing, model training, evaluation, and deployment via a FastAPI web server. The project is structured for maintainability and cloud deployment (e.g., AWS).

Technologies Used
Programming Language: Python 3.8

Libraries & Frameworks:

Transformers (HuggingFace)

Datasets (HuggingFace)

PyTorch

FastAPI

Uvicorn

nltk

pandas

tqdm

matplotlib

Tools:

Docker (for containerization)

AWS ECR (for deployment)

SentencePiece (for tokenization)

Jinja2, PyYAML (for configuration)

Operating System: Linux (Docker Image: python:3.8-slim-buster)

Dataset
Source: CNN/DailyMail Dataset via Hugging Face Datasets

Description: Contains news articles with human-written summaries

Size: 287,000+ examples

Use: Used for supervised training of the summarization model

Model
Base Model: t5-small (from Hugging Face)

Task: Text summarization

Method:

Data tokenization using T5Tokenizer

Fine-tuned using PyTorch and Hugging Face Trainer API

Evaluated using ROUGE and BLEU scores