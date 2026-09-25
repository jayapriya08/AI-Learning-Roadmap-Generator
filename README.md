# AI-Learning-Roadmap-Generator

An AI-powered learning roadmap application that generates personalized learning paths based on a learner's career goal, current skill level, existing skills, available study time, and learning duration.

# Project Overview

The AI Learning Roadmap Generator helps learners create structured learning plans for their desired career path.

The application uses a curated knowledge base with Retrieval-Augmented Generation (RAG) concepts to identify relevant learning areas and generates a month-by-month roadmap with topics, skills, projects, and expected outcomes.

# Objectives

- Generate personalized learning roadmaps
- Consider the learner's current skill level
- Use existing skills to personalize the roadmap
- Consider available study time
- Provide structured monthly learning plans
- Recommend practical projects
- Use knowledge-base retrieval to provide relevant learning areas
- Handle unsupported career topics without claiming information is available

# Features

- Career goal based roadmap generation
- Beginner, Intermediate and Advanced levels
- Personalized learning duration
- Monthly learning phases
- Topics to study
- Skills to develop
- Practical projects
- Expected learning outcomes
- Knowledge-base retrieval using RAG
- Unknown-topic detection
- Interactive Gradio interface

# Technologies Used

- Python
- Gradio
- Sentence Transformers
- FAISS
- NumPy
- Retrieval-Augmented Generation (RAG)

# RAG Implementation

The project uses a small curated knowledge base containing information about:

- Data Analysis
- SQL
- Machine Learning
- Data Visualization
- Deep Learning
- Career Preparation

Sentence Transformers are used to convert the knowledge-base content into embeddings.

FAISS is used as the vector database for similarity-based retrieval.

The system retrieves relevant topics based on the user's career goal.

If no sufficiently relevant information is found, the application displays:

> Information not found in the knowledge base.

# Example Career Goals

The application currently includes career-specific roadmaps for:

- Data Analyst
- Data Scientist
- Machine Learning Engineer

Other career goals receive a generic learning roadmap.

# User Inputs

The application accepts:

1. Career Goal
2. Current Level
3. Current Skills
4. Available Study Time
5. Learning Duration

Example:

```text
Career Goal: Machine Learning Engineer
Current Level: Beginner
Current Skills: Python
Available Study Time: 3 hours per day
Learning Duration: 6 months
# Example Output

For a Machine Learning Engineer with beginner-level knowledge of Python and 3 hours of study time per day, the application generates a structured six-month roadmap.

The roadmap includes:

- Programming and Data Foundations
- Machine Learning
- Machine Learning Projects
- Deep Learning
- ML Deployment and MLOps
- ML Engineer Portfolio and Interviews

Each month contains:

- Topics
- Skills
- Project
- Expected Outcome

# System Architecture

```text
User Input
    ↓
Gradio Interface
    ↓
Career Goal Query
    ↓
Sentence Transformer Embeddings
    ↓
FAISS Similarity Search
    ↓
Knowledge Base
    ↓
Career-Specific Roadmap Generator
    ↓
Personalized Learning Roadmap

# Installation

# 1. Clone the repository

Open Command Prompt or Terminal and run:

```bash
git clone https://github.com/jayapriya08/AI-Learning-Roadmap-Generator.git
