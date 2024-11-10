from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip()
                    and not line.startswith('#')]

setup(
    name="mastermind",
    version="0.1.0",
    author="Shahin ABDI",
    author_email="contact@shahinabdi.fr",
    description="A command-line Mastermind game implementation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shahinabdi/mastermind",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.11',
)
