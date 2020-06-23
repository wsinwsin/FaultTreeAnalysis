from setuptools import setup


setup(
    name = "ft_bdd",
    version = "1.0",
    autor = 'wsinwsin',
    author_email = "kitasin101021@gmail.com",
    description = "Tool to convert FaultTree to BDD",
    long_description = "",
    url = "https://github.com/wsinwsin/FaultTreeAnalysis",
    install_requires = ['IPython','pybind11', 'numpy','pydotplus','graphviz'],
    test_suite='tests'
)