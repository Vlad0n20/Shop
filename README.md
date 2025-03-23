# Shop Project

## Pre-commit Setup

This project uses pre-commit hooks to ensure code quality and consistency. The hooks will:
- Format code with Black and isort
- Check for syntax errors with Flake8
- Enforce code style and documentation standards

### Setting up pre-commit hooks

1. Run the setup script:
```
./setup_pre_commit.sh
```

Or manually:
```
pip install pre-commit
pre-commit install
```

2. The hooks will now run automatically on every commit. You can also run them manually:
```
pre-commit run --all-files  # Run all hooks on all files
pre-commit run              # Run only on staged files
```

3. If you want to temporarily bypass hooks when committing:
```
git commit -m "message" --no-verify
```

### Pre-commit Hook Details

- **Black**: Formats Python code
- **isort**: Sorts imports
- **Flake8**: Checks for syntax errors and enforces code style
- **pre-commit-hooks**: Enforces basic file hygiene (trailing whitespace, file endings)

The configuration is in `.pre-commit-config.yaml` and additional settings in `setup.cfg`.

## CI/CD with GitHub Actions

This project uses GitHub Actions for continuous integration and deployment. The workflow is triggered on:
- Push to the main branch
- Pull requests to the main branch

### CI Pipeline

The CI pipeline does the following:
1. Sets up Python 3.13.2
2. Installs Poetry dependency manager
3. Sets up dependency caching for faster builds
4. Installs project dependencies using Poetry
5. Runs pre-commit hooks on all files
6. Applies database migrations
7. Runs Django tests

### CD Pipeline

The CD pipeline is triggered only when changes are pushed to the main branch and all tests pass. Currently, it's set up as a placeholder, but you can customize it for your deployment needs.

### Setting up Deployment

To set up deployment:
1. Uncomment the deployment steps in `.github/workflows/ci-cd.yml`
2. Add your SSH private key to GitHub Secrets as `SSH_PRIVATE_KEY`
3. Customize the deployment commands to match your server configuration 