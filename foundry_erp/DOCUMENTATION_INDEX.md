# Foundry ERP - Documentation Index

Welcome to the Foundry ERP documentation! This custom ERPNext v15 application provides comprehensive foundry management capabilities.

## 📚 Documentation Structure

### Getting Started

1. **[README.md](README.md)** - Start here!
   - Application overview
   - Feature list
   - Module structure
   - Quick usage examples
   - Technical specifications

2. **[INSTALLATION.md](INSTALLATION.md)** - Installation & Setup
   - Prerequisites
   - Frappe Cloud installation steps
   - Local bench installation
   - Post-installation setup
   - Master data configuration
   - Troubleshooting guide

### Implementation Details

3. **[SUMMARY.md](SUMMARY.md)** - Complete Implementation Summary
   - Project deliverables
   - All 26 DocTypes detailed
   - Business logic documentation
   - Roles and permissions
   - Technical compliance checklist
   - Testing checklist
   - Success criteria

### Visual Documentation

4. **[SCREENSHOTS.md](SCREENSHOTS.md)** - Comprehensive Visual Guide
   - Detailed screenshot descriptions for all features
   - UI mockups and layouts
   - Form view examples
   - List view examples
   - Workflow diagrams
   - Validation examples (success and error states)
   - Cost breakdown visualizations
   - Chemistry validation flows
   - Pattern management workflows
   - Notes for capturing actual screenshots

5. **[FEATURES_VISUAL_GUIDE.md](FEATURES_VISUAL_GUIDE.md)** - Quick Visual Reference
   - Quick reference table for all DocTypes
   - Module structure diagram
   - Top 10 visual features
   - UI component guide
   - Color scheme reference
   - Role-based view documentation
   - Screenshot specifications
   - Workflow diagrams

---

## 📖 Documentation by Topic

### For New Users

**"I want to understand what this app does"**
→ Start with [README.md](README.md)

**"I want to see visual examples of the features"**
→ Read [SCREENSHOTS.md](SCREENSHOTS.md) or [FEATURES_VISUAL_GUIDE.md](FEATURES_VISUAL_GUIDE.md)

**"I want to install and set up the app"**
→ Follow [INSTALLATION.md](INSTALLATION.md)

### For Administrators

**"I need complete implementation details"**
→ Review [SUMMARY.md](SUMMARY.md)

