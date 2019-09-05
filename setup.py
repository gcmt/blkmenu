from setuptools import setup


with open("README.md") as f:
    readme = f.read()


setup(
    name="blkmenu",
    version="0.1",
    description="Tiny curses wrapper around lsblk and udisksctl",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Giacomo Comitti",
    author_email="dev@gcomit.com",
    url="https://github.com/gcmt/blkmenu",
    data_files=[("man/man1", ["blkmenu.1"])],
    scripts=["blkmenu"],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
)
