
import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# =========================
# KNOWLEDGE BASE
# =========================

knowledge_base = [
    {
        "topic": "Data Analysis",
        "content": "Data analysis involves collecting, cleaning, exploring and interpreting data. Important tools include Pandas, NumPy, Excel and data visualization libraries. Common data analysis tasks include handling missing values, removing duplicates, exploratory data analysis and identifying patterns in datasets."
    },
    {
        "topic": "SQL",
        "content": "SQL is used to work with relational databases. Important SQL topics include SELECT queries, filtering, sorting, grouping, aggregate functions, joins, subqueries and window functions. SQL is an important skill for data analysts and data scientists."
    },
    {
        "topic": "Machine Learning",
        "content": "Machine learning allows computers to learn patterns from data. Important topics include data preprocessing, feature engineering, regression, classification, clustering and model evaluation. Scikit-learn is commonly used for implementing machine learning algorithms."
    },
    {
        "topic": "Data Visualization",
        "content": "Data visualization presents information using charts, graphs and dashboards. Common tools include Matplotlib, Seaborn and Power BI. Effective visualization helps users understand patterns, trends and relationships in datasets and supports data-driven decision making."
    },
    {
        "topic": "Deep Learning",
        "content": "Deep learning is a machine learning approach based on neural networks. Important topics include neural networks, convolutional neural networks, recurrent neural networks and transfer learning. Deep learning can be applied to computer vision, natural language processing and other complex prediction tasks."
    },
    {
        "topic": "Career Preparation",
        "content": "Career preparation includes building practical projects, maintaining a GitHub portfolio, preparing a resume, practicing technical interviews and explaining project work clearly. Real-world projects help demonstrate practical skills to employers."
    }
]

# =========================
# EMBEDDING MODEL
# =========================

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [item["content"] for item in knowledge_base]

embeddings = embedding_model.encode(documents)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(embeddings)

print("Knowledge base loaded successfully!")
print("Documents:", len(documents))
print("Embedding dimension:", dimension)

# =========================
# RAG SEARCH
# =========================

def search_knowledge_base(query, top_k=2):

    query_embedding = embedding_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = faiss_index.search(
        query_embedding,
        top_k
    )

    best_distance = distances[0][0]

    if best_distance > 1.2:
        return "Information not found in the knowledge base."

    results = []

    for index in indices[0]:
        results.append({
            "topic": knowledge_base[index]["topic"],
            "content": knowledge_base[index]["content"]
        })

    return results

# =========================
# RAG TOPICS
# =========================

def get_rag_topics(career_goal):

    query = (
        f"What skills and topics should I learn "
        f"to become a {career_goal}?"
    )

    results = search_knowledge_base(query, top_k=2)

    if isinstance(results, str):
        return []

    return [result["topic"] for result in results]

# =========================
# CAREER ROADMAP CONTENT
# =========================

