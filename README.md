
## Log Analysis

### Overview
_Log Analysis_ is a Python application that works in conjunction with PostgreSQL to deliver statistics on historical database usage. The database belongs to a newspaper and contains the titles of various articles, the authors who wrote them, and logs of each "hit" (user access) along with the date and time of the request. Running the application will display results for the following queries:

1. What are the three most popular articles of all time?
2. Who are the most-read authors of all time?
3. On which dates did user requests result in an error rate of 1% or higher?

### Requirements

* **Database file**: Download the actual data file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) as it is too large to host directly on GitHub. Place the unzipped `newsdata.sql` file in the same directory where you will run the application.

### Setting up the Database

1. Create the database and load the data by typing:
   ```
   psql -d news -f newsdata.sql
   ```
   This command creates the necessary tables and populates them with data.

2. To explore the database manually, type:
   ```
   psql -d news
   ```
   Use the following commands to view the database structure:
   - `\dt` to display the list of tables
   - `\d table_name` (replace `table_name` with the actual table name) to view the schema of a specific table

3. SQL queries can be executed from the `news=#` prompt. Note that SQL statements must end with a semicolon (`;`), and you can break up longer queries by pressing return before entering the semicolon.

### Running the Application

To run the application, type:
```
python3 log-analysis.py
```

The script does **not** rely on any pre-existing SQL views, and all queries are executed directly in Python.

*Note*: The application may take around 20 seconds to complete, depending on your machine. Please be patient while the results are generated.
