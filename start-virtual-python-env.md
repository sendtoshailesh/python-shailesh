# Python Virtual Environment Guide

## Setting Up a Python Virtual Environment

### Prerequisites
- Python installed on your system

### Step-by-Step Instructions

1. **Check Python Installation**
   ```bash
   python --version
   ```

2. **Create a Virtual Environment**
   ```bash
   # Navigate to your project directory
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   ```bash
   # On macOS
   source venv/bin/activate
   
   # On Windows
   # venv\Scripts\activate
   ```

4. **Install Packages**
   ```bash
   pip install package_name
   ```

5. **Track Dependencies**
   ```bash
   pip freeze > requirements.txt
   ```

6. **Deactivate the Virtual Environment**
   ```bash
   deactivate
   ```

## Recommended Packages for SQL NLP Project

For your SQL NLP application, consider installing:

```bash
pip install boto3 pandas numpy requests
```

## Benefits of Virtual Environments

- Isolates project dependencies
- Prevents conflicts between projects
- Makes project setup reproducible
- Simplifies dependency management
- Enables clean testing environments
