
## Log Analysis

### Use
_Log Analysis_ is a Python application that works in conjunction with SQL to deliver statistics on historical database use. The database belongs to a newspaper and contains the names of various articles and the authors who wrote them, logging each "hit" along with the date and time of user access. Running the application will display results on the following queries:

1. What are the 3 most popular articles of all time?
2. Who are the most read authors?
3. On which dates did user actions result in an error rate of 1% or greater?

### What You Need
_Log Analysis_ runs on a virtual Ubuntu box, and the database engine is postgresql. To get started please proceed as follows:

* You will need a shell window. If you're on a Mac this is the command line utility. If on Windows 7 or later you will need to download [Git BASH](https://gitforwindows.org/).

* In the shell you will run the Ubuntu box using [Vagrant](https://www.vagrantup.com/) in conjunction with [Virtual Box](https://www.virtualbox.org/wiki/Downloads).

* Since it's too large to host here on Github, you'll need to download the actual data file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Put the unzipped ``newsdata.sql`` file inside the log-analysis subdirectory of your Vagrant folder. This is also where you will finde the ``log-analysis.py`` file which runs the application.


### Prepping the Database

Type ``vagrant up`` which will install Ubuntu 22.04 as a virtual machine. This will take several minutes to finish. Once complete, type ``vagrant ssh`` to log in to your virtual machine. Type ``cd /vagrant`` to access your shared files, where you'll find ``newsdata.sql`` and ``log-analysis.py`` located in the folder called ``log-analysis``. 

Type ``cd log-analysis`` and then type ``psql -d news -f newsdata.sql`` to create the database tables and populate them with data. You can proceed to explore the database by typing ``psql -d news``. Use ``\dt`` to display the tables and ``\d table`` (replacing "table" with the name of a table) to navigate the table schema. You can also execute SQL commands from the ``news=>>`` prompt. The command will execute only when the ending semicolon ``;`` is reached, so longer queries may be broken up into smaller ones simply by hitting return.

### Running the Application

If you are still in the ``psql news=>`` prompt, type ``^ d`` to escape, which will bring you back to the shared directory prompt ``/vagrant$``. You can now run the application.
The code does not rely on SQL views. Simply type ``python3 log-analysis.py`` to run.

The application will take around 20 seconds to run, so please be patient while waiting for the results!
