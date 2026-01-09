# Foundry ERP - Development Guide

## Overview

Foundry ERP is a custom Frappe application that extends ERPNext. It is designed as a **companion app** that depends on ERPNext rather than a fork.

## Architecture

### Dependency Chain
```
Frappe Framework (v15.x)
    ↓
ERPNext (v15.x)
    ↓
Foundry ERP (this app)
```

### Directory Structure
```
foundry_erp/
├── foundry_erp/              # Main app directory
│   ├── __init__.py          # App initialization
│   ├── hooks.py             # App hooks and configuration
│   ├── modules.txt          # List of modules
│   ├── config/              # Desk configuration
│   ├── fixtures/            # Default data fixtures
│   ├── public/              # Static assets (JS, CSS)
│   │   ├── js/
│   │   └── css/
│   ├── templates/           # Jinja templates
│   └── foundry_erp/         # Sample module directory
│       ├── __init__.py
│       ├── doctype/         # Custom DocTypes
│       ├── page/            # Custom Pages
│       ├── report/          # Custom Reports
│       └── workspace/       # Custom Workspaces
├── pyproject.toml           # Python project configuration
├── setup.py                 # Setup script
├── MANIFEST.in              # Package manifest
└── README.md               # This file
```

## Installation

### Prerequisites

1. Frappe Framework v15.x or higher
2. ERPNext v15.x or higher
3. Python 3.10 or higher

### Install via Bench

```bash
# Navigate to your bench directory
cd ~/frappe-bench

# Get the app
bench get-app https://github.com/PATILYASHH/foundry_erp

# Install on your site
bench --site <your-site-name> install-app foundry_erp
```

### Verify Installation

```bash
# Check installed apps
bench --site <your-site-name> list-apps

# You should see:
# frappe
# erpnext
# foundry_erp
```

## Development

### Creating Custom DocTypes

To create a new DocType in the Foundry ERP module:

```bash
bench --site <site-name> new-doctype --module "Foundry ERP"
```

This will create a new DocType in `foundry_erp/foundry_erp/foundry_erp/doctype/`.

### Creating Custom Pages

```bash
bench --site <site-name> make-page <page-name> --module "Foundry ERP"
```

### Creating Custom Reports

1. Create a report via the UI under "Report Builder"
2. Save the report
3. Export the report JSON to `foundry_erp/foundry_erp/foundry_erp/report/`

### Extending ERPNext DocTypes

To extend an ERPNext DocType (e.g., Sales Order), add to `hooks.py`:

```python
# Override doctype class
override_doctype_class = {
    "Sales Order": "foundry_erp.overrides.sales_order.FoundrySalesOrder"
}

# Add custom fields
doc_events = {
    "Sales Order": {
        "validate": "foundry_erp.overrides.sales_order.validate_foundry_data"
    }
}
```

Then create the override file:

```python
# foundry_erp/foundry_erp/overrides/sales_order.py
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder

class FoundrySalesOrder(SalesOrder):
    def validate(self):
        super().validate()
        # Add your custom validation here
        pass
```

### Adding Custom Fixtures

Create fixture files in `foundry_erp/foundry_erp/fixtures/` and reference them in `hooks.py`:

```python
fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Foundry ERP"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Foundry ERP"]]},
]
```

## Configuration

### hooks.py

The `hooks.py` file is the central configuration file for the app. Key configurations:

- `app_name`: The unique identifier for your app
- `required_apps`: Apps that must be installed before this app
- `doc_events`: Hook into document lifecycle events
- `scheduler_events`: Schedule background tasks
- `override_whitelisted_methods`: Override API methods

Example:

```python
# Scheduler Events
scheduler_events = {
    "daily": [
        "foundry_erp.tasks.daily_sync"
    ],
    "hourly": [
        "foundry_erp.tasks.hourly_update"
    ]
}

# Document Events
doc_events = {
    "Sales Order": {
        "on_submit": "foundry_erp.events.on_sales_order_submit",
        "on_cancel": "foundry_erp.events.on_sales_order_cancel"
    }
}
```

## Best Practices

### 1. Do NOT Modify ERPNext Core

- Never modify ERPNext's core files directly
- Always use hooks and overrides to extend functionality
- Use custom fields instead of modifying DocType JSON

### 2. Use Module Organization

- Keep related functionality in modules
- One module per business domain
- Follow Frappe's naming conventions

### 3. Version Control

- Keep your customizations in version control
- Use migrations for database changes
- Document breaking changes

### 4. Testing

Create tests in your module:

```python
# foundry_erp/foundry_erp/foundry_erp/doctype/custom_doctype/test_custom_doctype.py
import frappe
import unittest

class TestCustomDocType(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Custom DocType",
            "field1": "value1"
        })
        doc.insert()
        self.assertTrue(doc.name)
```

Run tests:

```bash
bench --site <site-name> run-tests --app foundry_erp
```

## Updating the App

```bash
# Get latest changes
cd ~/frappe-bench/apps/foundry_erp
git pull

# Migrate the site
bench --site <site-name> migrate

# Clear cache
bench --site <site-name> clear-cache
```

## Troubleshooting

### App not showing after installation

```bash
# Clear cache and rebuild
bench --site <site-name> clear-cache
bench build
```

### Import errors

Make sure ERPNext is installed and activated:

```bash
bench --site <site-name> list-apps
```

### Permission errors

Check that the app is enabled in Site Config:

```bash
bench --site <site-name> enable-app foundry_erp
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests
5. Submit a pull request

## Resources

- [Frappe Framework Documentation](https://frappeframework.com/docs)
- [ERPNext Documentation](https://docs.erpnext.com)
- [Frappe Developer API](https://frappeframework.com/docs/user/en/api)

## License

MIT License - See LICENSE file for details
