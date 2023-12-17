AUTHOR = 'PyLadies São Carlos'
SITENAME = 'PyLadies São Carlos'
SITE_DESCRIPTION = 'PyLadies São Carlos é um grupo de mulheres que se reúne para aprender a programar em Python, compartilhar conhecimento e promover a inclusão de mulheres na tecnologia.'

AUTHOR_EMAIL = 'saocarlos@pyladies.com'
AUTHOR_TWITTER = 'pyladiessanca'
AUTHOR_FACEBOOK = 'pyladiessanca'
AUTHOR_GITHUB = 'pyladiessanca'
AUTHOR_INSTAGRAM = 'pyladiessanca'
AUTHOR_LINKEDIN = 'pyladiessanca'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme path
THEME = 'themes/pelican-mediumfox'

SUMMARY_MAX_LENGTH = 30


DEFAULT_PAGINATION = False

MENUITEMS = [
    ('Blog', './archives.html'),
    ('Sobre', './index.html'),
    ('Parcerias', './parcerias.html'),
]