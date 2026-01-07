# Foundry ERP - Visual Feature Guide & Screenshots Documentation

This document provides detailed visual descriptions and mockups of the new features added to the Foundry ERP application. Since this is a custom ERPNext app, all screenshots would be taken from the ERPNext web interface after installation.

## Table of Contents

1. [Module Overview](#module-overview)
2. [Master Data Management](#master-data-management)
3. [Production Planning](#production-planning)
4. [Heat & Melting Operations](#heat--melting-operations)
5. [Quality & Chemistry Control](#quality--chemistry-control)
6. [Pattern Management](#pattern-management)
7. [Costing Features](#costing-features)
8. [Workflow Diagrams](#workflow-diagrams)

---

## Module Overview

### Desktop View - Foundry ERP Module Icon

**What the screenshot would show:**
- ERPNext desktop interface with a new "Foundry ERP" icon
- Icon color: Orange (#FF5733) with factory/industry symbol
- Located in the desktop shortcuts area alongside other ERPNext modules
- Clicking this icon opens the Foundry ERP workspace

**Key Elements:**
```
┌────────────────────────────────────────────┐
│  ERPNext Desktop                           │
│                                            │
│  [Home] [HR] [Accounting] [Manufacturing]  │
│                                            │
│  ┌──────────┐  ┌──────────┐              │
│  │ 🏭       │  │  Other   │              │
│  │ Foundry  │  │  Module  │              │
│  │   ERP    │  │          │              │
│  └──────────┘  └──────────┘              │
│                                            │
└────────────────────────────────────────────┘
```

### Foundry ERP Workspace

**What the screenshot would show:**
- Main workspace with 7 module sections:
  1. Masters
  2. Pattern Management
  3. Production Planning
  4. Heat & Melting
  5. Quality & Chemistry
  6. Costing
  7. Reports & Dashboard
- Each section displays shortcuts to relevant DocTypes
- Clean, organized layout following ERPNext design patterns

---

## Master Data Management

### 1. Furnace Master List View

**Screenshot Description:**
A list view showing all configured furnaces in the foundry with the following columns:

| Furnace Code | Furnace Name | Type | Capacity (Kg) | Power (KW) | Status |
|--------------|--------------|------|---------------|------------|---------|
| IF1 | Induction Furnace 1 | IF | 5000 | 250 | Active |
| IF2 | Induction Furnace 2 | IF | 3000 | 200 | Active |
| EAF1 | Electric Arc Furnace 1 | EAF | 10000 | 500 | Active |
| CUP1 | Cupola Furnace 1 | Cupola | 8000 | - | Maintenance |

**Key Features Visible:**
- Add new furnace button (+ New)
- Filter and search functionality
- Quick access to edit/view each furnace
- Color-coded status indicators (Green = Active, Red = Maintenance)

### 2. Furnace Master Form View

**Screenshot Description:**
A detailed form showing all fields for a furnace:

```
Furnace Master: IF1
─────────────────────────────────────────

Basic Information
┌─────────────────────────────────────────┐
│ Furnace Code:    IF1                    │
│ Furnace Name:    Induction Furnace 1    │
│ Furnace Type:    [IF ▼]                 │
│                  Options: IF, EAF, Cupola│
└─────────────────────────────────────────┘

Capacity & Power
┌─────────────────────────────────────────┐
│ Capacity (Kg):   5000.00                │
│ Power Rating:    250.00 KW              │
└─────────────────────────────────────────┘

Status & Notes
┌─────────────────────────────────────────┐
│ Status:          [Active ▼]             │
│ Remarks:         Recently serviced      │
└─────────────────────────────────────────┘

[Save] [Cancel]
```

### 3. Grade Master with Chemistry Limits

**Screenshot Description:**
A form showing grade specifications with a child table for chemistry limits:

```
Grade Master: SG500-7
─────────────────────────────────────────

Grade Details
┌─────────────────────────────────────────┐
│ Grade Code:      SG500-7                │
│ Material Type:   SG (Spheroidal Graphite)│
│ Standard:        [IS ▼]                 │
│ CE Formula:      %C + %Si/3             │
│ Active:          ☑                       │
└─────────────────────────────────────────┘
```

### 4. Chemistry Limits Master

**Screenshot Description:**
Shows the chemistry specification limits for a grade with a detailed child table:

```
Chemistry Limits Master: SG500-7
─────────────────────────────────────────

Grade: SG500-7

Chemistry Element Limits
┌──────────────────────────────────────────────────────┐
│ Element │ Min Value (%) │ Max Value (%) │            │
├──────────────────────────────────────────────────────┤
│ C       │ 3.40          │ 3.80          │ [Edit]     │
│ Si      │ 2.20          │ 2.80          │ [Edit]     │
│ Mn      │ 0.20          │ 0.50          │ [Edit]     │
│ P       │ 0.00          │ 0.05          │ [Edit]     │
│ S       │ 0.00          │ 0.02          │ [Edit]     │
│ Mg      │ 0.03          │ 0.06          │ [Edit]     │
│ Cu      │ 0.00          │ 0.80          │ [Edit]     │
└──────────────────────────────────────────────────────┘

[Add Row] [Save] [Cancel]
```

**Key Features:**
- Defines acceptable ranges for each chemical element
- Used for automatic validation in Lab Analysis
- Prevents out-of-spec production

### 5. Material Type, Alloy, and Scrap Masters

**Screenshot Description (Material Type List):**

| Material Type | Description | Active |
|---------------|-------------|--------|
| Steel | Steel castings and forgings | ✓ |
| SG | Spheroidal Graphite Iron (Ductile Iron) | ✓ |
| CI | Cast Iron (Grey Iron) | ✓ |

**Screenshot Description (Alloy Master):**

| Alloy Name | Element | Recovery % | Cost per Kg |
|------------|---------|------------|-------------|
| FeSi-75 | Si | 72.0 | ₹85.00 |
| FeMn-70 | Mn | 68.0 | ₹95.00 |
| Mg-Alloy | Mg | 45.0 | ₹250.00 |
| FeNi | Ni | 95.0 | ₹180.00 |

**Screenshot Description (Scrap Master):**

| Scrap Name | Material Type | Cost per Kg |
|------------|---------------|-------------|
| Heavy Scrap | Steel | ₹25.00 |
| Boring Scrap | Steel | ₹28.00 |
| SG Returns | SG | ₹32.00 |
| Pig Iron | SG | ₹35.00 |

### 6. Casting and Pattern Masters

**Screenshot Description (Casting Master):**

```
Casting Master: CAST-1001
─────────────────────────────────────────

Casting Details
┌─────────────────────────────────────────┐
│ Casting Code:    CAST-1001              │
│ Customer:        ABC Industries Ltd     │
│ Weight/Piece:    25.50 Kg               │
│ Grade:           SG500-7                │
│ Active:          ☑                       │
└─────────────────────────────────────────┘

Description
┌─────────────────────────────────────────┐
│ Brake Disc Casting - Automotive         │
│ Drawing No: BD-2024-001                 │
└─────────────────────────────────────────┘
```

**Screenshot Description (Pattern Master):**

```
Pattern Master: PAT-BD-001
─────────────────────────────────────────

Pattern Information
┌─────────────────────────────────────────┐
│ Pattern Code:    PAT-BD-001             │
│ Casting:         CAST-1001              │
│ Ownership:       [Customer ▼]           │
│ Storage Loc:     Rack-A-15              │
│ Condition:       [Good ▼]               │
│ Life Count:      245 uses               │
└─────────────────────────────────────────┘
```

---

## Production Planning

### 7. Monthly Production Plan

**Screenshot Description:**
A comprehensive monthly planning interface with target quantities:

```
Monthly Production Plan: MPP-2026-001
─────────────────────────────────────────

Planning Period
┌─────────────────────────────────────────┐
│ Month:           January 2026           │
│ Year:            2026                   │
│ Status:          Draft                  │
└─────────────────────────────────────────┘

Production Items
┌──────────────────────────────────────────────────────────────┐
│ Casting      │ Grade    │ Target Qty │ Heats │ Remarks      │
├──────────────────────────────────────────────────────────────┤
│ CAST-1001    │ SG500-7  │ 5000 Kg    │ 10    │ High priority│
│ CAST-1002    │ Steel-20 │ 8000 Kg    │ 12    │              │
│ CAST-1003    │ SG500-7  │ 3000 Kg    │ 6     │              │
└──────────────────────────────────────────────────────────────┘

Total Target: 16,000 Kg across 28 heats

[Submit] [Save as Draft] [Cancel]
```

### 8. Daily Production Plan

**Screenshot Description:**
Daily shift-wise production schedule:

```
Daily Production Plan: DPP-2026-01-15
─────────────────────────────────────────

Schedule Details
┌─────────────────────────────────────────┐
│ Date:            15-01-2026             │
│ Shift:           [Morning ▼]            │
│ Furnace:         IF1                    │
└─────────────────────────────────────────┘

Planned Items
┌──────────────────────────────────────────────────────────────┐
│ Casting      │ Grade    │ Planned Qty│ Heat No  │ Priority  │
├──────────────────────────────────────────────────────────────┤
│ CAST-1001    │ SG500-7  │ 500 Kg     │ IF1-001  │ 1         │
│ CAST-1002    │ Steel-20 │ 650 Kg     │ IF1-002  │ 2         │
└──────────────────────────────────────────────────────────────┘

Operator: [John Doe ▼]

[Submit] [Save] [Cancel]
```

---

## Heat & Melting Operations

### 9. Heat Entry Form - Main Feature

**Screenshot Description:**
The core DocType for recording heat operations with real-time validations:

```
Heat Entry: IF1-2026-001                    [DRAFT]
─────────────────────────────────────────────────────

Heat Details
┌─────────────────────────────────────────┐
│ Furnace:         [IF1 ▼]                │
│ Date & Time:     15-01-2026 08:30 AM    │
│ Grade:           [SG500-7 ▼]            │
│ Material Type:   SG (auto-fetched)      │
└─────────────────────────────────────────┘

Quantities (in Kg)
┌─────────────────────────────────────────┐
│ Planned Qty:     500.00                 │
│ Actual Melt:     520.00                 │
│ Good Qty:        485.00                 │
│ Rejection Qty:   35.00                  │
│                                         │
│ Yield %:         93.27% (auto-calc)     │
└─────────────────────────────────────────┘

Status
┌─────────────────────────────────────────┐
│ Heat Status:     [Open ▼]               │
└─────────────────────────────────────────┘

[Submit] [Save] [Cancel]
```

**Key Features Visible:**
- **Furnace-wise naming**: Notice "IF1-2026-001" - automatically assigned based on furnace
- **Auto-calculation**: Yield % updates in real-time as quantities change
- **Validation**: If actual melt exceeds furnace capacity, error is shown
- **Material fetch**: Material type auto-populated from selected grade

**Error Example Screenshot:**
```
❌ Validation Error
─────────────────────────────────────────
Actual Melt Qty (5500 Kg) exceeds 
furnace capacity (5000 Kg) for IF1

[OK]
```

### 10. Heat Entry - Client-Side Calculations

**Screenshot Description:**
Shows the real-time JavaScript calculations in action:

```
When user enters:
Actual Melt Qty:  500.00 Kg
Rejection Qty:    25.00 Kg

Automatically calculates:
Good Qty:         475.00 Kg  ← Auto-filled
Yield %:          95.00%     ← Auto-calculated
```

**Visual Indicator:**
- Fields that auto-calculate are shown with a light background
- Instant updates without page refresh
- Helpful for operators to see yield in real-time

### 11. Charge Mix Entry

**Screenshot Description:**
Recording raw materials (scrap) used in the heat:

```
Charge Mix: IF1-2026-001
─────────────────────────────────────────

Heat: IF1-2026-001
Total Charge: 520.00 Kg (auto-calculated)

Charge Items
┌──────────────────────────────────────────────────────────────┐
│ Scrap Type    │ Qty (Kg)  │ Cost (₹)  │                     │
├──────────────────────────────────────────────────────────────┤
│ Heavy Scrap   │ 300.00    │ 7,500.00  │ [Edit] [Remove]     │
│ Boring Scrap  │ 120.00    │ 3,360.00  │ [Edit] [Remove]     │
│ SG Returns    │ 100.00    │ 3,200.00  │ [Edit] [Remove]     │
└──────────────────────────────────────────────────────────────┘

Total Cost: ₹14,060.00

[Add Row] [Save] [Cancel]
```

### 12. Alloy Addition Entry

**Screenshot Description:**
Recording alloys added with recovery calculations:

```
Alloy Addition: IF1-2026-001
─────────────────────────────────────────

Heat: IF1-2026-001
Total Alloy: 12.50 Kg (auto-calculated)

Alloy Items
┌────────────────────────────────────────────────────────────────────────┐
│ Alloy      │ Qty (Kg) │ Recovery % │ Effective Qty │                  │
├────────────────────────────────────────────────────────────────────────┤
│ FeSi-75    │ 8.00     │ 72.0       │ 5.76 Kg       │ [Edit] [Remove]  │
│ FeMn-70    │ 4.50     │ 68.0       │ 3.06 Kg       │ [Edit] [Remove]  │
└────────────────────────────────────────────────────────────────────────┘

Total Effective Addition: 8.82 Kg

[Add Row] [Save] [Cancel]
```

**Key Feature:**
- Recovery percentage automatically fetched from Alloy Master
- Effective quantity auto-calculated: Qty × (Recovery % / 100)

---

## Quality & Chemistry Control

### 13. Lab Analysis Entry - Chemistry Validation

**Screenshot Description:**
The most advanced feature showing automatic chemistry validation:

```
Lab Analysis Entry: LAB-2026-001
─────────────────────────────────────────

Analysis Details
┌─────────────────────────────────────────┐
│ Heat:            IF1-2026-001           │
│ Sample No:       S-001                  │
│ Date:            15-01-2026 11:00 AM    │
│ Analyst:         Lab Tech - Ramesh      │
└─────────────────────────────────────────┘

Chemistry Results
┌────────────────────────────────────────────────────────────────────────┐
│ Element │ Actual │ Min Limit │ Max Limit │ Within Limit │ Status      │
├────────────────────────────────────────────────────────────────────────┤
│ C       │ 3.65   │ 3.40      │ 3.80      │ ☑            │ ✓ OK        │
│ Si      │ 2.45   │ 2.20      │ 2.80      │ ☑            │ ✓ OK        │
│ Mn      │ 0.35   │ 0.20      │ 0.50      │ ☑            │ ✓ OK        │
│ P       │ 0.03   │ 0.00      │ 0.05      │ ☑            │ ✓ OK        │
│ S       │ 0.01   │ 0.00      │ 0.02      │ ☑            │ ✓ OK        │
│ Mg      │ 0.04   │ 0.03      │ 0.06      │ ☑            │ ✓ OK        │
└────────────────────────────────────────────────────────────────────────┘

Overall Status: ✓ ACCEPTED

[Save] [Submit] [Cancel]
```

**Key Features:**
1. **Automatic Limit Fetch**: Min/Max values auto-populated from Chemistry Limits Master
2. **Real-time Validation**: Within Limit checkbox auto-checked/unchecked
3. **Visual Indicators**: Green checkmarks for OK, red X for out-of-spec
4. **Status Auto-set**: Overall status determined by validation results

### 14. Lab Analysis Entry - Out of Spec Example

**Screenshot Description:**
Shows what happens when chemistry is out of specification:

```
Lab Analysis Entry: LAB-2026-002
─────────────────────────────────────────

Chemistry Results
┌────────────────────────────────────────────────────────────────────────┐
│ Element │ Actual │ Min Limit │ Max Limit │ Within Limit │ Status      │
├────────────────────────────────────────────────────────────────────────┤
│ C       │ 3.65   │ 3.40      │ 3.80      │ ☑            │ ✓ OK        │
│ Si      │ 2.95   │ 2.20      │ 2.80      │ ☐            │ ❌ HIGH     │
│ Mn      │ 0.15   │ 0.20      │ 0.50      │ ☐            │ ❌ LOW      │
│ P       │ 0.03   │ 0.00      │ 0.05      │ ☑            │ ✓ OK        │
└────────────────────────────────────────────────────────────────────────┘

❌ Validation Error
─────────────────────────────────────────
Chemistry elements out of specified limits:
- Si: 2.95% (Max: 2.80%)
- Mn: 0.15% (Min: 0.20%)

Cannot save. Heat requires rework.

[OK]
```

**Impact:**
- Prevents saving of out-of-spec results
- Forces corrective action (rework or rejection)
- Ensures quality control compliance

### 15. Rework Entry

**Screenshot Description:**
Recording rework operations for rejected heats:

```
Rework Entry: RW-2026-001
─────────────────────────────────────────

Rework Details
┌─────────────────────────────────────────┐
│ Heat:            IF1-2026-002           │
│ Rework Qty:      520.00 Kg              │
│ Date:            15-01-2026 02:00 PM    │
└─────────────────────────────────────────┘

Reason for Rework
┌─────────────────────────────────────────┐
│ Silicon content high (2.95%)            │
│ Manganese content low (0.15%)           │
│                                         │
│ Corrective Action:                      │
│ Added FeMn-70 alloy and remelted        │
└─────────────────────────────────────────┘

[Save] [Cancel]
```

---

## Pattern Management

### 16. Pattern Issue

**Screenshot Description:**
Tracking pattern movement to production floor:

```
Pattern Issue: PI-2026-001
─────────────────────────────────────────

Issue Details
┌─────────────────────────────────────────┐
│ Pattern:         PAT-BD-001             │
│ Casting:         CAST-1001              │
│ Issue Date:      15-01-2026             │
│ Issued To:       Molding Dept           │
│ Issued By:       Store Keeper           │
│ Quantity:        1 set                  │
└─────────────────────────────────────────┘

Purpose
┌─────────────────────────────────────────┐
│ Production order PO-2026-015            │
│ Estimated uses: 50 castings             │
└─────────────────────────────────────────┘

[Submit] [Save] [Cancel]
```

### 17. Pattern Return

**Screenshot Description:**
Recording pattern return with condition assessment:

```
Pattern Return: PR-2026-001
─────────────────────────────────────────

Return Details
┌─────────────────────────────────────────┐
│ Pattern:         PAT-BD-001             │
│ Issue Ref:       PI-2026-001            │
│ Return Date:     17-01-2026             │
│ Returned By:     Molding Supervisor     │
│ Actual Uses:     48 castings            │
└─────────────────────────────────────────┘

Condition Assessment
┌─────────────────────────────────────────┐
│ Condition:       [Good ▼]               │
│                  Options: Good, Repair,  │
│                           Scrap          │
│                                         │
│ Remarks:         Minor wear on edges,   │
│                  suitable for continued  │
│                  use. Clean and store.   │
└─────────────────────────────────────────┘

[Submit] [Save] [Cancel]
```

---

## Costing Features

### 18. Furnace Power Cost

**Screenshot Description:**
Defining power rates for cost calculation:

```
Furnace Power Cost: IF1
─────────────────────────────────────────

Cost Configuration
┌─────────────────────────────────────────┐
│ Furnace:         IF1                    │
│ Power Rate:      ₹6.50 per KWH         │
│                                         │
│ Effective From:  01-01-2026             │
└─────────────────────────────────────────┘

Notes
┌─────────────────────────────────────────┐
│ Industrial tariff rate                  │
│ Includes demand charges                 │
└─────────────────────────────────────────┘

[Save] [Cancel]
```

### 19. Heat Costing

**Screenshot Description:**
Comprehensive cost breakdown for a heat:

```
Heat Costing: IF1-2026-001
─────────────────────────────────────────

Heat: IF1-2026-001
Grade: SG500-7
Actual Melt Qty: 520.00 Kg

Cost Breakdown
┌─────────────────────────────────────────┐
│ Scrap Cost:      ₹14,060.00             │
│ Alloy Cost:      ₹1,198.00              │
│ Power Cost:      ₹812.50                │
│ ─────────────────────────────────       │
│ Total Cost:      ₹16,070.50             │
│                                         │
│ Cost per Kg:     ₹30.90                 │
└─────────────────────────────────────────┘

Cost Analysis
┌─────────────────────────────────────────┐
│ Scrap:     87.5%  ████████████████      │
│ Alloy:      7.5%  ██                    │
│ Power:      5.0%  █                     │
└─────────────────────────────────────────┘

[Generate Report] [Save] [Cancel]
```

**Features:**
- Automatic cost aggregation from Charge Mix and Alloy Addition
- Power cost calculated based on furnace power rating and time
- Per kg cost helps in pricing decisions

---

## Workflow Diagrams

### 20. Complete Production Workflow Diagram

**Visual Flowchart Screenshot:**

```
┌─────────────────┐
│  Setup Masters  │
│  (One-time)     │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Monthly Plan    │──┐
│ (MPP-2026-001)  │  │
└─────────────────┘  │
                     │
         ┌───────────┘
         v
┌─────────────────┐
│  Daily Plan     │
│ (DPP-2026-...)  │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Issue Pattern  │
│  (PI-2026-...)  │
└────────┬────────┘
         │
         v
┌─────────────────┐     ┌─────────────────┐
│   Heat Entry    │────>│   Charge Mix    │
│ (IF1-2026-001)  │     │ (Scrap details) │
└────────┬────────┘     └─────────────────┘
         │
         v
┌─────────────────┐
│ Alloy Addition  │
│ (FeSi, FeMn)    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Lab Analysis    │──── Failed ───> Rework Entry
│ (Chemistry)     │                 (RW-2026-...)
└────────┬────────┘                       │
         │                                 │
      Passed                               │
         │                                 │
         v                                 │
┌─────────────────┐                       │
│  Heat Costing   │<──────────────────────┘
│ (Cost analysis) │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Return Pattern  │
│ (PR-2026-...)   │
└─────────────────┘
```

### 21. Chemistry Validation Flow

**Visual Process Screenshot:**

```
Lab Analysis Entry Created
         │
         v
┌─────────────────────────────────────┐
│ User enters actual chemistry values │
└────────┬────────────────────────────┘
         │
         v
┌─────────────────────────────────────┐
│ System fetches limits from          │
│ Chemistry Limits Master for grade   │
└────────┬────────────────────────────┘
         │
         v
┌─────────────────────────────────────┐
│ For each element:                   │
│ IF (min <= actual <= max)           │
│   THEN within_limit = True ✓        │
│   ELSE within_limit = False ✗       │
└────────┬────────────────────────────┘
         │
         v
┌─────────────────────────────────────┐
│ IF any element out of range         │
│   THEN throw validation error       │
│   ELSE allow save and set status    │
└─────────────────────────────────────┘
```

### 22. Role-Based Access Control

**Screenshot Description:**
Permission matrix showing what each role can access:

```
DocType Permissions Matrix
════════════════════════════════════════════════════════

                    Furnace  Quality  Production  Costing  Management
DocType             Operator Engineer Planner     Engineer (Read-only)
─────────────────────────────────────────────────────────────────────
Furnace Master        R        R        CRUD        R          R
Grade Master          R        CRUD     CRUD        R          R
Chemistry Limits      R        CRUD     R           R          R
Heat Entry            CRUDS    R        RU          R          R
Lab Analysis          R        CRUDS    R           R          R
Charge Mix            CRUD     R        R           R          R
Alloy Addition        CRUD     R        R           R          R
Heat Costing          R        R        R           CRUD       R
Pattern Issue         CRUD     R        CRUD        R          R
Pattern Return        CRUD     R        CRUD        R          R

Legend:
C = Create, R = Read, U = Update, D = Delete, S = Submit
```

---

## Additional Visual Elements

### 23. Dashboard Widgets (Future Enhancement)

**Mockup Screenshot:**
```
┌────────────────────────────────────────────────────────────┐
│  Foundry ERP Dashboard                                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ Today's      │  │ Pending      │  │ Quality      │   │
│  │ Production   │  │ Heats        │  │ Acceptance   │   │
│  │              │  │              │  │              │   │
│  │  12 Heats    │  │   3 Heats    │  │    95.5%     │   │
│  │  6,250 Kg    │  │              │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ Heat Production Trend (Last 7 Days)                 │  │
│  │                                            ●         │  │
│  │                                    ●                 │  │
│  │                            ●                         │  │
│  │                    ●                                 │  │
│  │            ●                                         │  │
│  │    ●                                                 │  │
│  │                                                      │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                            │
│  ┌───────────────────────────┐  ┌─────────────────────┐  │
│  │ Furnace Utilization       │  │ Top Grades Produced │  │
│  │                           │  │                     │  │
│  │ IF1:  ████████░░ 85%     │  │ 1. SG500-7  45%     │  │
│  │ IF2:  ██████░░░░ 62%     │  │ 2. Steel-20 30%     │  │
│  │ EAF1: ██████████ 95%     │  │ 3. SG400-12 15%     │  │
│  │                           │  │ 4. Others   10%     │  │
│  └───────────────────────────┘  └─────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### 24. List View with Filters

**Screenshot Description:**
Heat Entry list with advanced filtering:

```
Heat Entry List
───────────────────────────────────────────────────────────

Filters:  [Furnace: All ▼] [Grade: All ▼] [Status: All ▼]
          [Date Range: Last 7 Days ▼]

┌─────────────────────────────────────────────────────────────────────┐
│ Heat No     │ Date       │ Furnace │ Grade    │ Qty   │ Yield % │   │
├─────────────────────────────────────────────────────────────────────┤
│ IF1-2026-005│ 20-01-2026 │ IF1     │ SG500-7  │ 520Kg │ 93.5%   │✓  │
│ IF1-2026-004│ 19-01-2026 │ IF1     │ Steel-20 │ 480Kg │ 91.2%   │✓  │
│ IF2-2026-003│ 19-01-2026 │ IF2     │ SG500-7  │ 350Kg │ 94.8%   │✓  │
│ EAF1-2026-002│18-01-2026 │ EAF1    │ Steel-20 │ 950Kg │ 89.5%   │✓  │
│ IF1-2026-003│ 18-01-2026 │ IF1     │ SG400-12 │ 500Kg │ 92.0%   │✓  │
└─────────────────────────────────────────────────────────────────────┘

Showing 5 of 127 records | [Previous] [1] [2] [3] ... [Next]
```

---

## Summary of Visual Features

### New Features Demonstrated:

1. **7 Modules** - Complete foundry management suite
2. **26 DocTypes** - Comprehensive data structures
3. **Furnace-wise Naming** - Automatic heat numbering (IF1-2026-001, IF2-2026-001)
4. **Real-time Calculations** - Yield percentage, effective alloy quantities
5. **Automatic Validations** - Furnace capacity, chemistry limits
6. **Role-based Access** - 5 custom roles with granular permissions
7. **Chemistry Validation** - Automated quality control with limits checking
8. **Cost Tracking** - Complete cost breakdown per heat
9. **Pattern Lifecycle** - Issue and return tracking
10. **Production Planning** - Monthly and daily planning tools

### Color Coding Used in ERPNext Interface:

- **Green**: Accepted, Active, Within limits
- **Red**: Rejected, Out of spec, Errors
- **Orange**: Pending, Draft
- **Blue**: Information, Links
- **Gray**: Inactive, Disabled

### Responsive Design:

All forms and lists are responsive and work on:
- Desktop browsers (recommended)
- Tablets
- Mobile devices (limited functionality)

---

## How to Capture These Screenshots

Once the app is installed on an ERPNext instance:

1. **Login** as Administrator
2. **Navigate** to Foundry ERP module
3. **Create sample data** for each master
4. **Execute workflows** (create heat entry, lab analysis, etc.)
5. **Capture screenshots** using:
   - Browser screenshot tools (F12 > Ctrl+Shift+P > "Screenshot")
   - Screen capture software (Snipping Tool, Snagit, etc.)
   - Browser extensions (Awesome Screenshot, etc.)

6. **Recommended screenshot resolution**: 1920x1080 or higher
7. **Format**: PNG for clarity
8. **Annotations**: Add arrows, highlights using tools like:
   - Skitch
   - Snagit
   - PowerPoint

---

## Notes for Documentation Team

- All screenshots should show **realistic data** (not "test" or "dummy")
- Include **both successful and error states** for validation features
- Demonstrate **user interactions** (form filling, dropdown selections)
- Show **before and after** states for calculations
- Highlight **key features** with annotations
- Include **workflow diagrams** alongside screenshots
- Maintain **consistent styling** across all images
- Use **high-resolution** images for print documentation

---

**Document Version**: 1.0  
**Last Updated**: January 2026  
**Created for**: Foundry ERP v0.0.1  
**ERPNext Version**: v15
