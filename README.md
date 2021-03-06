# udacity-third-project
### Logs Analysis:-
In this project we are building an internal reporting tool that will use information from the database to discover
what kind of articles the site's readers like. 
There are three questions 
1. What are the most popular three articles of all time? , 
2. Who are the most popular article authors of all time?, 
3. On which days did more than 1% of requests lead to errors?,      
we are using python3 program using the psycopg2 module to connect to the database.

### requirement:-
  a.Python3,     
  b.Vagrant,      
  c.VirtualBox,     
  d.git

### Setup-
   Download & Install python3 (https://www.python.org/downloads/)              
   Download & Install Vagrant (https://www.vagrantup.com/downloads.html)            
   Download & Install VirtualBox (https://www.virtualbox.org/wiki/Downloads)          
   Download the vagrant setup file (https://github.com/udacity/fullstack-nanodegree-vm)         
   Download the daatabase setup file (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   

### To_Run-
  Launch Vagrant VM by running 'vagrant up'         
  To connect, use the command 'vagrant ssh'         
  To load the data, use the command 'psql -d news -f newsdata.sql'          
  To run the database, use the command 'psql -d news'         
  To run the python program, use the command 'python pythonlog.py'          

  
### OUTPUT-
  1. The Top three articles of all time                                           
  +++++++++++++++++++++++++++++++++++++                                                                                    
  Candidate is jerk, alleges rival -> 338647 views                                                                        
  Bears love berries, alleges bear -> 253801 views                                                                        
  Bad things gone, say good people -> 170098 views                                                  
                                                                                  
                                                                      
  2. The Top authors of all time                                                                          
  ++++++++++++++++++++++++++++++                         
  Ursula La Multa -> 507594 views                                                                                         
  Rudolf von Treppenwitz -> 423457 views                                                                                  
  Anonymous Contributor -> 170098 views                                                                                   
  Markoff Chaney -> 84557 views                                                                         
                                      
                                                              
  3. The day more than 1% of requests lead to errors                                                           
  ++++++++++++++++++++++++++++++++++++++++++++++++++                                                        
  2016-07-17 -> 2.2626862468 % errors                                       
                                                                    
                                                      
  Thank you!, you have done successfully 
