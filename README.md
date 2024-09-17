# Fine-tuning Large Language Models for SQL Query Generation

## Overview
This project focuses on fine-tuning a pre-trained LLaMA 3-8B model to generate SQL queries from natural language inputs. This was my first attempt at fine-tuning an LLM, and I used **QLoRA with PEFT** (Parameter-Efficient Fine-Tuning) to adapt the model for the task. 

## Motivation
As I am taking an SQL course thought it would be relevant and fun to see how it performs at learning compared to me. Overall this project was an opportunity to strengthen my understanding of SQL while gaining hands-on experience with LLM fine-tuning.

## Approach

### 1. Dataset Selection
I selected **Spider 1.0**, a complex cross-domain dataset designed for text-to-SQL generation tasks:
- **10,181** questions covering over **200** databases.
- SQL queries ranging from simple to highly complex, making it ideal for fine-tuning.

### 2. Data Preprocessing
- **Tokenization** and sequence length management for both natural language and SQL queries.
- **Schema Linking** to improve model understanding of database context.
- **Sequence Length Management**: Managed the input/output sequence length to ensure optimal model performance.

### 3. Fine-tuning (QLoRA with PEFT)
I applied **QLoRA with PEFT** to fine-tune the LLaMA 3-8B model. This method is designed for efficient fine-tuning by freezing most of the model’s parameters and only training a small subset.
- Experimented with various hyperparameters (batch size, learning rate).
- Implemented regularization techniques like dropout to combat overfitting.

### 4. Challenges
- **Performance Issues**: Despite fine-tuning, the model underperformed compared to the initial 16-bit version, indicating overfitting and dataset challenges.
- **SQL Complexity**: The model struggled with complex queries and database schema alignment.

## Key Learnings
- **First Fine-tuning Experience**: Gained a solid understanding of model adaptation using QLoRA with PEFT.
- **Error Analysis**: Learned to identify common pitfalls and performance bottlenecks in fine-tuning.
