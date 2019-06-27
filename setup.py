import setuptools

setuptools.setup(
    name="a_package",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    package_data={"a_package": ["py.typed"]},
)
