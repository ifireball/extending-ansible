import setuptools

setuptools.setup(
    name="ansible-device",
    version="0.0.1",
    author="Barak Korren",
    author_email="bkorren@redhat.com",
    description="A Python API for Ansible devices",
    long_description=(
        "# ansible-device\n\n"
        "A Python API for controlling Ansible faster-then-light\n"
        "interstellar communication devices\n"
    ),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)
