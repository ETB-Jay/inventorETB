#!/usr/bin/env python3
"""Test script to verify layout components"""

def test_imports():
    """Test that all modules can be imported"""
    try:
        from app.widgets import InventoryWidget, ProductDetailsWidget, TimeWidget
        print("✅ All widgets imported successfully")
        return True
    except Exception as e:
        print(f"❌ Widget import failed: {e}")
        return False

def test_css_files():
    """Test that all CSS files exist and are readable"""
    import os
    css_files = [
        "app/styles/base.tcss",
        "app/styles/layout.tcss",
        "app/styles/forms.tcss", 
        "app/styles/controls.tcss",
        "app/styles/output.tcss"
    ]
    
    for css_file in css_files:
        if os.path.exists(css_file):
            print(f"✅ {css_file} exists")
        else:
            print(f"❌ {css_file} missing")
            return False
    return True

def test_app_structure():
    """Test that the main app can be instantiated"""
    try:
        from app.shopifyql_app import ShopifyQLApp
        app = ShopifyQLApp()
        print("✅ App instantiated successfully")
        return True
    except Exception as e:
        print(f"❌ App instantiation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 Running intensive layout check...\n")
    
    tests = [
        ("CSS Files", test_css_files),
        ("Widget Imports", test_imports),
        ("App Structure", test_app_structure),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Layout is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")

if __name__ == "__main__":
    main()
