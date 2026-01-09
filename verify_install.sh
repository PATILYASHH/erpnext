#!/bin/bash

# Foundry ERP - Installation Verification Script
# This script verifies that Foundry ERP structure is valid

echo "============================================================="
echo "FOUNDRY ERP - STRUCTURE VERIFICATION"
echo "============================================================="
echo ""

# Check current directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ ERROR: pyproject.toml not found"
    echo "   Please run this script from the foundry_erp app directory"
    exit 1
fi

echo "✅ Running from foundry_erp directory"
echo ""

# Verify app structure
echo "Checking app structure..."

required_files=(
    "foundry_erp/foundry_erp/__init__.py"
    "foundry_erp/foundry_erp/hooks.py"
    "foundry_erp/foundry_erp/modules.txt"
    "pyproject.toml"
    "foundry_erp/setup.py"
)

all_found=true
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ Missing: $file"
        all_found=false
    fi
done

if [ "$all_found" = false ]; then
    echo ""
    echo "❌ ERROR: Required files missing"
    exit 1
fi

echo ""
echo "✅ All required files present"
echo ""

# Check Python syntax
echo "Checking Python syntax..."
python3 -m py_compile foundry_erp/foundry_erp/__init__.py foundry_erp/foundry_erp/hooks.py foundry_erp/setup.py 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Python syntax valid"
else
    echo "❌ Python syntax errors found"
    exit 1
fi
echo ""

# Verify app configuration
echo "Verifying app configuration..."
python3 << 'PYTHON_EOF'
import sys
sys.path.insert(0, '.')

try:
    from foundry_erp.foundry_erp import hooks
    
    # Check app name
    if hooks.app_name == "foundry_erp":
        print("  ✅ app_name: foundry_erp")
    else:
        print(f"  ❌ app_name: {hooks.app_name} (expected: foundry_erp)")
        sys.exit(1)
    
    # Check required apps
    required = hooks.required_apps
    if "frappe" in required and "erpnext" in required:
        print(f"  ✅ required_apps: {required}")
    else:
        print(f"  ❌ required_apps: {required} (should include frappe and erpnext)")
        sys.exit(1)
    
    # Check app title
    if hasattr(hooks, 'app_title'):
        print(f"  ✅ app_title: {hooks.app_title}")
    
    print("\n✅ App configuration valid")
    
except Exception as e:
    print(f"❌ Error loading app configuration: {e}")
    sys.exit(1)
PYTHON_EOF

if [ $? -ne 0 ]; then
    exit 1
fi

echo ""
echo "============================================================="
echo "✅ VERIFICATION COMPLETE"
echo "============================================================="
echo ""
echo "The app structure is valid and ready for installation."
echo ""
echo "To install this app on a Frappe bench, run:"
echo "  cd ~/frappe-bench"
echo "  bench get-app /path/to/foundry_erp"
echo "  bench --site <site-name> install-app foundry_erp"
echo ""
echo "Or clone directly into apps directory:"
echo "  cd ~/frappe-bench/apps"
echo "  git clone https://github.com/PATILYASHH/foundry_erp"
echo "  bench --site <site-name> install-app foundry_erp"
echo ""
echo "⚠️  IMPORTANT: Make sure ERPNext is installed on your site first!"
echo ""
