from CoverImageGenerator import CoverImageGenerator

emojis = [
    # ('🗄', '#E5C07B', '#282C34'),
    # ('🔑', '#E5C07B', '#282C34'),
    # ('🗃', '#E5C07B', '#282C34'),
    # ('🐘', '#C678DD', '#282C34'),
    # ('🐍', '#98C779', '#282C34'),
    # ('🐱‍💻', '#ABB2BF', '#282C34'),
    # ('🖥', '#ABB2BF', '#282C34'),
    # ('✨', '#282C34', '#E5C07B'),
    # ('', '#ABB2BF', '#282C34'),
    # ('', '#ABB2BF', '#282C34'),
    # ('', '#ABB2BF', '#282C34'),
    ('', '#ABB2BF', '#282C34'),
]

for emoji, bg, fg in emojis:
    generator = CoverImageGenerator(
        emoji=emoji,
        width=1200,
        height=600,
        color_bg=bg,
        color_fg=fg
    )
    image = generator.generate()
    image.save(f'./cover-images/{emoji}.png')
