from .models import Gist
from datetime import datetime

def search_gists(db_connection, **kwargs):
    result  = []
    sql_query = """SELECT * FROM gists"""
    if kwargs:
        if 'github_id' in kwargs:
            sql_query += ' WHERE github_id == :github_id'
        elif 'created_at' in kwargs:
            sql_query += ' WHERE datetime(created_at) == datetime(:created_at)'
        cursor = db_connection.execute(sql_query, kwargs)
        gists = cursor.fetchall()
    else:
        cursor = db_connection.execute(sql_query)
        gists = cursor.fetchall()
    for gist in gists:
        result.append(Gist(gist))
    return result
        