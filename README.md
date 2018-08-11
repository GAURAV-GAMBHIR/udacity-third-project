# udacity-third-project
Logs Analysis:-

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.
A large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a new paper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

How To Run:-

You will need-
a. Python3
b. Vagrant
c. VirtualBox

Setup-
a. Install Vagrant and VirtualBox
b. Clone this repository

To Run-

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

To execute the program, run `python3 newsdata.py` from the command line.
