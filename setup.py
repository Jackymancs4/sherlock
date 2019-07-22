from setuptools import setup

setup(
    name="sherlock",
    version="0.99.0",
    description="Sherlock: Find Usernames Across Social Networks",
    author="Man Foo",
    author_email="foomail@foo.com",
    packages=["sherlock"],
    # install_requires=['bar', 'greek'],
    entry_points={"console_scripts": ["sherlock = sherlock.__main__:main"]},
)
