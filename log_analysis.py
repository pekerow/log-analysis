#!/usr/bin/env python3

import psycopg2

question1 = "What are the three most popular articles of all time?"
query1 = """SELECT title, count(*) as hits FROM articles
            JOIN log ON substring(log.path, 10) LIKE articles.slug
            GROUP BY title ORDER BY hits DESC LIMIT 3;"""

question2 = "Who are the most read article authors of all time?"
query2 = """SELECT authors.name, count(*) as hits FROM articles
            JOIN authors ON authors.id = articles.author
            JOIN log ON substring(log.path, 10) LIKE articles.slug
            GROUP BY authors.name ORDER BY hits DESC;"""

question3 = "On which days did more than 1% of user queries result in errors?"
query3 = """SELECT Date(time) as day, 
            count(*) FILTER (WHERE status LIKE '404%') * 100.0 / count(*) as error_rate
            FROM log GROUP BY day HAVING
            (count(*) FILTER(WHERE status LIKE '404%') * 100 / count(*)) > 1;"""


def get_results(query: str) -> list:
    with psycopg2.connect(database="news") as db:
        with db.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


def print_results(outcome: tuple):
    print(f"\n{outcome[1]}")
    for i, result in enumerate(outcome[0], 1):
        print(f"\t{i} - {result[0]} -- {result[1]} hits")


def print_errors(outcome: tuple):
    print(f"\n{outcome[1]}")
    for result in outcome[0]:
        print(f"\t{result[0]} -- {result[1]}% errors\n")


if __name__ == '__main__':
    top_articles = get_results(query1), question1
    top_authors = get_results(query2), question2
    error_days = get_results(query3), question3

    print_results(top_articles)
    print_results(top_authors)
    print_errors(error_days)
