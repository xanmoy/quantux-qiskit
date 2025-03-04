#!/bin/bash

# Project setup script for Quantum Computing Development

# Ensure the script uses bash
#! /usr/bin/env bash

# Project directory and virtual environment name
PROJECT_DIR="$(pwd)"
VENV_NAME="quantum_env"

# Check if virtual environment already exists
if [ ! -d "$VENV_NAME" ]; then
    # Create virtual environment
    python3 -m venv "$VENV_NAME"
fi

# Path to the virtual environment's pip
VENV_PIP="$PROJECT_DIR/$VENV_NAME/bin/pip"

# Activate virtual environment (using . instead of source for POSIX compatibility)
. "$PROJECT_DIR/$VENV_NAME/bin/activate"

# Upgrade pip
"$VENV_PIP" install --upgrade pip

# Install Qiskit and related libraries
"$VENV_PIP" install qiskit[visualization]
"$VENV_PIP" install numpy matplotlib

# Optional: Save requirements
"$VENV_PIP" freeze > requirements.txt

echo "Virtual environment setup complete!"
echo "Activate with: source $VENV_NAME/bin/activate"
echo "Deactivate with: deactivate"