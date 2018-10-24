#!/usr/bin/env python3
import psycopg2


def QueryDb(query):
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def TopArticles():
    query_string = """
        SELECT a.title, count(log.*)
        FROM articles a
        JOIN log
            ON log.path = '/article/'||a.slug
        WHERE log.status LIKE '200%'
        GROUP BY 1
        ORDER BY 2 DESC;"""

    result = QueryDb(query_string)

    print('The most viewed articles are:')

    for result in result:
        title = result[0]
        views = result[1]
        print('\t{0}: {1} views'.format(title, views))


def TopAuthors():
    query_string = """
        SELECT a.name,count(*)
        FROM log l
        JOIN articles
            ON l.path = '/article/'||articles.slug
        LEFT JOIN authors a
            ON articles.author = a.id
        WHERE l.path != '/'
        GROUP BY 1
        ORDER BY 2 DESC;"""

    result = QueryDb(query_string)

    print('The most viewed authors are:')

    for result in result:
        author = result[0]
        views = result[1]
        print('\t{0}: {1} views'.format(author, views))


def ErrorRate():
    query_string = """
        SELECT *
        FROM (
            SELECT date_trunc('day',time)::date,
                sum(
                    CASE WHEN status LIKE '404%' THEN 1
                    ELSE 0
                    END
                    )::float / count(*) AS error_rate
            FROM log
            GROUP BY 1) AS errors
        WHERE error_rate > 0.01;"""

    result = QueryDb(query_string)

    print('On the following days the error rate was greater than 1%:')

    for result in result:
        day = result[0]
        error_rate = round(result[1] * 100.0, 2)
        print('\t{0}: {1}% errors'.format(day, error_rate))


if __name__ == '__main__':
    TopArticles()
    print('\n')
    TopAuthors()
    print('\n')
    ErrorRate()
