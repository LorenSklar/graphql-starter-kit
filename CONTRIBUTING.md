# Contributing to GraphQL Starter Kit

Thank you for your interest in contributing to the GraphQL Starter Kit! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test your changes**: `python3 -m pytest`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## 📋 Development Setup

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/graphql-starter-kit.git
cd graphql-starter-kit

# Install dependencies
pip install -r requirements.txt

# Initialize database
python3 load_sample_data.py

# Run the server
python3 main.py
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python3 -m pytest

# Run tests with coverage
python3 -m pytest --cov=app

# Run specific test file
python3 -m pytest tests/test_resolvers.py
```

### Writing Tests
- Place test files in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Test both success and error cases

## 📝 Code Style

### Python
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

### GraphQL
- Use camelCase for query/mutation names
- Use PascalCase for type names
- Use SCREAMING_SNAKE_CASE for constants
- Add descriptions to types and fields

### Database
- Use direct SQL queries (no ORM)
- Use parameterized queries to prevent SQL injection
- Add proper error handling

## 🐛 Reporting Bugs

### Before Reporting
1. Check if the issue has already been reported
2. Try to reproduce the issue with the latest version
3. Check the documentation for solutions

### Bug Report Template
```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment:**
- OS: [e.g. macOS, Windows, Linux]
- Python version: [e.g. 3.8, 3.9, 3.10]
- Package versions: [from requirements.txt]

**Additional context**
Add any other context about the problem here.
```

## 💡 Suggesting Features

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions.

**Additional context**
Add any other context or screenshots about the feature request.
```

## 🔄 Pull Request Process

### Before Submitting
1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Run existing tests** to ensure nothing breaks
4. **Update CHANGELOG.md** with your changes

### PR Template
```markdown
**Description**
Brief description of changes made.

**Type of change**
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

**Testing**
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Updated existing tests if needed

**Checklist**
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

## 📚 Documentation

### Updating Documentation
- Keep README.md up to date with new features
- Update API documentation when endpoints change
- Add examples for new functionality
- Update deployment guides if needed

## 🏷️ Release Process

### For Maintainers
1. **Update version** in setup.py and main.py
2. **Update CHANGELOG.md** with release notes
3. **Create a release tag**: `git tag v1.0.0`
4. **Push the tag**: `git push origin v1.0.0`
5. **Create GitHub release** with release notes

## 🤝 Community Guidelines

### Be Respectful
- Be kind and respectful to other contributors
- Use inclusive language
- Give constructive feedback

### Be Helpful
- Help new contributors get started
- Answer questions in issues and discussions
- Share knowledge and best practices

### Be Patient
- Maintainers are volunteers
- Response times may vary
- Complex issues take time to resolve

## 📞 Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Security**: See SECURITY.md for security-related issues

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to GraphQL Starter Kit! 🎉 