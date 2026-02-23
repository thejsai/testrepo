# Test Calculator App

A simple Python calculator application for testing CI/CD pipelines.

## Features
- Basic arithmetic operations (add, subtract, multiply, divide)
- Comprehensive test suite with 5 test cases
- 100% test coverage
- Clean, simple structure perfect for CI/CD testing

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=calculator --cov-report=xml
```

## Usage

```python
from calculator import add, subtract, multiply, divide

# Addition
result = add(5, 3)  # Returns 8

# Subtraction
result = subtract(10, 4)  # Returns 6

# Multiplication
result = multiply(7, 6)  # Returns 42

# Division
result = divide(15, 3)  # Returns 5.0
```

## Project Structure

```
.
├── calculator.py          # Main calculator module
├── tests/
│   └── test_calculator.py # Test suite
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
└── README.md             # This file
```

## License

MIT
