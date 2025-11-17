.PHONY: format lint test clean fix check help

# Format code
format:
	black src/ tests/
	ruff check src/ tests/ --fix

# Check code quality (without modifying)
lint:
	black --check src/ tests/
	ruff check src/ tests/
	flake8 src/ tests/

# Run tests
test:
	python -m pytest -v

# Complete check (format + lint + test)
check: format lint test

# Clean cache files
clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache .ruff_cache
	rm -rf build/ dist/ *.egg-info src/*.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# Auto-fix all issues
fix: format
	@echo "✅ Code formatted and fixed!"

# Show help
help:
	@echo "Available commands:"
	@echo "  make format  - Format code with Black and Ruff"
	@echo "  make lint    - Check code quality"
	@echo "  make test    - Run tests"
	@echo "  make check   - Run all checks"
	@echo "  make fix     - Auto-fix all issues"
	@echo "  make clean   - Remove cache files"
