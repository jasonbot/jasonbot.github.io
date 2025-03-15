filenames = [
    "AtkinsonHyperlegibleMono-Bold.woff2",
    "AtkinsonHyperlegibleMono-BoldItalic.woff2",
    "AtkinsonHyperlegibleMono-ExtraBold.woff2",
    "AtkinsonHyperlegibleMono-ExtraBoldItalic.woff2",
    "AtkinsonHyperlegibleMono-ExtraLight.woff2",
    "AtkinsonHyperlegibleMono-ExtraLightItalic.woff2",
    "AtkinsonHyperlegibleMono-Light.woff2",
    "AtkinsonHyperlegibleMono-LightItalic.woff2",
    "AtkinsonHyperlegibleMono-Medium.woff2",
    "AtkinsonHyperlegibleMono-MediumItalic.woff2",
    "AtkinsonHyperlegibleMono-Regular.woff2",
    "AtkinsonHyperlegibleMono-RegularItalic.woff2",
    "AtkinsonHyperlegibleMono-SemiBold.woff2",
    "AtkinsonHyperlegibleMono-SemiBoldItalic.woff2",
    "AtkinsonHyperlegibleNext-Bold.woff2",
    "AtkinsonHyperlegibleNext-BoldItalic.woff2",
    "AtkinsonHyperlegibleNext-ExtraBold.woff2",
    "AtkinsonHyperlegibleNext-ExtraBoldItalic.woff2",
    "AtkinsonHyperlegibleNext-ExtraLight.woff2",
    "AtkinsonHyperlegibleNext-ExtraLightItalic.woff2",
    "AtkinsonHyperlegibleNext-Light.woff2",
    "AtkinsonHyperlegibleNext-LightItalic.woff2",
    "AtkinsonHyperlegibleNext-Medium.woff2",
    "AtkinsonHyperlegibleNext-MediumItalic.woff2",
    "AtkinsonHyperlegibleNext-Regular.woff2",
    "AtkinsonHyperlegibleNext-RegularItalic.woff2",
    "AtkinsonHyperlegibleNext-SemiBold.woff2",
    "AtkinsonHyperlegibleNext-SemiBoldItalic.woff2",
]

weights = (
    ("ExtraBold", 800),
    ("Bold", 600),
    ("Regular", 400),
    ("Light", 300),
    ("ExtraLight", 200),
)

for filename in filenames:
    weight = 400
    for namepart, wt in weights:
        if namepart in filename:
            weight = wt
            break
    isitalic = "Italic" in filename
    text = f"""@font-face {{
    font-family: "{filename.split('-')[0]}";
    font-style: {'italic' if isitalic else 'normal'};
    font-weight: {weight};
    src: url(/fonts/{filename}) format("woff2");
}}"""
    print(text)