def get_roadmap_content(career_goal):

    goal = career_goal.lower()

    if "data analyst" in goal:

        return [
            {
                "title": "Advanced Data Analysis",
                "topics": [
                    "Advanced Pandas",
                    "Data Cleaning",
                    "Exploratory Data Analysis"
                ],
                "skills": [
                    "Data analysis",
                    "Data cleaning",
                    "Problem solving"
                ],
                "project": "Analyze a real-world sales dataset.",
                "outcome": "Able to clean and analyze real-world datasets."
            },
            {
                "title": "Data Visualization and Business Intelligence",
                "topics": [
                    "Matplotlib",
                    "Seaborn",
                    "Power BI"
                ],
                "skills": [
                    "Data visualization",
                    "Dashboard development",
                    "Business reporting"
                ],
                "project": "Build a sales performance dashboard.",
                "outcome": "Able to communicate insights using dashboards."
            },
            {
                "title": "Statistics and Portfolio Preparation",
                "topics": [
                    "Descriptive statistics",
                    "Probability",
                    "Portfolio development"
                ],
                "skills": [
                    "Statistical analysis",
                    "Data interpretation",
                    "Portfolio development"
                ],
                "project": "Create an end-to-end data analysis project.",
                "outcome": "Able to present a complete data analysis project."
            },
            {
                "title": "Advanced SQL and Analytics",
                "topics": [
                    "Joins",
                    "Subqueries",
                    "Window functions"
                ],
                "skills": [
                    "Advanced SQL",
                    "Database analysis",
                    "Query optimization"
                ],
                "project": "Build an analytics project using SQL.",
                "outcome": "Able to solve business problems using SQL."
            },
            {
                "title": "Business Intelligence Project",
                "topics": [
                    "Power BI",
                    "KPIs",
                    "Business insights"
                ],
                "skills": [
                    "BI development",
                    "Dashboard design",
                    "Business communication"
                ],
                "project": "Create a business intelligence dashboard.",
                "outcome": "Able to create professional BI reports."
            },
            {
                "title": "Portfolio and Interview Preparation",
                "topics": [
                    "GitHub portfolio",
                    "Resume preparation",
                    "Technical interviews"
                ],
                "skills": [
                    "Communication",
                    "Interview preparation",
                    "Project explanation"
                ],
                "project": "Build and publish a complete portfolio.",
                "outcome": "Ready for Data Analyst job applications."
            }
        ]

    elif "data scientist" in goal:

        return [
            {
                "title": "Statistics and Data Analysis",
                "topics": [
                    "Statistics",
                    "Pandas",
                    "Exploratory Data Analysis"
                ],
                "skills": [
                    "Statistical thinking",
                    "Data analysis",
                    "Data preprocessing"
                ],
                "project": "Perform exploratory analysis on a real-world dataset.",
                "outcome": "Able to analyze and interpret datasets."
            },
            {
                "title": "Machine Learning",
                "topics": [
                    "Regression",
                    "Classification",
                    "Model evaluation"
                ],
                "skills": [
                    "Machine learning",
                    "Feature engineering",
                    "Model evaluation"
                ],
                "project": "Build a machine learning prediction model.",
                "outcome": "Able to develop and evaluate ML models."
            },
            {
                "title": "Data Science Portfolio",
                "topics": [
                    "End-to-end projects",
                    "Data storytelling",
                    "GitHub"
                ],
                "skills": [
                    "Project development",
                    "Data storytelling",
                    "Portfolio development"
                ],
                "project": "Create a complete data science project.",
                "outcome": "Able to demonstrate practical data science skills."
            },
            {
                "title": "Advanced Machine Learning",
                "topics": [
                    "Ensemble methods",
                    "Hyperparameter tuning",
                    "Cross-validation"
                ],
                "skills": [
                    "Model optimization",
                    "Feature selection",
                    "Evaluation"
                ],
                "project": "Develop an optimized ML model.",
                "outcome": "Able to improve machine learning model performance."
            },
            {
                "title": "Advanced Analytics and Deployment",
                "topics": [
                    "Model deployment",
                    "APIs",
                    "Model monitoring"
                ],
                "skills": [
                    "Deployment",
                    "API development",
                    "Production thinking"
                ],
                "project": "Deploy a machine learning model as an API.",
                "outcome": "Able to deploy ML solutions."
            },
            {
                "title": "Data Science Portfolio and Interviews",
                "topics": [
                    "Portfolio projects",
                    "Resume preparation",
                    "Technical interviews"
                ],
                "skills": [
                    "Communication",
                    "Problem solving",
                    "Interview preparation"
                ],
                "project": "Build a professional Data Science portfolio.",
                "outcome": "Ready for Data Scientist job applications."
            }
        ]

    elif "machine learning engineer" in goal:

        return [
            {
                "title": "Programming and Data Foundations",
                "topics": [
                    "Python programming",
                    "NumPy",
                    "Pandas"
                ],
                "skills": [
                    "Python programming",
                    "Data processing",
                    "Problem solving"
                ],
                "project": "Build a data preprocessing pipeline.",
                "outcome": "Able to prepare data for ML projects."
            },
            {
                "title": "Machine Learning",
                "topics": [
                    "Regression",
                    "Classification",
                    "Clustering"
                ],
                "skills": [
                    "Machine learning",
                    "Feature engineering",
                    "Model evaluation"
                ],
                "project": "Build a machine learning prediction system.",
                "outcome": "Able to train and evaluate ML models."
            },
            {
                "title": "Machine Learning Projects",
                "topics": [
                    "End-to-end ML projects",
                    "Feature engineering",
                    "Model selection"
                ],
                "skills": [
                    "Project development",
                    "Model selection",
                    "Problem solving"
                ],
                "project": "Develop a complete ML project using a real dataset.",
                "outcome": "Able to build practical ML solutions."
            },
            {
                "title": "Deep Learning",
                "topics": [
                    "Neural networks",
                    "CNN",
                    "Transfer learning"
                ],
                "skills": [
                    "Deep learning",
                    "Neural networks",
                    "Model training"
                ],
                "project": "Build an image classification system.",
                "outcome": "Able to develop deep learning applications."
            },
            {
                "title": "ML Deployment and MLOps",
                "topics": [
                    "Model deployment",
                    "REST APIs",
                    "MLOps fundamentals"
                ],
                "skills": [
                    "Deployment",
                    "API development",
                    "Production ML"
                ],
                "project": "Deploy an ML model as a web API.",
                "outcome": "Able to deploy machine learning models."
            },
            {
                "title": "ML Engineer Portfolio and Interviews",
                "topics": [
                    "GitHub portfolio",
                    "Resume preparation",
                    "ML interviews"
                ],
                "skills": [
                    "Communication",
                    "Technical interviews",
                    "Project explanation"
                ],
                "project": "Create a complete ML engineering portfolio.",
                "outcome": "Ready for Machine Learning Engineer job applications."
            }
        ]

    else:

        return [
            {
                "title": "Programming and Foundations",
                "topics": [
                    "Programming fundamentals",
                    "Problem solving",
                    "Development tools"
                ],
                "skills": [
                    "Programming",
                    "Problem solving",
                    "Logical thinking"
                ],
                "project": "Build a beginner-friendly project.",
                "outcome": "Understand the fundamentals required for the career goal."
            },
            {
                "title": "Core Technical Skills",
                "topics": [
                    "Core concepts",
                    "Tools",
                    "Practical exercises"
                ],
                "skills": [
                    "Technical skills",
                    "Problem solving",
                    "Tool usage"
                ],
                "project": "Build a practical project.",
                "outcome": "Able to apply core technical concepts."
            },
            {
                "title": "Practical Projects",
                "topics": [
                    "Project development",
                    "Real-world datasets",
                    "Testing"
                ],
                "skills": [
                    "Project development",
                    "Testing",
                    "Debugging"
                ],
                "project": "Build a real-world project.",
                "outcome": "Able to develop practical solutions."
            },
            {
                "title": "Advanced Skills",
                "topics": [
                    "Advanced concepts",
                    "Best practices",
                    "Optimization"
                ],
                "skills": [
                    "Optimization",
                    "Advanced problem solving",
                    "Best practices"
                ],
                "project": "Improve and extend an existing project.",
                "outcome": "Able to handle more complex problems."
            },
            {
                "title": "Portfolio Development",
                "topics": [
                    "GitHub",
                    "Documentation",
                    "Project presentation"
                ],
                "skills": [
                    "Portfolio development",
                    "Documentation",
                    "Communication"
                ],
                "project": "Create a professional portfolio.",
                "outcome": "Able to demonstrate practical skills."
            },
            {
                "title": "Career Preparation",
                "topics": [
                    "Resume preparation",
                    "Technical interviews",
                    "Job preparation"
                ],
                "skills": [
                    "Interview preparation",
                    "Communication",
                    "Career planning"
                ],
                "project": "Prepare and present your final portfolio.",
                "outcome": "Ready to apply for relevant entry-level roles."
            }
        ]


