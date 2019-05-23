import setuptools

setuptools.setup(
    name="pycon-il-2019",
    version="0.0.1",
    author="Barak Korren",
    author_email="bkorren@redhat.com",
    description="Example code for extending-ansible PyCon-IL talk",
    long_description=(
        "# PyCON-IL 2019 Extending-Ansible talk\n\n"
        "Example scripts and libraries presented during the talk"
    ),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)
