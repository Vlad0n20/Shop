#!/bin/bash

# Check if pre-commit is installed
if ! command -v pre-commit &> /dev/null; then
    echo "Installing pre-commit..."
    pip install pre-commit
fi

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
pre-commit install

echo "Pre-commit hooks have been set up successfully!"
echo "These hooks will run automatically on commit, but you can also run them manually:"
echo "  pre-commit run --all-files  # Run all hooks on all files"
echo "  pre-commit run              # Run only on staged files" 