# =========================
# CREATE ROADMAP
# =========================

def create_rag_personalized_roadmap(
    career_goal,
    current_level,
    current_skills,
    available_time,
    duration
):

    rag_topics = get_rag_topics(career_goal)

    roadmap_content = get_roadmap_content(career_goal)

    number_of_months = int(duration.split()[0])

    roadmap = f"""
# AI Learning Roadmap

**Career Goal:** {career_goal}

**Current Level:** {current_level}

**Current Skills:** {current_skills}

**Study Time:** {available_time}

**Duration:** {duration}

---

## Knowledge-Based Focus

"""

    if rag_topics:

        for topic in rag_topics:
            roadmap += f"- {topic}\n"

    else:

        roadmap += "- No matching information found in the knowledge base.\n"

    roadmap += "\n---\n"

    for i in range(number_of_months):

        if i < len(roadmap_content):

            data = roadmap_content[i]

        else:

            data = {
                "title": "Advanced Practice and Portfolio",
                "topics": [
                    "Advanced Project Development",
                    "Real-World Dataset Analysis",
                    "Portfolio Development",
                    "Interview Preparation"
                ],
                "skills": [
                    "Problem solving",
                    "Project development",
                    "Portfolio development"
                ],
                "project": "Build a real-world project related to your career goal.",
                "outcome": "Able to apply your skills to real-world problems."
            }

        roadmap += f"""
## Month {i + 1}: {data["title"]}

Topics:
"""

        for number, topic in enumerate(data["topics"], start=1):
            roadmap += f"{number}. {topic}\n"

        roadmap += """
Skills:
"""

        for skill in data["skills"]:
            roadmap += f"- {skill}\n"

        roadmap += f"""
Project:

{data["project"]}

Outcome:

{data["outcome"]}

---
"""

    return roadmap.strip()


# =========================
# GRADIO APP
# =========================

def roadmap_app(
    career_goal,
    current_level,
    current_skills,
    available_time,
    duration
):

    return create_rag_personalized_roadmap(
        career_goal,
        current_level,
        current_skills,
        available_time,
        duration
    )


demo = gr.Interface(
    fn=roadmap_app,
    inputs=[
        gr.Textbox(
            label="Career Goal",
            placeholder="Example: Machine Learning Engineer"
        ),
        gr.Dropdown(
            choices=[
                "Beginner",
                "Intermediate",
                "Advanced"
            ],
            label="Current Level",
            value="Beginner"
        ),
        gr.Textbox(
            label="Current Skills",
            placeholder="Example: Python, SQL"
        ),
        gr.Textbox(
            label="Available Study Time",
            placeholder="Example: 2 hours per day"
        ),
        gr.Dropdown(
            choices=[
                "3 months",
                "6 months",
                "9 months",
                "12 months"
            ],
            label="Learning Duration",
            value="6 months"
        )
    ],
    outputs=gr.Markdown(),
    title="AI Learning Roadmap Generator",
    description=(
        "Generate a personalized learning roadmap using "
        "knowledge-based retrieval and career-specific learning paths."
    )
)

demo.launch(share=True)
