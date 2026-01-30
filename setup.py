from setuptools import setup, find_packages

setup(
    name="idioms",
    version="0.0.1",
    package_dir={"idioms": "."},  # Map current directory as 'idioms' package
    packages=["idioms", "idioms.idioms", "idioms.idioms.data", "idioms.idioms.data.idastubs"],
)
