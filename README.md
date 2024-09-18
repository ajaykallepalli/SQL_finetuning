# Fine-tuning Large Language Models for SQL Query Generation

## Overview
This project focuses on fine-tuning a LLaMA 3-8B completion model to generate SQL queries from natural language inputs. This was my first attempt at fine-tuning an LLM, and I used **QLoRA** to adapt the model for the task. Ultimately the model performed worse than the base model for out of sample query generation but I learnt a lot and have the future points to address in the challenges section below.

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

### 3. Fine-tuning (QLoRA)
I applied **QLoRA** to fine-tune the LLaMA 3-8B model. This method is designed for efficient fine-tuning by freezing most of the model’s parameters and only training a small subset.
- Experimented with various hyperparameters (batch size, learning rate).
- Implemented regularization techniques like dropout to combat overfitting.

### 4. Challenges
- **Memory Constraints**: I initially attempted to fine-tune a 16-bit model, but frequent crashes due to RAM limitations (particularly on an A100 in Colab) led me to switch to a 4-bit version. Also required to lower the batch size and gradient accumulation steps.
- **Performance Issues**: Despite fine-tuning, the 4-bit model underperformed compared to the initial 16-bit pre-trained model, which suggests overfitting and dataset imbalance.
- **SQL Complexity**: The model faced difficulty with complex queries and database schema alignment.

## Key Learnings
- **First Fine-tuning Experience**: This project taught me the intricacies of model adaptation using QLoRA.
- **Local Inference and Deployment**: Learned how to deploy a model from hugging face locally using Ollama and manage fine-tuning tasks using google colab to enable access to GPUs.
- **Error Analysis**: Gained experience in identifying common bottlenecks and failure modes during fine-tuning.
