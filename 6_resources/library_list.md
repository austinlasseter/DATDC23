We use several libraries and Integrated Development Environments throughout this class. Here is an overview.


**Integrated Development Environments**
* **Spyder** - This is a Python IDE that imitates Rstudio. This is generally better used for larger projects that don't have have that needs to be presented to a general audience.
* **Jupyter Notebook** - A great example of literate programming, Jupyter Notebook allows use to mix markdown code for presentation and functioning code. This is great for presentations and prototypes, but you probably shouldn't work on a large project on Jupyter Notebook because other IDE provide better tools for auto-checking syntax and code structure.
Note: For larger projects it can help to use something like Pycharm and Eclipse with a Python plug-in to help you organize files, check code, automatically test code, and automatically deploy.

**Python Libraries**
* **Pandas** - A popular data manipulation library that's inspired by the DataFrame concept from R programming
* **Sklearn** - A very well documented and consistent machine learning library. You are likely to find more efficient or powerful version of the algorithms that come with Sklearn in other corners of Python, but the great documentation and consistency make this an excellent learning and rapid-prototyping environment.
* **Numpy** - MatLab for Python essentially. One of the great strength of Python for data science is the numerical capability that is readily available that is hard to find in other langauges. In practice, most modern numerical tools all use the same C and Fortran libraries that have been optimized over the last 40 years and make convenient interfaces to them.
* **Matplotlib** - A bare bones graphing library in Python. This clearly imitates MatLab ploting and serves as a basis for many other plotting libraries.
* **Seaborn** - One of the more polished graphing in Python that focuses and specific exploratory data needs. The API reference comes with many useful out of the box examples that take little effort to understand. This is useful in class, but not difficult enough to warrant a direct lesson. http://seaborn.pydata.org/api.html
* **BeautifulSoup** - Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. Great for webscraping and possibly working with XML variants of data.
