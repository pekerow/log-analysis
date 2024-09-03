
## Log Analysis

### Use
_Log Analysis_ is a Python application that works in conjunction with SQL to deliver statistics on historical database use. The database belongs to a newspaper and contains the names of various articles and the authors who wrote them, logging each "hit" along with the date and time of user access. Running the application will display results on the following queries:

1. What are the 3 most popular articles of all time?
2. Who are the most read authors?
3. On which dates did user actions result in an error rate of 1% or greater?

### What You Need

* Since it's too large to host here on Github, you'll need to download the actual data file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Put the unzipped ``newsdata.sql`` file inside subdirectory in which you are running the application.


### Prepping the Database

Type ``psql -d news -f newsdata.sql`` to create the database tables and populate them with data. You can proceed to explore the database by typing ``psql -d news``. Use ``\dt`` to display the tables and ``\d table`` (replacing "table" with the name of a table) to navigate the table schema. You can also execute SQL commands from the ``news=>>`` prompt. The command will execute only when the ending semicolon ``;`` is reached, so longer queries may be broken up into smaller ones simply by hitting return.

### Running the Application

The code does not rely on SQL views. Simply type ``python3 log-analysis.py`` to run.

The application will take around 20 seconds to run, so please be patient while waiting for the results!
