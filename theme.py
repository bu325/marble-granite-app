from kivymd.theming import ThemeManager
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase

# Register Arabic fonts
LabelBase.register(name="Amiri", fn_regular="assets/fonts/Amiri-Regular.ttf")
LabelBase.register(name="Cairo", fn_regular="assets/fonts/Cairo-Regular.ttf")

# Custom theme configuration
def setup_theme(app):
    app.theme_cls.primary_palette = "BlueGray"
    app.theme_cls.accent_palette = "Blue"
    app.theme_cls.theme_style = "Light"
    
    # Set default font to Arabic
    app.theme_cls.font_styles["H1"] = ["Amiri", 96, False, 0.15]
    app.theme_cls.font_styles["H2"] = ["Amiri", 60, False, 0.15]
    app.theme_cls.font_styles["H3"] = ["Amiri", 48, False, 0]
    app.theme_cls.font_styles["H4"] = ["Amiri", 34, False, 0.25]
    app.theme_cls.font_styles["H5"] = ["Amiri", 24, False, 0]
    app.theme_cls.font_styles["H6"] = ["Amiri", 20, False, 0.15]
    app.theme_cls.font_styles["Subtitle1"] = ["Amiri", 16, False, 0.15]
    app.theme_cls.font_styles["Subtitle2"] = ["Amiri", 14, False, 0.1]
    app.theme_cls.font_styles["Body1"] = ["Amiri", 16, False, 0.5]
    app.theme_cls.font_styles["Body2"] = ["Amiri", 14, False, 0.25]
    app.theme_cls.font_styles["Button"] = ["Amiri", 14, True, 1.25]
    app.theme_cls.font_styles["Caption"] = ["Amiri", 12, False, 0.4]
    app.theme_cls.font_styles["Overline"] = ["Amiri", 10, True, 1.5]


