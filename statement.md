# Problem Statement

Recruiters and job seekers both spend significant time manually comparing
resumes against job descriptions to judge fit. This project builds a tool
that automatically scores how well a resume matches a given job description
using NLP techniques, and highlights which important keywords from the job
description are missing from the resume.

## Scope

- Works on plain-text resumes and job descriptions (extracted from PDF/DOCX
  or provided as text/CSV).
- Uses TF-IDF vectorization and cosine similarity to compute a match score
  between a resume and a job description.
- Identifies keyword gaps: important terms present in the job description
  but absent from the resume.
- Delivered as a command-line tool — no GUI required.
- Out of scope: contextual/semantic matching beyond TF-IDF (e.g. deep
  learning embeddings), and support for multiple languages.

## Target Users

- Job seekers who want to tailor their resume to a specific job posting.
- Recruiters or HR teams who want a quick, automated first-pass screening
  of resumes against a job description.

## High-Level Features

1. Text preprocessing: cleans and normalizes resume and job description
   text (lowercasing, stopword removal, tokenization).
2. Similarity scoring: computes a match score between a resume and a job
   description using TF-IDF + cosine similarity.
3. Keyword gap analysis: extracts top keywords from the job description
   and reports which ones are missing from the resume.
4. CLI interface: takes a resume and job description as input and prints
   the match score and missing keywords.