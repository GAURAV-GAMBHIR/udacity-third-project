#!/usr/bin/env python3
# import postgresql db and time module
import psycopg2
from datetime import date


# connect to the postgrs database
def postgres_db():
    return psycopg2.connect(database="news")


def top_articles():
    # queries for select top three articles title and number of views
    top_articles = """select articles.title, count(*) as x
            from log, articles where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title order by x desc limit 3;"""
    db = postgres_db()
    cur = db.cursor()
    # execute the database query by passing request articles
    cur.execute(top_articles)
    results = cur.fetchall()

    # select title and number of views from results
    for title, x in results:
        print(" {} -> {} views".format(title, x))
    # close the database connection
    db.close()


def top_authors():
    # queries for select top authors name and number of views
    top_authors = """select authors.name, count(*) as x
            from articles, authors, log where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name order by x desc;"""
    db = postgres_db()
    cur = db.cursor()
    cur.execute(top_authors)
    results = cur.fetchall()

    # select name and number of views of top three authors from results
    for name, x in results:
        print(" {} -> {} views".format(name, x))
    db.close()


def error_day():
    # queries for select days with more then 1% errors name
    errors_days = """ WITH xyz AS (SELECT time::date AS day, count(*)
                FROM log GROUP BY time::date ORDER BY time::date),
                errors AS (SELECT time::date AS day, count(*)
                FROM log WHERE status != '200 OK' GROUP BY time::date
                ORDER BY time::date),
                total_error AS (SELECT xyz.day, errors.count::
                float / xyz.count::float * 100 AS abc
                FROM xyz, errors WHERE xyz.day = errors.day )
                SELECT * FROM total_error WHERE abc > 1;"""
    db = postgres_db()
    cur = db.cursor()
    cur.execute(errors_days)
    results = cur.fetchall()

    # select status in results for highest errors
    for status in results:
        print(str(status[0]) + ' -> ' + str(status[1]) + ' % errors')
    db.close()
# call the all functions of this file by executing current module
if __name__ == '__main__':
    print("1. The Top three articles of all time")
    print("+++++++++++++++++++++++++++++++++++++")
    top_articles()
    print("\n")
    print("2. The Top authors of all time")
    print("++++++++++++++++++++++++++++++")
    top_authors()
    print("\n")
    print("3. The day more than 1% of requests lead to errors")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    error_day()
    print("\n")
    print("Thank you!, you have done successfully")
