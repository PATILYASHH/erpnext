# Contributing to Foundry ERP

Thank you for your interest in contributing to Foundry ERP!

## How to Contribute

### Reporting Issues

- Use the GitHub issue tracker
- Provide detailed information about the bug or feature request
- Include steps to reproduce for bugs
- Specify your environment (Frappe version, ERPNext version, OS, etc.)

### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   cd ~/frappe-bench/apps
   git clone https://github.com/<your-username>/foundry_erp
   ```
3. Install the app:
   ```bash
   bench --site <site-name> install-app foundry_erp
   ```
4. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Code Guidelines

1. **Follow Frappe conventions**
   - Use tabs for indentation (not spaces)
   - Follow PEP 8 for Python code
   - Use double quotes for strings

2. **Documentation**
   - Add docstrings to all functions and classes
   - Update README.md if adding new features
   - Document breaking changes

3. **Testing**
   - Write unit tests for new features
   - Ensure all tests pass before submitting
   - Test against both development and production databases

4. **Commits**
   - Write clear, descriptive commit messages
   - Reference issue numbers in commits
   - Keep commits focused and atomic

### Submitting Changes

1. Ensure all tests pass:
   ```bash
   bench --site <site-name> run-tests --app foundry_erp
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request on GitHub

4. Wait for review and address feedback

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

If you have questions, please:
- Open a GitHub issue
- Check existing issues and documentation
- Ask in the Frappe forum

Thank you for contributing!
