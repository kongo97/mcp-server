## 🧠 MCP Agent (Dockerized)
MCP Agent is a modular system designed to orchestrate intelligent agents capable of performing complex tasks using LLMs (Large Language Models) and external tools.
This repository provides a ready-to-use Docker environment for quickly running an instance of mcp-agent, including support for local file system interaction and integration with OpenAI models.

### ✨ What it's for
Automating tasks through configurable agents

Running LLM workflows with tools like filesystem and fetch

Integrating OpenAI models in a containerized environment

Rapid experimentation with prompt augmentation and retrieval

This setup is ideal for development, testing, and deploying MCP agents in isolated and reproducible environments.

### 📦 First step
Get OPEN-AI API key and put it in docker-compose.yml environment

### 🛠️ Build Image
> docker compose build

### 🟢 Container UP
> docker compose up -d

### 🐳 Run cointainer bash
> docker exec -it mcp-server bash

### 🚀 Run examples
> python examples/simple_finder.py

### 🛑 Container DOWN
> docker compose down