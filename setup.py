from setuptools import setup
setup(
    name = 'grocery-chat-bot',
    version = '0.1.0',
    packages = ['grocery-chat-bot'],
    entry_points = {
        'console_scripts': [
            'chatbot = app.__main__:main'
        ]
    })