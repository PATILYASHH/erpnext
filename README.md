# Foundry ERP

A custom Frappe app that extends ERPNext with foundry-specific business logic and customizations.

## Overview

Foundry ERP is a standalone Frappe application that depends on ERPNext. It provides custom extensions and business logic specific to foundry operations while leveraging the full power of ERPNext's core ERP functionality.

## Features

- Built on top of ERPNext v15.x
- Extends ERPNext with custom functionality
- Follows standard Frappe app architecture
- Does not modify ERPNext core logic

## Installation

### Prerequisites

- Frappe Framework (v15.x or higher)
- ERPNext (v15.x or higher)
- Python 3.10 or higher

### Steps

1. Get the app from the repository:
```bash
bench get-app https://github.com/PATILYASHH/foundry_erp
```

2. Install the app on your site:
```bash
bench --site <your-site-name> install-app foundry_erp
```

## Development Setup

1. Clone the repository:
```bash
cd ~/frappe-bench/apps
git clone https://github.com/PATILYASHH/foundry_erp
```

2. Install the app in your site:
```bash
bench --site <your-site-name> install-app foundry_erp
```

3. Start the development server:
```bash
bench start
```

## Architecture

This application follows the standard Frappe app structure:

```
foundry_erp/
├── foundry_erp/          # Main app directory
│   ├── __init__.py       # App initialization
│   ├── hooks.py          # App hooks and configuration
│   ├── modules.txt       # List of modules
│   ├── config/           # Desk configuration
│   ├── public/           # Static assets (JS, CSS)
│   ├── templates/        # Jinja templates
│   └── fixtures/         # Default data fixtures
├── pyproject.toml        # Python project configuration
└── README.md            # This file
```

## Relationship with ERPNext

Foundry ERP is designed as a **companion app** to ERPNext, not a fork or replacement:

- **Depends on ERPNext**: ERPNext must be installed before Foundry ERP
- **Extends, doesn't replace**: Uses ERPNext's core modules (Accounts, Stock, Manufacturing, etc.)
- **Custom additions**: Adds foundry-specific doctypes, workflows, and business logic
- **No core modifications**: Does not modify ERPNext's core functionality

## License

MIT License

## Support

For issues and questions, please use the GitHub issue tracker.
