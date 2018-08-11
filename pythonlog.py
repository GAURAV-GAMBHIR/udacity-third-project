import psycopg2
name="news"
#1. What are the most popular three articles of all time?
q1="select title,views from article_view limit 3"
#2. Who are the most popular article authors of all time?
q2="""select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""
#3. On which days did more than 1% of requests lead to errors?
q3="select * from error_log_view where \"Percent Error\" > 1"
#to store results
q1_rslt = dict()
q1_rslt['title'] = "a.The 3 most popular articles of all time are"
q2_rslt = dict()
q2_rslt['title'] = """b.The most popular article authors of
all time are:\n"""
q3_rslt = dict()
q3_rslt['title'] = """c.Days with more than 1% of request that
lead to an error"""
#returns query result
def get_q_rslt(q):
    db=psycopg2.connect(database=name)
    c=db.cursor()
    c.execute(q)
    rslts=c.fetchall()
    db.close()
    return rslts
def print_q_rslts(q_rslt):
    print(q_rslt['title'])
    for rslt in q_rslt['rslts']:
        print('\t' + str(rslt[0])+' -> '+str(rslt[1])+'views')
def print_error_q_rslts(q_rslt):
    print(q_rslt['title'])
    for rslt in q_rslt['rslts']:
        print('\t'+str(rslt[0])+' -> '+str(rslt[1])+'%')
#stores query result
q1_rslt['rslts'] = get_q_rslt(q1)
q2_rslt['rslts'] = get_q_rslt(q2)
q3_rslt['rslts'] = get_q_rslt(q3)
#print formatted output
print_q_rslts(q1_rslt)
print_q_rslts(q2_rslt)
print_error_q_rslts(q3_rslt)
