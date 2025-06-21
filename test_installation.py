#!/usr/bin/env python3
"""
Test script to verify FaviconX installation and dependencies.
"""

def test_imports():
    """Test if all required modules can be imported."""
    try:
        import click
        print("✅ Click imported successfully")
    except ImportError:
        print("❌ Click not found. Install with: pip install click")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow (PIL) imported successfully")
    except ImportError:
        print("❌ Pillow not found. Install with: pip install Pillow")
        return False
    
    try:
        import cairosvg
        print("✅ CairoSVG imported successfully")
    except ImportError:
        print("❌ CairoSVG not found. Install with: pip install cairosvg")
        return False
    
    try:
        from pathlib import Path
        print("✅ Pathlib imported successfully")
    except ImportError:
        print("❌ Pathlib not found (should be built-in)")
        return False
    
    return True

def test_faviconx_import():
    """Test if FaviconX can be imported."""
    try:
        from faviconx import FaviconGenerator, HTMLGenerator
        print("✅ FaviconX classes imported successfully")
        return True
    except ImportError as e:
        print(f"❌ FaviconX import failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing FaviconX installation...\n")
    
    # Test basic imports
    imports_ok = test_imports()
    print()
    
    # Test FaviconX import
    faviconx_ok = test_faviconx_import()
    print()
    
    if imports_ok and faviconx_ok:
        print("🎉 All tests passed! FaviconX is ready to use.")
        print("\nTo get started:")
        print("1. python faviconx.py <source_image> <output_directory>")
        print("2. python faviconx.py --help (for more options)")
    else:
        print("❌ Some tests failed. Please check the installation.")
        print("\nTo install dependencies:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    main() 