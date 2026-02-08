<div align="center">

# 🦜🔗 LangChain Structured Output Experiments

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Structured%20Output-green)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-orange)
![HuggingFace](https://img.shields.io/badge/HuggingFace-LLM-yellow)
![Status](https://img.shields.io/badge/Status-Learning%20Project-blueviolet)

### Developed by **[Ghulam Muhammad]**
*Building the foundation for Agentic AI in 2026*

---
</div>

This repository documents my **hands-on learning journey with LangChain’s Structured Output feature**.
The goal is to explore **different schema enforcement techniques**—such as `TypedDict`, **JSON Schema**, and **Pydantic models**—to reliably extract structured data from Large Language Model (LLM) responses.

This is a **learning-focused but production-minded** repository, intended to demonstrate how structured outputs improve reliability, validation, and downstream processing in LLM-powered applications.

---

## 🚀 What This Repository Covers

* Using **LangChain with HuggingFace models**
* Enforcing structured responses using:

  * Python `TypedDict`
  * JSON Schema
  * Pydantic models
* Applying annotations (`Annotated`, `Literal`, `Optional`) to guide model output
* Comparing flexibility vs validation strictness across approaches
* Practical review-analysis examples (sentiment, pros/cons, themes)

---

## 🧠 Why Structured Output Matters

LLMs are probabilistic by nature. Without structure:

* Outputs may be inconsistent
* Downstream parsing becomes fragile
* Validation is difficult

Structured output ensures:

* Predictable response formats
* Strong typing and validation
* Safer integration with APIs, databases, and analytics pipelines

---

## 📂 File Overview

### 1️⃣ `1_with_structured_output_typedict.py`

Basic example using **TypedDict** to enforce a simple schema (`summary`, `sentiment`) from an LLM response.

**Concepts:**

* `TypedDict`
* `model.with_structured_output()`
* Simple schema enforcement

---

### 2️⃣ `2_with_structured_output_typedict.py`

Advanced TypedDict example using:

* `Annotated` descriptions
* `Literal` for constrained values
* `Optional` fields

Extracts:

* Key themes
* Summary
* Sentiment
* Pros & Cons
* Reviewer name

---

### 3️⃣ `json_schema.json`

A standalone **JSON Schema** example defining a simple `student` object.

Used to understand:

* Schema design
* Required vs optional fields
* JSON-based validation concepts

---

### 4️⃣ `pydantic_demo.py`

Demonstrates **Pydantic validation** without LangChain.

Covers:

* Field constraints (`gt`, `lt`)
* Default values
* Email validation
* Converting models to dict and JSON

---

### 5️⃣ `Reviews.txt`

Raw, unstructured review text used as input for structured extraction examples.

This file simulates **real-world LLM input data**.

---

### 6️⃣ `typeddict_demo.py`

A minimal Python example explaining how `TypedDict` works independently of LangChain.

Useful for understanding:

* Static typing expectations
* Differences from normal dictionaries

---

### 7️⃣ `with_structured_output_json.py`

Uses **JSON Schema directly inside LangChain** to enforce structured output.

Highlights:

* Schema-first design
* Language-agnostic validation
* Suitable for API-driven systems

---

### 8️⃣ `with_structured_output_pydantic.py`

Uses **Pydantic models** as the schema layer for LangChain structured output.

Best for:

* Strong validation
* Python-native workflows
* Production-grade pipelines

---

## 🛠️ Tech Stack

* Python 3.10+
* LangChain
* HuggingFace Inference Endpoints
* Pydantic
* dotenv

---

## ⚙️ Setup & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/imabid141/langchain-structured-output-experiments.git
   
   cd langchain-structured-output-experiments
   ```

2. Install dependencies:

   ```bash
   pip install langchain pydantic python-dotenv langchain-huggingface
   ```

3. Create a `.env` file:

   ```env
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```

4. Run any script:

   ```bash
   python with_structured_output_pydantic.py
   ```

---

## 📌 Learning Outcome

By the end of this mini-project, you’ll clearly understand:

* When to use TypedDict vs JSON Schema vs Pydantic
* How schema strictness impacts LLM behavior
* How to build safer, more reliable LLM applications

---

## 📜 License

This repository is created for **learning and experimentation purposes**.
Feel free to explore, fork, and adapt.
