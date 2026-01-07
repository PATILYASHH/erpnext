# Foundry ERP

Custom ERPNext v15 app for foundry business operations, designed for Frappe Cloud deployment.

> 📚 **New!** See [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) for complete documentation navigation
> 
> 🖼️ **Visual Guide** - Check [SCREENSHOTS.md](SCREENSHOTS.md) for detailed visual documentation of all features

## Overview

Foundry ERP is a comprehensive solution for managing foundry operations including:
- Multiple furnace management (IF, EAF, Cupola)
- Material tracking (Steel, SG Iron, CI)
- Heat-wise production with furnace-specific numbering
- Quality control and chemistry analysis
- Pattern lifecycle management
- Production planning and costing

## Features

### 1. Masters Module
- **Furnace Master**: Define furnaces with capacity and power ratings
- **Material Type Master**: Manage material types (Steel, SG, CI)
- **Grade Master**: Define material grades with standards (IS, ASTM, EN)
- **Chemistry Limits Master**: Set acceptable chemistry ranges per grade
- **Alloy Master**: Track alloy specifications and recovery percentages
- **Scrap Master**: Manage scrap materials and costs
- **Casting Master**: Define casting specifications
- **Pattern Master**: Track pattern inventory and condition

### 2. Pattern Management
- **Pattern Issue**: Track pattern issuance to production
- **Pattern Return**: Record pattern returns and condition

### 3. Production Planning
- **Monthly Production Plan**: Plan production targets by month
- **Daily Production Plan**: Daily production scheduling with shift tracking

### 4. Heat & Melting (Core Module)
- **Heat Entry**: 
  - Submittable DocType with furnace-wise naming (IF1-2025-001, IF2-2025-001, etc.)
  - Automatic yield calculation
  - Furnace capacity validation
  - Track planned vs actual quantities
- **Charge Mix**: Record scrap materials used in each heat
- **Alloy Addition**: Track alloy additions with recovery calculations

### 5. Quality & Chemistry
- **Lab Analysis Entry**:
  - Record chemistry test results
  - Automatic validation against Chemistry Limits Master
  - Auto-mark elements as within/out of limits
  - Throws error if chemistry is out of specification
- **Rework Entry**: Track rework quantities and reasons

### 6. Costing
- **Furnace Power Cost**: Define power rates per furnace
- **Heat Costing**: Calculate total heat cost (scrap + alloy + power)

## Business Logic

### Heat Entry Validations
1. **Furnace Capacity Validation**: Ensures actual melt qty doesn't exceed furnace capacity
2. **Yield Calculation**: Automatically calculates yield % = (good_qty / actual_melt_qty) × 100
3. **Furnace-wise Naming**: Each furnace gets its own naming series (IF1-.YYYY.-.###)

### Lab Analysis Validations
1. **Chemistry Validation**: Compares actual values against defined limits
2. **Auto-marking**: Sets within_limit flag for each element
3. **Error Handling**: Throws validation error if any element is out of range

## Roles & Permissions

### Roles Defined
1. **Furnace Operator**: Heat entry, pattern issue/return, daily planning
2. **Quality Engineer**: Lab analysis, chemistry limits, grade management
3. **Production Planner**: Production plans, casting and pattern masters
4. **Costing Engineer**: Costing data, alloy/scrap masters
5. **Management**: Read-only access to all modules

### Permission Structure
All DocTypes have granular permissions assigned by role with appropriate create, read, write, delete, and submit rights.

## Installation (Frappe Cloud)

1. Add this app to your Frappe Cloud bench
2. Install the app on your site
3. The following will be automatically created:
   - 7 modules
   - 19 DocTypes (with child tables)
   - 5 custom roles
   - Server-side validations
   - Client-side scripts

## Technical Details

- **Framework**: Frappe Framework v15
- **ERP Version**: ERPNext v15
- **Deployment**: Frappe Cloud compatible (no bench/SSH required)
- **Customization Approach**: Pure custom app (no ERPNext core modifications)
- **Upgrade Safety**: All business logic in DocTypes and scripts

## Module Structure

```
foundry_erp/
├── masters/                    # Master data DocTypes
├── pattern_management/         # Pattern issue/return
├── production_planning/        # Monthly/daily plans
├── heat___melting/            # Heat entry, charge mix, alloy addition
├── quality___chemistry/       # Lab analysis, rework
├── costing/                   # Power cost, heat costing
└── reports___dashboard/       # Future reports module
```

## Usage Example

### Typical Workflow
1. Setup masters (Furnaces, Materials, Grades, Chemistry Limits)
2. Create production plans (Monthly → Daily)
3. Record heat entry with furnace-specific numbering
4. Add charge mix and alloy additions for the heat
5. Perform lab analysis and validate chemistry
6. Calculate heat costing
7. Track patterns and rework as needed

## Documentation

For complete documentation, see:

- **[DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)** - Central navigation hub for all documentation
- **[SCREENSHOTS.md](SCREENSHOTS.md)** - Comprehensive visual guide with detailed mockups and examples
- **[FEATURES_VISUAL_GUIDE.md](FEATURES_VISUAL_GUIDE.md)** - Quick reference for all features and UI components
- **[INSTALLATION.md](INSTALLATION.md)** - Installation and setup guide
- **[SUMMARY.md](SUMMARY.md)** - Complete implementation summary

## License

MIT

## Support

For issues or questions related to this custom app, contact your implementation partner.
