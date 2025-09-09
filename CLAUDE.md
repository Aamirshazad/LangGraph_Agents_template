# Agents in this Repository

## Overview

This repository demonstrates building agents using LangGraph, focusing on an email assistant that can:
- Triage incoming emails
- Draft appropriate responses
- Execute actions (calendar scheduling, etc.)
- Incorporate human feedback
- Learn from past interactions

## Environment Setup

**Recommended: Using uv (faster and more reliable)**

```bash
# Install uv if you haven't already
pip install uv

# Install the package with development dependencies
uv sync --extra dev
```

 # Add new dependencies 
 ```bash
 uv add -U <package_name>
 ```

The package is installed as `interrupt_workshop` with import name `email_assistant`, allowing you to import from anywhere with `from email_assistant import ...`

## Agent Implementations

### Scripts 

The repository contains several implementations with increasing complexity in `src/email_assistant`:


2. **Basic  Assistant** (`email_assistant.py`)
   - Core email triage and response functionality

### Notebooks

Each aspect of the agent is explained in dedicated notebooks:
- `notebooks/agent.ipynb` - Basic agent implementation
## Running Tests

### Testing Scripts

Test to ensure all implementations work:

```bash
# Test all implementations
python tests/run_all_tests.py --all
```

(Note: This will leave out the Gmail implementation)

### Testing Notebooks

Test all notebooks to ensure they run without errors:

```bash
# Run all notebook tests directly
python tests/test_notebooks.py
```

