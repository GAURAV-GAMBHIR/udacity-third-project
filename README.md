# udacity-third-project
Logs Analysis:-
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.A large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a new paper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

How To Run:-

Pre Requisites-
  a.[Python3](https://www.python.org/)
  b.[Vagrant](https://www.vagrantup.com/)
  c.[VirtualBox](https://www.virtualbox.org/)

Setup-
a. Install Vagrant and VirtualBox
b. Clone this repository

To Run-
Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`
To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes 3 tables-
a. Authors table
b. Articles table
c. Log table

To execute the program, run python3 pythonlog.py.
