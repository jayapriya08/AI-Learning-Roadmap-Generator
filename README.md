# AI-Learning-Roadmap-Generator

An AI-powered learning roadmap application that generates personalized learning paths based on a learner's career goal, current skill level, existing skills, available study time, and learning duration.

## Project Overview

The AI Learning Roadmap Generator helps learners create structured learning plans for their desired career path.

The application uses a curated knowledge base with Retrieval-Augmented Generation (RAG) concepts to identify relevant learning areas and generates a month-by-month roadmap with topics, skills, projects, and expected outcomes.

## Objectives

- Generate personalized learning roadmaps
- Consider the learner's current skill level
- Use existing skills to personalize the roadmap
- Consider available study time
- Provide structured monthly learning plans
- Recommend practical projects
- Use knowledge-base retrieval to provide relevant learning areas
- Handle unsupported career topics without claiming information is available

## Features

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

## Technologies Used

- Python
- Gradio
- Sentence Transformers
- FAISS
- NumPy
- Retrieval-Augmented Generation (RAG)

## RAG Implementation

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

## Example Career Goals

The application currently includes career-specific roadmaps for:

- Data Analyst
- Data Scientist
- Machine Learning Engineer

Other career goals receive a generic learning roadmap.

## User Inputs

The application accepts:

1. Career Goal
2. Current Level
3. Current Skills
4. Available Study Time
5. Learning Duration

### Example:

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

## System Architecture

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

## Installation

# 1. Clone the repository

Open Command Prompt or Terminal and run:

git clone https://github.com/jayapriya08/AI-Learning-Roadmap-Generator.git

2. Open the project folder
cd AI-Learning-Roadmap-Generator
3. Install the required packages
pip install -r requirements.txt
4. Run the application
python app.py

The Gradio application will start and provide a local URL in the terminal.

## Requirements

The main dependencies used in this project are:

sentence-transformers
faiss-cpu
numpy

## Testing
The application was tested using different career goals, skill levels, study times, and learning durations.

Test cases included:

1. Machine Learning Engineer – Beginner – Python – 3 hours/day – 6 months
2. Data Scientist – Intermediate – Python, SQL, Pandas, NumPy – 2 hours/day – 6 months
3. Data Analyst – Advanced – Python, SQL – 1 hour/day – 3 months
4. Unsupported career goal – Professional Chef – Beginner – Cooking – 2 hours/day – 6 months

The unsupported career test confirmed that the system can identify when relevant information is not available in the knowledge base.

## Project Links
### GitHub Repository

https://github.com/jayapriya08/AI-Learning-Roadmap-Generator

## Hugging Face Space

https://huggingface.co/spaces/Jayapriyar/AI-Learning-Roadmap-Generator

## Project Documentation

The complete project documentation is included in this repository.

## The documentation covers:

Abstract / Executive Summary
Problem Statement
Objectives
Scope
System Architecture
Tech Stack
Prompt Design
Implementation Details
RAG Details
User Interface
Testing
Results and Sample Outputs
Challenges and Fixes
Limitations
Future Improvements
Deployment Details
Conclusion
References

## Team Members
Team Member 	Contribution
[R. Jayapriya]	Project development, RAG implementation, application           integration, testing and documentation
[Alli Satyaveni]

## Future Improvements
Expand the knowledge base with more career paths
Add more learning resources and recommended courses
Integrate a larger language model for more flexible roadmap generation
Add learner progress tracking
Add user accounts and saved roadmaps
Improve deployment scalability
