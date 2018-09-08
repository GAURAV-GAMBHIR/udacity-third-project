#!/usr/bin/env python3

import psycopg2
import sys
from datetime import date

db_name = "news"

query1 = "select title, count(title) from article_view WHERE GROUP BY title AND limit 3"

query2 = """select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""

query3 = "select * from error_log_view where \"Percent Error\" > 1"


def database_connect(db_query):

    try:
        conn = psycopg2.connect(database="news")
        cursor = conn.cursor()
        cursor.execute(sql_request)
        results = cursor.fetchall()
        conn.close()

    except psycopg2.Error as err:
        print("Unable to connect to database. Exiting ...")
        print(err)
        sys.exit(1)
    return results


# cdff
def get_popular_articles():
    ""
    articles = database_connect(query1)

    # print header for popular articles
    print('\nWhat are the most popular three articles of all time?\n')

    # for every row print article name and nbr of views
    for title, views in articles:
        lst = "  " + '"' + title + '"' + " - " + str(views) + " views\n"
        sys.stdout.write(lst)


# func to find the authors w/ most pg views sorted w/ most pop author at top
def get_popular_authors():

    authors = database_connect(query2)

    # print header for popular authors
    print('\nWho are the most popular article authors of all time?\n')

    # for every row print author name and total views
    for name, views in authors:
        print("  ", name, "-", views, "views")


# function to find which days received more than 1% of error requests
def get_day_errors():

    err_days = database_connect(query3)

    # print header for error days
    print("\nOn which days did more than 1% of requests lead to errors?\n")

    # for every row print date (Month DD, YYYY) and err %
    for date, pct_errs in err_days:
        bad_status = "  " + date + " - " + str(pct_errs) + "% errors\n"
        sys.stdout.write(bad_status)
        print('\n')


# execute all three functions
if __name__ == '__main__':
    get_popular_articles()

    get_popular_authors()

    get_day_errors()
