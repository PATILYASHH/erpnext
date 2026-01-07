# Foundry ERP - Visual Features Quick Reference

## 📋 Table of Contents

- [Overview](#overview)
- [Key Visual Elements](#key-visual-elements)
- [Module Screenshots Index](#module-screenshots-index)
- [Feature Highlights](#feature-highlights)
- [UI Components](#ui-components)

---

## Overview

This document provides a quick visual reference guide for the Foundry ERP application added in PR #1. The application introduces a complete foundry management system with 26 DocTypes across 7 modules.

**Application Details:**
- **Name**: Foundry ERP
- **Version**: 0.0.1
- **Framework**: ERPNext v15 / Frappe v15
- **Total DocTypes**: 26 (19 main + 7 child tables)
- **Custom Roles**: 5
- **Deployment**: Frappe Cloud compatible

---

## Key Visual Elements

### 🎨 Application Icon

**Desktop Icon:**
- **Color**: Orange (#FF5733)
- **Icon**: Factory/Industry symbol (fa fa-industry)
- **Location**: ERPNext Desktop
- **Label**: "Foundry ERP"

### 🏗️ Module Structure

```
Foundry ERP
│
├── 📦 Masters (9 DocTypes)
│   ├── Furnace Master
│   ├── Material Type Master
│   ├── Grade Master
│   ├── Chemistry Limits Master
│   ├── Alloy Master
│   ├── Scrap Master
│   ├── Casting Master
│   └── Pattern Master
│
├── 🔄 Pattern Management (2 DocTypes)
│   ├── Pattern Issue
│   └── Pattern Return
│
├── 📅 Production Planning (2 DocTypes + 2 Child)
│   ├── Monthly Production Plan
│   └── Daily Production Plan
│
├── 🔥 Heat & Melting (3 DocTypes + 2 Child)
│   ├── Heat Entry (SUBMITTABLE)
│   ├── Charge Mix
│   └── Alloy Addition
│
├── 🧪 Quality & Chemistry (2 DocTypes + 1 Child)
│   ├── Lab Analysis Entry
│   └── Rework Entry
│
├── 💰 Costing (2 DocTypes)
│   ├── Furnace Power Cost
│   └── Heat Costing
│
└── 📊 Reports & Dashboard (Future)
```

---

## Module Screenshots Index

### 1. Masters Module Screenshots

#### Furnace Master
**Purpose**: Define and manage furnaces
**Key Fields**:
- Furnace Code (Unique identifier)
- Furnace Name
- Type (IF/EAF/Cupola)
- Capacity in Kg
- Power Rating in KW
- Status (Active/Maintenance)

**Visual Highlights**:
- ✅ Status indicator badges
- 🔵 Capacity validation
- 📊 Power consumption tracking

#### Material Type Master
**Purpose**: Define material types (Steel, SG, CI)
**Key Fields**:
- Material Type
- Description
- Active checkbox

**Visual Highlights**:
- Simple, clean interface
- Quick toggle for active/inactive

#### Grade Master
**Purpose**: Define material grades with standards
**Key Fields**:
- Grade Code
- Material Type (Link)
- Standard (IS/ASTM/EN dropdown)
- CE Formula
- Active checkbox

**Visual Highlights**:
- 🔗 Linked to Material Type
- 📐 Formula field for calculations

#### Chemistry Limits Master
**Purpose**: Set acceptable chemistry ranges per grade
**Key Components**:
- Main form with grade selection
- Child table for element limits

**Child Table Columns**:
| Element | Min Value (%) | Max Value (%) |
|---------|---------------|---------------|
| C       | 3.40          | 3.80          |
| Si      | 2.20          | 2.80          |
| Mn      | 0.20          | 0.50          |

**Visual Highlights**:
- 📋 Editable grid for quick data entry
- ✏️ Inline editing capabilities
- 🎯 Precision control (2 decimal places)

#### Alloy Master
**Purpose**: Track alloy specifications and recovery
**Key Fields**:
- Alloy Name
- Element
- Recovery Percent
- Cost per Kg

**Visual Highlights**:
- 💰 Currency formatting
- 📊 Recovery percentage display

#### Scrap Master
**Purpose**: Manage scrap materials and costs
**Key Fields**:
- Scrap Name
- Material Type (Link)
- Cost per Kg

**Visual Highlights**:
- 🔗 Material type integration
- 💵 Cost tracking

#### Casting Master
**Purpose**: Define casting specifications
**Key Fields**:
- Casting Code
- Customer (Link to ERPNext Customer)
- Weight per Piece
- Grade (Link)
- Active checkbox

**Visual Highlights**:
- 🔗 Integration with ERPNext Customers
- ⚖️ Weight specifications
- 📏 Grade linkage

#### Pattern Master
**Purpose**: Track pattern inventory and condition
**Key Fields**:
- Pattern Code
- Casting (Link)
- Ownership (Customer/Company)
- Storage Location
- Condition (Good/Repair/Scrap)
- Life Count

**Visual Highlights**:
- 📍 Storage location tracking
- 🔄 Life cycle counting
- ⚠️ Condition indicators

---

### 2. Pattern Management Screenshots

#### Pattern Issue
**Purpose**: Track pattern issuance to production
**Naming**: PI-.YYYY.-.####
**Key Fields**:
- Pattern (Link)
- Issue Date
- Issued To
- Purpose

**Visual Highlights**:
- 📤 Outgoing transaction
- 🕒 Date/time stamping
- 📝 Purpose documentation

#### Pattern Return
**Purpose**: Record pattern returns with condition
**Naming**: PR-.YYYY.-.####
**Key Fields**:
- Pattern (Link)
- Issue Reference
- Return Date
- Condition Assessment
- Remarks

**Visual Highlights**:
- 📥 Incoming transaction
- ✅ Condition assessment
- 🔗 Links back to issue

---

### 3. Production Planning Screenshots

#### Monthly Production Plan
**Purpose**: Plan production targets by month
**Naming**: MPP-.YYYY.-.####
**Key Components**:
- Header with month/year
- Child table with production items

**Child Table**:
| Casting | Grade | Target Qty | Heats | Remarks |
|---------|-------|------------|-------|---------|
| CAST-1001 | SG500-7 | 5000 Kg | 10 | High priority |

**Visual Highlights**:
- 📅 Calendar integration
- 📊 Target tracking
- 📈 Heat count estimation

#### Daily Production Plan
**Purpose**: Daily shift-wise production scheduling
**Naming**: DPP-.YYYY.-.####
**Key Fields**:
- Date
- Shift (Morning/Afternoon/Night)
- Furnace
- Child table with planned items

**Visual Highlights**:
- ⏰ Shift-based planning
- 🔥 Furnace allocation
- 🎯 Priority ordering

---

### 4. Heat & Melting Screenshots (★ Core Module)

#### Heat Entry (★ MAIN FEATURE)
**Purpose**: Record heat operations with validations
**Naming**: Furnace-wise (IF1-.YYYY.-.###, IF2-.YYYY.-.###, EAF1-.YYYY.-.###)
**Type**: SUBMITTABLE DocType

**Key Fields**:
```
┌─────────────────────────────────────┐
│ Furnace:      [IF1 ▼]               │
│ Date/Time:    15-01-2026 08:30      │
│ Grade:        [SG500-7 ▼]           │
│ Material:     SG (auto)             │
│                                     │
│ Planned:      500.00 Kg             │
│ Actual Melt:  520.00 Kg             │
│ Good Qty:     485.00 Kg (auto)      │
│ Rejection:    35.00 Kg              │
│ Yield %:      93.27% (auto)         │
│                                     │
│ Status:       [Open ▼]              │
└─────────────────────────────────────┘
```

**Visual Highlights**:
- 🏷️ **Furnace-wise naming** - Automatic assignment
- 🔄 **Real-time calculations** - Yield auto-updates
- ⚠️ **Capacity validation** - Prevents overloading
- 📱 **Client-side scripts** - Instant feedback
- ✅ **Submittable workflow** - Draft → Submit states

**Server-Side Validations**:
```python
✓ validate_furnace_capacity()
  → Actual melt ≤ Furnace capacity
  
✓ calculate_yield()
  → (Good Qty / Actual Melt) × 100
```

**Client-Side Features**:
```javascript
✓ Live yield calculation
✓ Auto-calculate good qty
✓ Real-time field updates
```

#### Charge Mix
**Purpose**: Record scrap materials used
**Naming**: Auto-named by heat
**Key Components**:
- Heat link
- Total charge (auto-calculated)
- Child table with scrap items

**Child Table**:
| Scrap Type | Qty (Kg) | Cost (₹) |
|------------|----------|----------|
| Heavy Scrap | 300.00 | 7,500.00 |
| Boring Scrap | 120.00 | 3,360.00 |

**Visual Highlights**:
- 🔗 Linked to Heat Entry
- 💰 Cost aggregation
- ⚖️ Weight totaling

#### Alloy Addition
**Purpose**: Track alloy additions with recovery
**Naming**: Auto-named by heat
**Key Features**:
- Recovery % auto-fetched
- Effective quantity auto-calculated

**Child Table**:
| Alloy | Qty (Kg) | Recovery % | Effective Qty |
|-------|----------|------------|---------------|
| FeSi-75 | 8.00 | 72.0 | 5.76 Kg |
| FeMn-70 | 4.50 | 68.0 | 3.06 Kg |

**Calculation**:
```
Effective Qty = Qty × (Recovery % / 100)
```

**Visual Highlights**:
- 🧮 Automatic calculations
- 📊 Recovery tracking
- ⚗️ Effective addition display

---

### 5. Quality & Chemistry Screenshots (★ Advanced Feature)

#### Lab Analysis Entry (★ CHEMISTRY VALIDATION)
**Purpose**: Record and validate chemistry test results
**Naming**: LAB-.YYYY.-.####
**Key Features**:
- Automatic limit fetching
- Real-time validation
- Visual status indicators

**Interface Layout**:
```
Lab Analysis Entry: LAB-2026-001
═══════════════════════════════════

Heat: IF1-2026-001
Sample No: S-001
Analyst: Lab Tech - Ramesh

Chemistry Results Table:
┌────────────────────────────────────────────────────┐
│ Element │ Actual │ Min │ Max │ ✓/✗ │ Status      │
├────────────────────────────────────────────────────┤
│ C       │ 3.65   │3.40 │3.80 │ ✓   │ ✓ OK        │
│ Si      │ 2.45   │2.20 │2.80 │ ✓   │ ✓ OK        │
│ Mn      │ 0.35   │0.20 │0.50 │ ✓   │ ✓ OK        │
│ P       │ 0.03   │0.00 │0.05 │ ✓   │ ✓ OK        │
│ S       │ 0.01   │0.00 │0.02 │ ✓   │ ✓ OK        │
│ Mg      │ 0.04   │0.03 │0.06 │ ✓   │ ✓ OK        │
└────────────────────────────────────────────────────┘

Overall Status: ✓ ACCEPTED
```

**Server-Side Validation Logic**:
```python
validate_chemistry_limits():
  1. Fetch Chemistry Limits Master for grade
  2. For each element:
     - Compare actual vs min/max
     - Set within_limit flag
     - Mark status
  3. If any out of range:
     - throw validation error
     - prevent save
```

**Visual Highlights**:
- ✅ **Green checkmarks** for within-spec
- ❌ **Red X marks** for out-of-spec
- ⚠️ **Validation errors** prevent bad data
- 🎯 **Automatic limit population**
- 📊 **Visual status indicators**

**Error State Example**:
```
❌ Validation Error
═══════════════════════════════════
Chemistry elements out of limits:
- Si: 2.95% (Max: 2.80%) ❌ HIGH
- Mn: 0.15% (Min: 0.20%) ❌ LOW

Cannot save. Heat requires rework.
```

#### Rework Entry
**Purpose**: Track rework operations for rejected heats
**Naming**: RW-.YYYY.-.####
**Key Fields**:
- Heat (Link)
- Rework Quantity
- Reason
- Corrective Action

**Visual Highlights**:
- 🔄 Rework tracking
- 📝 Reason documentation
- ✅ Corrective actions

---

### 6. Costing Screenshots

#### Furnace Power Cost
**Purpose**: Define power rates for cost calculation
**Naming**: Auto-named by furnace
**Key Fields**:
- Furnace (Link)
- Power Rate per KWH

**Visual Highlights**:
- ⚡ Power rate configuration
- 💰 Cost per unit tracking

#### Heat Costing
**Purpose**: Calculate total heat cost breakdown
**Naming**: Auto-named by heat
**Key Components**:
- Scrap Cost
- Alloy Cost
- Power Cost
- Total Cost
- Cost per Kg (auto-calculated)

**Cost Breakdown Display**:
```
Heat Costing: IF1-2026-001
═══════════════════════════════════

Scrap Cost:    ₹14,060.00  (87.5%)
Alloy Cost:    ₹1,198.00   (7.5%)
Power Cost:    ₹812.50     (5.0%)
─────────────────────────────
Total Cost:    ₹16,070.50
Cost per Kg:   ₹30.90

Visual Bar Chart:
Scrap  ████████████████  87.5%
Alloy  ██                 7.5%
Power  █                  5.0%
```

**Visual Highlights**:
- 💰 Cost aggregation
- 📊 Percentage breakdown
- 📈 Visual cost analysis
- ⚖️ Per kg cost calculation

---

## Feature Highlights

### 🌟 Top 10 Visual Features

1. **Furnace-Wise Heat Numbering**
   - Automatic naming: IF1-2026-001, IF2-2026-001, EAF1-2026-001
   - No manual intervention required
   - Prevents duplicate heat numbers

2. **Real-Time Yield Calculation**
   - Updates instantly as user types
   - Formula: (Good Qty / Actual Melt) × 100
   - Visual feedback for operators

3. **Chemistry Validation with Visual Indicators**
   - Green ✓ for within limits
   - Red ✗ for out of spec
   - Error messages with details

4. **Capacity Validation**
   - Prevents furnace overloading
   - Error popup if exceeded
   - Shows current vs maximum capacity

5. **Automatic Cost Aggregation**
   - Pulls costs from multiple sources
   - Calculates total automatically
   - Shows percentage breakdown

6. **Recovery Percentage Calculations**
   - Auto-fetches from Alloy Master
   - Calculates effective quantity
   - Updates in real-time

7. **Role-Based UI Customization**
   - Different views for different roles
   - Restricted access where needed
   - Tailored workflows per role

8. **Pattern Lifecycle Tracking**
   - Issue → Use → Return workflow
   - Condition assessment
   - Life count tracking

9. **Shift-Based Planning**
   - Morning/Afternoon/Night shifts
   - Furnace allocation per shift
   - Priority-based scheduling

10. **Submittable Workflows**
    - Draft → Submit states
    - Prevents accidental changes
    - Audit trail maintenance

---

## UI Components

### Form Elements

**Standard Fields**:
- ✏️ Text input (Data, Small Text)
- 🔢 Number input (Int, Float, Currency)
- 📅 Date/Datetime pickers
- ☑️ Checkboxes
- 🔽 Dropdowns (Select fields)
- 🔗 Link fields (to other DocTypes)

**Special Components**:
- 📋 Child tables (editable grids)
- 📊 Read-only calculated fields
- ⚠️ Validation messages
- 💡 Helper tooltips
- 🎨 Color-coded status badges

### List View Features

**Standard Features**:
- 🔍 Search bar
- 🎛️ Filter dropdowns
- 📄 Pagination
- 🔄 Sorting
- ⬇️ Export options

**Custom Features**:
- 🏷️ Furnace-based filtering
- 📅 Date range filters
- 🎯 Grade-based filtering
- 📊 Status indicators
- ⚡ Quick actions

### Color Scheme

**Status Colors**:
- 🟢 **Green**: Active, Accepted, Within limits, Success
- 🔴 **Red**: Inactive, Rejected, Out of spec, Errors
- 🟡 **Orange**: Pending, Draft, Warning
- 🔵 **Blue**: Information, Links, Selected
- ⚫ **Gray**: Disabled, Read-only, Archived

**Module Colors**:
- 🟠 **Foundry ERP**: Orange (#FF5733)
- 🎨 Consistent with ERPNext color palette

---

## Screenshot Specifications

### Recommended Settings

**Resolution**: 1920x1080 or higher  
**Format**: PNG (for clarity)  
**DPI**: 96 or higher  
**Browser**: Chrome/Firefox (latest version)  
**Zoom**: 100% (no browser zoom)

### Screenshot Types Needed

#### 1. Form Views
- ✅ Empty form (new entry)
- ✅ Filled form (with data)
- ✅ Submitted state
- ✅ Validation errors

#### 2. List Views
- ✅ Full list with filters
- ✅ Filtered results
- ✅ Empty state

#### 3. Dashboard/Workspace
- ✅ Module overview
- ✅ Desktop icon
- ✅ Quick access shortcuts

#### 4. Workflows
- ✅ Draft → Submit flow
- ✅ Approval flows (if any)

#### 5. Validations
- ✅ Success states
- ✅ Error states
- ✅ Warning states

---

## Workflow Diagrams

### Main Production Workflow

```
START
  ↓
[Setup Masters] (One-time)
  ↓
[Monthly Production Plan]
  ↓
[Daily Production Plan]
  ↓
[Pattern Issue]
  ↓
[Heat Entry] ←→ [Charge Mix]
  ↓              ↓
  ↓         [Alloy Addition]
  ↓              ↓
[Lab Analysis]   ↓
  ↓              ↓
  ├─ Pass ──→ [Heat Costing]
  │              ↓
  └─ Fail → [Rework] ──┘
                 ↓
            [Pattern Return]
                 ↓
               END
```

### Chemistry Validation Workflow

```
Lab Analysis Created
        ↓
Enter Chemistry Values
        ↓
System Fetches Limits from Chemistry Limits Master
        ↓
For Each Element: Compare Actual vs Min/Max
        ↓
    ┌───┴───┐
    ↓       ↓
 Within   Out of
 Limits   Range
    ↓       ↓
    ✓       ✗
    ↓       ↓
  Save   Error
 Success  Message
```

---

## Role-Based Views

### Furnace Operator View
**Access**:
- ✅ Create Heat Entry
- ✅ Create Charge Mix
- ✅ Create Alloy Addition
- ✅ Issue/Return Patterns
- 👁️ View Daily Plans
- ❌ Cannot modify masters
- ❌ Cannot access costing

### Quality Engineer View
**Access**:
- ✅ Create Lab Analysis
- ✅ Manage Chemistry Limits
- ✅ Create Rework Entries
- ✅ Manage Grade Masters
- 👁️ View Heat Entries
- ❌ Cannot create heats
- ❌ Cannot access costing

### Production Planner View
**Access**:
- ✅ Create Production Plans
- ✅ Manage All Masters
- ✅ Update Heat Entries
- ✅ Pattern Management
- 👁️ View all documents
- ❌ Cannot create Lab Analysis
- ❌ Limited costing access

### Costing Engineer View
**Access**:
- ✅ Create Heat Costing
- ✅ Manage Power Costs
- ✅ Manage Scrap/Alloy Masters
- 👁️ View all production data
- ❌ Cannot create heats
- ❌ Cannot create lab analysis

### Management View
**Access**:
- 👁️ **Read-Only** access to all modules
- 📊 Dashboard and reports
- 📈 Analytics (future)
- ❌ Cannot create/modify any document

---

## Quick Reference Table

| DocType | Module | Type | Naming | Key Feature |
|---------|--------|------|--------|-------------|
| Furnace Master | Masters | Master | By Code | Capacity validation |
| Material Type | Masters | Master | By Type | Foundation data |
| Grade Master | Masters | Master | By Code | Standards tracking |
| Chemistry Limits | Masters | Master | By Grade | Element ranges |
| Alloy Master | Masters | Master | By Name | Recovery % |
| Scrap Master | Masters | Master | By Name | Cost tracking |
| Casting Master | Masters | Master | By Code | Customer link |
| Pattern Master | Masters | Master | By Code | Life count |
| Pattern Issue | Pattern Mgmt | Transaction | PI-YYYY-#### | Issue tracking |
| Pattern Return | Pattern Mgmt | Transaction | PR-YYYY-#### | Condition assess |
| Monthly Plan | Planning | Transaction | MPP-YYYY-#### | Month targets |
| Daily Plan | Planning | Transaction | DPP-YYYY-#### | Shift schedule |
| **Heat Entry** | **Heat & Melt** | **Submittable** | **Furnace-YYYY-###** | **Core feature** |
| Charge Mix | Heat & Melt | Transaction | By Heat | Scrap tracking |
| Alloy Addition | Heat & Melt | Transaction | By Heat | Recovery calc |
| **Lab Analysis** | **Quality** | **Transaction** | **LAB-YYYY-####** | **Chem validation** |
| Rework Entry | Quality | Transaction | RW-YYYY-#### | Rework tracking |
| Power Cost | Costing | Master | By Furnace | Rate config |
| Heat Costing | Costing | Transaction | By Heat | Cost breakdown |

**Legend**:
- **Bold** = Key feature with advanced functionality
- Master = Reference/setup data
- Transaction = Operational data
- Submittable = Workflow with submit action

---

## Additional Resources

### Documentation Files
1. **README.md** - App overview and features
2. **INSTALLATION.md** - Setup and configuration guide
3. **SUMMARY.md** - Implementation details
4. **SCREENSHOTS.md** - Detailed visual guide (this file's companion)
5. **FEATURES_VISUAL_GUIDE.md** - This quick reference

### External Links
- ERPNext Documentation: https://docs.erpnext.com
- Frappe Framework Docs: https://frappeframework.com/docs
- Frappe Cloud: https://frappecloud.com

---

**Document Version**: 1.0  
**Created**: January 2026  
**For**: Foundry ERP v0.0.1  
**Framework**: ERPNext v15
