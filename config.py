"""
Configuration file for Face Recognition System
Automatically detects screen resolution and scales accordingly
"""

import tkinter as tk
from tkinter import ttk

class ScreenConfig:
    """Responsive screen configuration"""
    
    @staticmethod
    def get_screen_dimensions():
        """Get actual screen dimensions"""
        root = tk.Tk()
        root.withdraw()
        
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Deduct title bar (~30px) and taskbar (~40px)
        usable_width = screen_width
        usable_height = screen_height - 70
        
        root.destroy()
        return screen_width, screen_height, usable_width, usable_height
    
    @staticmethod
    def calculate_scaling():
        """Calculate scaling factor based on screen resolution"""
        screen_w, screen_h, usable_w, usable_h = ScreenConfig.get_screen_dimensions()
        
        # Base resolution: 1366x698 (Dell Latitude 7490)
        base_width = 1366
        base_height = 698
        
        # Calculate scaling factor
        scale_w = usable_w / base_width
        scale_h = usable_h / base_height
        scale_factor = min(scale_w, scale_h)
        
        return {
            'screen_width': usable_w,
            'screen_height': usable_h,
            'scale_factor': scale_factor,
            'base_width': base_width,
            'base_height': base_height
        }
    
    @staticmethod
    def get_font_size(base_size):
        """Calculate font size based on scaling"""
        config = ScreenConfig.calculate_scaling()
        scaled_size = int(base_size * config['scale_factor'])
        return max(scaled_size, 8)  # Minimum 8px
    
    @staticmethod
    def scale_dimension(dimension):
        """Scale any dimension based on screen resolution"""
        config = ScreenConfig.calculate_scaling()
        return int(dimension * config['scale_factor'])

# Initialize config
SCREEN_CONFIG = ScreenConfig.calculate_scaling()

# Font sizes (responsive)
TITLE_FONT_SIZE = ScreenConfig.get_font_size(26)
HEADING_FONT_SIZE = ScreenConfig.get_font_size(22)
BUTTON_FONT_SIZE = ScreenConfig.get_font_size(18)
LABEL_FONT_SIZE = ScreenConfig.get_font_size(10)
ENTRY_FONT_SIZE = ScreenConfig.get_font_size(9)
SMALL_FONT_SIZE = ScreenConfig.get_font_size(8)

# Colors
PRIMARY_COLOR = "#003366"
SECONDARY_COLOR = "#006600"
BUTTON_COLOR = "#0066CC"
DELETE_COLOR = "#CC0000"
SUCCESS_COLOR = "#00AA00"
BACKGROUND_COLOR = "white"
HEADER_BG = "white"

# Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Test@123"
DB_NAME = "face_recognizer"

# Face Recognition Configuration
CONFIDENCE_THRESHOLD = 70  # Threshold for face recognition
MIN_NEIGHBORS = 5  # Minimum neighbors for cascade classifier
SCALE_FACTOR = 1.1  # Scale factor for cascade classifier