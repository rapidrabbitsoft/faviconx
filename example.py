#!/usr/bin/env python3
"""
Example script demonstrating how to use FaviconX programmatically.
"""

from faviconx import FaviconGenerator, HTMLGenerator
import os

def main():
    """Example usage of FaviconX."""
    
    # Example paths
    source_image = "example-logo.png"  # Replace with your image path
    output_directory = "./example-output"
    
    # Check if source image exists
    if not os.path.exists(source_image):
        print(f"❌ Source image '{source_image}' not found!")
        print("Please create or provide a valid image file.")
        return
    
    try:
        # Generate favicons
        print("🎨 Generating favicons...")
        generator = FaviconGenerator(source_image, output_directory)
        generator.generate_all_favicons()
        
        # Generate HTML files
        print("\n📄 Generating HTML files...")
        html_generator = HTMLGenerator(output_directory)
        html_generator.generate_html()
        html_generator.generate_webmanifest()
        
        print(f"\n✅ Example complete!")
        print(f"📁 Check the '{output_directory}' folder for generated files")
        print(f"🌐 Open '{output_directory}/index.html' in your browser to test")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 