**"I need to configure roles and permissions"**
→ See [INSTALLATION.md](INSTALLATION.md#2-assign-roles-to-users) and [SUMMARY.md](SUMMARY.md#5-roles--permissions)

**"I need to set up master data"**
→ Follow [INSTALLATION.md](INSTALLATION.md#3-setup-master-data)

### For Developers

**"I want to understand the technical architecture"**
→ Read [SUMMARY.md](SUMMARY.md#technical-compliance)

**"I want to see the DocType structure"**
→ Review [SUMMARY.md](SUMMARY.md#3-doctypes-implemented-19--7-child-tables--26-total)

**"I want to understand business logic"**
→ See [SUMMARY.md](SUMMARY.md#4-business-logic-implemented)

### For Documentation Teams

**"I need to create user manuals with screenshots"**
→ Use [SCREENSHOTS.md](SCREENSHOTS.md) as a template

**"I need specifications for taking screenshots"**
→ Follow [SCREENSHOTS.md](SCREENSHOTS.md#how-to-capture-these-screenshots)

**"I need a quick reference for all features"**
→ Use [FEATURES_VISUAL_GUIDE.md](FEATURES_VISUAL_GUIDE.md)

---

## 🎯 Key Features Documented

### 1. Masters Module (9 DocTypes)
- Furnace Master - Define furnaces with capacity and power ratings
- Material Type Master - Manage material types (Steel, SG, CI)
- Grade Master - Define material grades with standards
- Chemistry Limits Master - Set acceptable chemistry ranges
- Alloy Master - Track alloy specifications and recovery
- Scrap Master - Manage scrap materials and costs
- Casting Master - Define casting specifications
- Pattern Master - Track pattern inventory and condition

📄 Details: [README.md#1-masters-module](README.md#1-masters-module)  
🖼️ Screenshots: [SCREENSHOTS.md#master-data-management](SCREENSHOTS.md#master-data-management)

### 2. Pattern Management (2 DocTypes)
- Pattern Issue - Track pattern issuance to production
- Pattern Return - Record pattern returns and condition

📄 Details: [README.md#2-pattern-management](README.md#2-pattern-management)  
🖼️ Screenshots: [SCREENSHOTS.md#pattern-management](SCREENSHOTS.md#pattern-management)

### 3. Production Planning (2 Main + 2 Child DocTypes)
- Monthly Production Plan - Plan production targets by month
- Daily Production Plan - Daily production scheduling

📄 Details: [README.md#3-production-planning](README.md#3-production-planning)  
🖼️ Screenshots: [SCREENSHOTS.md#production-planning](SCREENSHOTS.md#production-planning)

### 4. Heat & Melting (3 Main + 2 Child DocTypes) ⭐ CORE MODULE
- **Heat Entry** - Submittable DocType with:
  - Furnace-wise naming (IF1-2025-001, IF2-2025-001, etc.)
  - Automatic yield calculation
  - Furnace capacity validation
  - Track planned vs actual quantities
- Charge Mix - Record scrap materials used in each heat
- Alloy Addition - Track alloy additions with recovery calculations

📄 Details: [README.md#4-heat--melting-core-module](README.md#4-heat--melting-core-module)  
🖼️ Screenshots: [SCREENSHOTS.md#heat--melting-operations](SCREENSHOTS.md#heat--melting-operations)  
⚙️ Business Logic: [SUMMARY.md#heat-entry-heat_entrypy](SUMMARY.md#heat-entry-heat_entrypy)

### 5. Quality & Chemistry (2 Main + 1 Child DocType) ⭐ ADVANCED FEATURE
- **Lab Analysis Entry** - Record chemistry test results with:
  - Automatic validation against Chemistry Limits Master
  - Auto-mark elements as within/out of limits
  - Throws error if chemistry is out of specification
- Rework Entry - Track rework quantities and reasons

📄 Details: [README.md#5-quality--chemistry](README.md#5-quality--chemistry)  
🖼️ Screenshots: [SCREENSHOTS.md#quality--chemistry-control](SCREENSHOTS.md#quality--chemistry-control)  
⚙️ Business Logic: [SUMMARY.md#lab-analysis-entry-lab_analysis_entrypy](SUMMARY.md#lab-analysis-entry-lab_analysis_entrypy)

### 6. Costing (2 DocTypes)
- Furnace Power Cost - Define power rates per furnace
- Heat Costing - Calculate total heat cost (scrap + alloy + power)

📄 Details: [README.md#6-costing](README.md#6-costing)  
🖼️ Screenshots: [SCREENSHOTS.md#costing-features](SCREENSHOTS.md#costing-features)

---

## 🔑 Key Validations & Features

### Furnace-Wise Heat Numbering
Each furnace gets its own naming series:
- IF1 furnace → IF1-2025-001, IF1-2025-002...
- IF2 furnace → IF2-2025-001, IF2-2025-002...
- EAF1 furnace → EAF1-2025-001, EAF1-2025-002...

📄 Details: [SUMMARY.md#furnace-wise-heat-numbering](SUMMARY.md#furnace-wise-heat-numbering)

### Heat Entry Validations
1. **Furnace Capacity Validation** - Ensures actual melt qty doesn't exceed furnace capacity
2. **Yield Calculation** - Automatically calculates yield % = (good_qty / actual_melt_qty) × 100
3. **Real-time Updates** - Client-side JavaScript for instant feedback

📄 Details: [README.md#heat-entry-validations](README.md#heat-entry-validations)  
🖼️ Example: [SCREENSHOTS.md#9-heat-entry-form---main-feature](SCREENSHOTS.md#9-heat-entry-form---main-feature)

### Lab Analysis Chemistry Validation
1. **Automatic Limit Fetching** - Pulls min/max values from Chemistry Limits Master
2. **Element-by-Element Validation** - Compares actual vs limits
3. **Visual Indicators** - Green checkmarks for OK, red X for out-of-spec
4. **Error Prevention** - Throws error and prevents save if chemistry is out of range

📄 Details: [README.md#lab-analysis-validations](README.md#lab-analysis-validations)  
🖼️ Example: [SCREENSHOTS.md#13-lab-analysis-entry---chemistry-validation](SCREENSHOTS.md#13-lab-analysis-entry---chemistry-validation)

---

## 👥 Roles & Permissions

### Custom Roles (5)
1. **Furnace Operator** - Heat entry, pattern management, daily operations
2. **Quality Engineer** - Lab analysis, chemistry limits, quality control
3. **Production Planner** - Production planning, master data management
4. **Costing Engineer** - Costing data, alloy/scrap cost management
5. **Management** - Read-only access across all modules

📄 Full Permissions: [SUMMARY.md#5-roles--permissions](SUMMARY.md#5-roles--permissions)  
🖼️ Visual Matrix: [FEATURES_VISUAL_GUIDE.md#role-based-views](FEATURES_VISUAL_GUIDE.md#role-based-views)

---

## 🛠️ Technical Information

### Technology Stack
- **Framework**: Frappe Framework v15
- **ERP Version**: ERPNext v15
- **Deployment**: Frappe Cloud compatible
- **Language**: Python (server), JavaScript (client)
- **Database**: MariaDB/PostgreSQL (via Frappe)

### App Compliance
- ✅ No ERPNext core modifications
- ✅ No custom patches
- ✅ No server file access assumptions
- ✅ Cloud-safe implementation
- ✅ Upgrade-safe design

📄 Full Technical Details: [SUMMARY.md#technical-compliance](SUMMARY.md#technical-compliance)

---

## 📊 Statistics

- **Total Modules**: 7
- **Total DocTypes**: 26 (19 main + 7 child tables)
- **Custom Roles**: 5
- **Server Validations**: 2 major (Heat Entry, Lab Analysis)
- **Client Scripts**: 1 (Heat Entry)
- **Total Files Created**: 100+
- **Lines of Code**: 3,500+

---

## 🚀 Quick Start Guide

1. **Install the App**
   ```bash
   # For Frappe Cloud
   - Add app from GitHub to your site
   - Install on site
   
   # For Local Bench
   bench get-app [repository-url]
   bench --site [site-name] install-app foundry_erp
   bench --site [site-name] clear-cache
   bench restart
   ```

2. **Setup Basic Masters**
   - Create Material Types (Steel, SG, CI)
   - Create Furnaces (IF1, IF2, EAF1)
   - Create Grades for each material type
   - Define Chemistry Limits for each grade

3. **Configure Costs**
   - Set up Scrap Master with costs
   - Set up Alloy Master with recovery percentages
   - Configure Furnace Power Costs

4. **Start Operations**
   - Create Monthly Production Plan
   - Break down into Daily Production Plans
   - Record Heat Entries
   - Perform Lab Analysis
   - Calculate Heat Costing

📄 Detailed Setup: [INSTALLATION.md](INSTALLATION.md)

---

## 🔍 Search Documentation

### By Module
- [Masters](README.md#1-masters-module)
- [Pattern Management](README.md#2-pattern-management)
- [Production Planning](README.md#3-production-planning)
- [Heat & Melting](README.md#4-heat--melting-core-module)
- [Quality & Chemistry](README.md#5-quality--chemistry)
- [Costing](README.md#6-costing)

### By DocType
- [Furnace Master](SCREENSHOTS.md#1-furnace-master-list-view)
- [Grade Master](SCREENSHOTS.md#3-grade-master-with-chemistry-limits)
- [Chemistry Limits Master](SCREENSHOTS.md#4-chemistry-limits-master)
- [Heat Entry](SCREENSHOTS.md#9-heat-entry-form---main-feature)
- [Lab Analysis Entry](SCREENSHOTS.md#13-lab-analysis-entry---chemistry-validation)
- [Heat Costing](SCREENSHOTS.md#19-heat-costing)
- [All DocTypes](FEATURES_VISUAL_GUIDE.md#quick-reference-table)

### By Feature
- [Furnace-wise Naming](SUMMARY.md#furnace-wise-heat-numbering)
- [Yield Calculation](SCREENSHOTS.md#10-heat-entry---client-side-calculations)
- [Chemistry Validation](SCREENSHOTS.md#13-lab-analysis-entry---chemistry-validation)
- [Cost Breakdown](SCREENSHOTS.md#19-heat-costing)
- [Workflow Diagrams](SCREENSHOTS.md#workflow-diagrams)

---

## 📝 Version History

**v0.0.1** (January 2026) - Initial Release
- All 26 DocTypes implemented
- 5 custom roles with permissions
- Server and client-side validations
- Furnace-wise heat numbering
- Complete documentation suite

---

## 🆘 Support & Resources

### Internal Documentation
- [Installation Guide](INSTALLATION.md)
- [Troubleshooting](INSTALLATION.md#troubleshooting)
- [Usage Workflow](README.md#usage-example)

### External Resources
- [Frappe Framework Documentation](https://frappeframework.com/docs)
- [ERPNext Documentation](https://docs.erpnext.com)
- [Frappe Cloud](https://frappecloud.com)

### Contact
For issues or questions related to this custom app, contact your implementation partner.

---

## 📄 License

MIT License - See [license.txt](license.txt) for details

---

**Last Updated**: January 2026  
**App Version**: 0.0.1  
**ERPNext Version**: v15  
**Frappe Version**: v15
