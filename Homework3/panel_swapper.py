import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME
from operation_panels_hw1 import create_hw1_panel
from operation_panels_hw2 import create_hw2_panel
from operation_panels_hw3 import create_hw3_panel

if TYPE_CHECKING:
    from app import ImageProcessorApp

class PanelSwapper:
    def __init__(self, app: 'ImageProcessorApp', container: tk.Frame):
        self.app = app
        self.container = container
        self.panels = {}

        # Create swap buttons
        button_frame = tk.Frame(container, bg=MAIN_THEME)
        button_frame.pack(side=tk.TOP, fill=tk.X)
        tk.Button(button_frame, text="HW1", command=lambda: self.show_panel("HW1")).pack(side=tk.LEFT)
        tk.Button(button_frame, text="HW2", command=lambda: self.show_panel("HW2")).pack(side=tk.LEFT)
        tk.Button(button_frame, text="HW3", command=lambda: self.show_panel("HW3")).pack(side=tk.LEFT)

        # Initialize panels, using only `pack` for each panel in the container
        self.panels["HW1"] = create_hw1_panel(app, container)
        self.panels["HW2"] = create_hw2_panel(app, container)
        self.panels["HW3"] = create_hw3_panel(app, container)

    def show_panel(self, panel_name):
        """
        Shows the selected panel and hides others.
        """
        for panel in self.panels.values():
            panel.pack_forget()
        self.panels[panel_name].pack(fill=tk.BOTH, expand=True)
