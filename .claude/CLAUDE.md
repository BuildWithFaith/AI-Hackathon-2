# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a 5-phase hackathon project called "The Evolution of Todo" designed to take a simple console application and evolve it into a sophisticated, cloud-native AI system. The project emphasizes spec-driven development using Claude Code and Spec-Kit Plus.

## Project Phases

### Phase I (0-20%) - CLI Console App
- **Stack**: Python, Claude Code, Spec-Kit Plus
- **Goal**: Pure console-based Todo system (no DB, no web)
- **Features**: In-memory todo engine with create, update, delete, list, and mark complete functionality

### Phase II (20-40%) - Full-Stack Web App
- **Stack**: Next.js, FastAPI, SQLModel, Neon DB
- **Goal**: Convert CLI system to web app with persistent storage
- **Features**: REST API, authentication, responsive UI

### Phase III (40-60%) - AI Chatbot System
- **Stack**: OpenAI ChatKit, OpenAI Agents SDK, Official MCP SDK
- **Goal**: Natural language processing for todo management
- **Features**: AI-powered conversational interface

### Phase IV (60-80%) - Local Kubernetes Deployment
- **Stack**: Docker, Minikube, Helm, kubectl-ai, kagent
- **Goal**: Containerized microservices on local K8s
- **Features**: Kubernetes deployment with monitoring

### Phase V (80-100%) - Advanced Cloud Deployment
- **Stack**: Kafka, Dapr, DigitalOcean DOKS
- **Goal**: Production-level distributed system
- **Features**: Event-driven architecture, cloud deployment

## Development Workflow

This project follows a strict Spec-Driven Development approach:
1. Write specification files in the `/specs` directory
2. Use Claude Code to generate implementations based on specs
3. Validate spec coverage before moving to next phase

## Key Technologies

- **Frontend**: Next.js 16+, React, OpenAI ChatKit
- **Backend**: Python FastAPI, SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens
- **AI/ML**: OpenAI Agents SDK, MCP (Model Context Protocol)
- **Containerization**: Docker, Docker AI Agent (Gordon)
- **Orchestration**: Kubernetes, Minikube, Helm
- **Messaging**: Kafka, Dapr
- **DevOps**: Claude Code, Spec-Kit Plus

## Project Structure

Current structure:
- `README.md` - Main project specification document
- `CLAUDE.md` - Claude Code instructions (this file)
- `/specs` - Specification files organized by feature/type
- `/frontend` - Next.js application (Phase II+)
- `/backend` - FastAPI application (Phase II+)
- `/src` - Python source code (Phase I)

## API Endpoints (Phase II+)

The REST API follows these patterns:
- GET `/api/{user_id}/tasks` - List all tasks
- POST `/api/{user_id}/tasks` - Create a new task
- GET `/api/{user_id}/tasks/{id}` - Get task details
- PUT `/api/{user_id}/tasks/{id}` - Update a task
- DELETE `/api/{user_id}/tasks/{id}` - Delete a task
- PATCH `/api/{user_id}/tasks/{id}/complete` - Toggle completion

## MCP Tools (Phase III+)

The AI chatbot uses MCP tools for task operations:
- `add_task` - Create new task
- `list_tasks` - Retrieve tasks
- `complete_task` - Mark task as complete
- `delete_task` - Remove task
- `update_task` - Modify task details

## Commands

### Phase I (CLI App)
- Python project setup with virtual environment
- In-memory todo engine implementation
- Interactive CLI interface

### Phase II (Full-Stack)
- Frontend: `cd frontend && npm run dev`
- Backend: `cd backend && uvicorn main:app --reload`
- Database: Neon PostgreSQL connection

### Phase III (AI Chatbot)
- MCP server for AI tools
- OpenAI Agents SDK integration
- Conversational interface

### Phase IV (Kubernetes)
- Docker containerization
- Minikube local deployment
- Helm chart deployment

### Phase V (Cloud)
- Kafka event-driven architecture
- Dapr distributed services
- DigitalOcean Kubernetes deployment

## Important Notes

- No manual coding is allowed - everything must be generated via Claude Code using spec-driven development
- Each phase builds on the previous phase
- Specifications must be written before implementation
- JWT tokens are used for authentication between Next.js frontend and FastAPI backend
- The project uses a monorepo structure with organized spec files

**Start using slash commands with your AI agent:**

1. /sp.constitution - Establish project principles
2. /sp.specify - Create baseline specification    
3. /sp.plan - Create implementation plan          
4. /sp.tasks - Generate actionable tasks          
5. /sp.implement - Execute implementation  