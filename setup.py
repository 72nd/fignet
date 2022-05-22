import setuptools

setuptools.setup(
    name="fignet",
    version="0.1.0",
    author="72nd",
    author_email="msg@frg72.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points="""
            [console_scripts]
            fignet=fignet.main:run
        """,
    install_requires=[
        "lxml==4.8.0",
        "pydot==1.4.2",
        "pygraphviz==1.9",
        "pyyaml==6.0",
        "networkx==2.8.2",
        "typer==0.4.1",
    ],
)
