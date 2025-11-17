# SagittalBrain

[![Tests](https://github.com/YOUR_USERNAME/sagittal_average/actions/workflows/pytest.yml/badge.svg)](https://github.com/YOUR_USERNAME/sagittal_average/actions/workflows/pytest.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

A Python library for calculating averages through sagittal-horizontal planes in brain imaging data.

## Description

SagittalBrain processes brain imaging data by calculating the average intensity for each sagittal-horizontal plane. The input data should be organized with coronal planes as columns and sagittal/horizontal plane intersections as rows.

## Features

- Calculate row-wise averages from CSV brain imaging data
- Command-line interface for easy batch processing
- Flexible input/output file specification
- Well-tested and documented

## Installation

### From source (development mode)
```bash
git clone https://github.com/YOUR_USERNAME/sagittal_average.git
cd sagittal_average
pip install -e .
```

### Requirements

- Python >= 3.10
- NumPy >= 1.20.0

## Usage

### As a command-line tool
```bash
# Basic usage
sagittal_average_run brain_sample.csv

# Specify output file
sagittal_average_run brain_sample.csv -o brain_average.csv

# Get help
sagittal_average_run --help
```

### As a Python library
```python
from sagittal_brain import run_averages

# Process a file
run_averages('brain_sample.csv', 'brain_average.csv')
```

## Input Format

The input CSV file should contain:
- Rows: intersections of sagittal/horizontal planes
- Columns: coronal planes
- Values: intensity measurements (integers or floats)

Example:
```
0,0,0,1
0,0,0,1
1,1,1,2
```

## Output Format

The output CSV file contains:
- One value per row from the input
- Each value is the average across that row

Example output for above input:
```
0.3
0.3
1.3
```

## Development

### Running tests
```bash
# Install development dependencies
pip install pytest

# Run tests
python -m pytest -v
```

### Project structure
```
sagittal_average/
├── src/
│   └── sagittal_brain/
│       ├── __init__.py
│       ├── sagittal_brain.py
│       └── command.py
├── tests/
│   └── test_sagittal_brain.py
├── pyproject.toml
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this software in your research, please cite it as described in [CITATION.cff](CITATION.cff).

## Authors

- Your Name (@your_github_username)

## Acknowledgments

- Developed as part of COMP0233 coursework at UCL
- Thanks to the course instructors and teaching assistants