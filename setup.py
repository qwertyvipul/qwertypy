from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='qwertypy',
    version='0.5.9',
    author='Vipul Sharma | @qwertyvipul',
    description='My personal python utilities library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://qwertyvipul.io/qwertypy/",
    project_urls={
        "Repository": "https://github.com/qwertyvipul/qwertypy",
        "Changelog": "https://github.com/qwertyvipul/qwertypy/blob/main/CHANGELOG.md",
        "Colab notebook": "https://colab.research.google.com/drive/1SK96YfBgIPY-CKNfvQxvBKkJnNA7fSCe?usp=sharing"
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose']
)