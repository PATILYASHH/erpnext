# Foundry ERP - Installation & Setup Guide

## Prerequisites
- Frappe Framework v15
- ERPNext v15
- Frappe Cloud account (for production deployment)

## Installation Steps

### For Frappe Cloud

1. **Add App to Your Site**
   - Log in to your Frappe Cloud dashboard
   - Navigate to your site
   - Go to "Apps" section
   - Click "Add App from GitHub"
   - Enter the repository URL
   - Click "Install"

2. **Install the App**
   The app will be automatically installed on your site with all dependencies.

### For Local Development (Bench)

```bash
# Navigate to your bench directory
cd ~/frappe-bench

# Get the app
bench get-app https://github.com/your-username/foundry_erp

# Install on site
bench --site your-site.localhost install-app foundry_erp

# Clear cache
bench --site your-site.localhost clear-cache

# Restart bench
bench restart
```

## Post-Installation Setup

### 1. Create Roles (If Not Auto-Created)

Navigate to Role List and ensure these roles exist:
- Furnace Operator
- Quality Engineer
- Production Planner
- Costing Engineer
- Management

### 2. Assign Roles to Users

Assign appropriate roles to users based on their responsibilities:

**Furnace Operator**: Floor-level staff operating furnaces
- Create Heat Entry
- Issue/Return Patterns
- View Daily Production Plans

**Quality Engineer**: QC team members
- Create Lab Analysis
- Manage Chemistry Limits
- Create Rework Entries

**Production Planner**: Planning team
- Create Production Plans
- Manage Master Data
- View all heat entries

**Costing Engineer**: Costing/Finance team
- Manage Costing Data
- View Heat Costing
- Manage Alloy/Scrap Costs

**Management**: Senior management
- Read-only access to all modules
- View reports and dashboards

### 3. Setup Master Data

Follow this sequence for initial master data setup:

#### Step 1: Material Types
Create material types:
- Steel
- SG (Spheroidal Graphite Iron)
- CI (Cast Iron) - for future

#### Step 2: Furnaces
Create furnace records with:
- Furnace Code (e.g., IF1, IF2, EAF1)
- Furnace Type (IF/EAF/Cupola)
- Capacity in Kg
- Power Rating in KW
- Set Status to Active

#### Step 3: Grades
Create grades for each material type:
- Grade Code (e.g., SG500-7, Steel-1020)
- Link to Material Type
- Standard (IS/ASTM/EN)
- CE Formula (optional)

#### Step 4: Chemistry Limits
For each grade, define acceptable chemistry ranges:
- Link to Grade
- Add elements (C, Si, Mn, P, S, etc.)
- Set Min and Max values in percentage

#### Step 5: Scrap & Alloy Masters
Create scrap types with costs per kg
Create alloy types with recovery percentages and costs

#### Step 6: Customers & Castings
- Create or link to existing ERPNext customers
- Create casting records with weight and grade specifications

#### Step 7: Pattern Masters
Create pattern records for each casting

### 4. Configure Furnace Power Costs
Set power rates for each furnace in Furnace Power Cost doctype

## Usage Workflow

### Daily Operations

1. **Morning**: Review Daily Production Plan
2. **Heat Creation**: Create Heat Entry with furnace-wise numbering
3. **Charge Recording**: Add Charge Mix (scrap materials)
4. **Alloy Addition**: Record alloy additions
5. **Lab Testing**: Create Lab Analysis Entry (auto-validates chemistry)
6. **Costing**: Calculate Heat Costing

### Monthly Planning

1. Create Monthly Production Plan
2. Break down into Daily Production Plans
3. Monitor execution through Heat Entries

## Naming Series Configuration

Heat entries automatically use furnace-wise naming:
- IF1 furnace: IF1-2025-001, IF1-2025-002...
- IF2 furnace: IF2-2025-001, IF2-2025-002...
- EAF1 furnace: EAF1-2025-001, EAF1-2025-002...

To add more furnaces, update the naming series in Heat Entry DocType.

## Key Validations

### Heat Entry
- Actual melt qty must not exceed furnace capacity
- Yield % auto-calculated: (good_qty / actual_melt_qty) × 100

### Lab Analysis
- Chemistry values validated against Chemistry Limits Master
- Error thrown if any element is out of specification
- Status auto-set based on validation

## Troubleshooting

### Issue: Roles not appearing
**Solution**: Clear cache and reload (Ctrl+Shift+R)

### Issue: Chemistry validation errors
**Solution**: Ensure Chemistry Limits Master is created for the grade

### Issue: Naming series conflict
**Solution**: Check if naming series already exists in other DocTypes

### Issue: Permissions not working
**Solution**: Verify role assignment and clear cache

## Customization

### Adding New Furnaces
1. Create furnace in Furnace Master
2. Update Heat Entry naming series to include new furnace code
3. Create Furnace Power Cost record

### Adding New Material Types
1. Create in Material Type Master
2. Create corresponding Grades
3. Set up Chemistry Limits

### Adding Custom Fields
Use ERPNext's Customize Form feature (avoid modifying DocType JSON directly)

## Backup & Migration

### Exporting Data
Use Data Import/Export tool in ERPNext to backup:
- All master data
- Transaction data (Heat Entry, Lab Analysis, etc.)

### Migrating Between Sites
1. Export fixtures from source site
2. Import fixtures to destination site
3. Verify data integrity

## Support & Maintenance

### Regular Maintenance
- Weekly: Review and archive old heat entries
- Monthly: Review costing data
- Quarterly: Audit chemistry limits and update if needed

### Performance Optimization
- Archive old transaction data periodically
- Use filters when viewing large lists
- Limit report date ranges

## Additional Resources

- Frappe Documentation: https://frappeframework.com/docs
- ERPNext Documentation: https://docs.erpnext.com
- Frappe Cloud: https://frappecloud.com

## Version History

- v0.0.1 (2026-01-06): Initial release
  - All 19 DocTypes
  - 5 custom roles
  - Server and client validations
  - Furnace-wise heat numbering
