from setuptools import setup


VERSION = '1.0.0'


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="whatismyip",
    version=VERSION,
    description="Shows your ip to access the internet",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="Check IP",
    url="https://github.com/danilocgsilva/what-is-my-ip",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["whatismyip"],
    entry_points={"console_scripts": ["wimi=whatismyip.__main__:main"]},
    include_package_data=True
)
