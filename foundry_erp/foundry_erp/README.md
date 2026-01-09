# Foundry ERP Module

This module contains Foundry-specific customizations and extensions.

## Purpose

Add your custom doctypes, pages, reports, and other Frappe resources here.

## Example Structure

```
foundry_erp/
├── doctype/           # Custom DocTypes
├── page/              # Custom Pages
├── report/            # Custom Reports
├── workspace/         # Custom Workspaces
└── __init__.py
```

## Usage

To add a new doctype, use the Frappe bench command:

```bash
bench --site <site-name> new-doctype --module "Foundry ERP"
```
