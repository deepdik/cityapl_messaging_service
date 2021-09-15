import os
from utils import pylogger

from flask import Flask
from flask_pymongo import PyMongo
from mysql.connector import Error
from mysql.connector import pooling

import psycopg2
from psycopg2 import pool
import psycopg2.extras

class DBConnector:
    """
    Singleton class for database connection
    """
    __instance = None

    @classmethod
    def connect_with_pool(cls, app):
        """ 
        static method to get instance
        """
        if not cls.__instance:
            print('new')
            cls.__instance = cls.__start_pool(app)
        return cls.__instance

    @staticmethod
    def __start_pool(app):
        """
        """
        app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
        mongo = PyMongo(app)
        return mongo


class PostgresDBConnector:
    """
    Singleton class for database connection
    """
    __instance = None

    @classmethod
    def connect_with_pool(cls, app):
        """ 
        static method to get instance
        """
        if not cls.__instance:
            cls.__instance = cls.__start_pool(app)
        return cls.__instance

    @staticmethod
    def __start_pool(app):
        """
        """
        host = app.config['DATABASE'].get('HOST')
        port = app.config['DATABASE'].get('PORT')
        user = app.config['DATABASE'].get('USER')
        password = app.config['DATABASE'].get('PASSWORD')
        database_name = app.config['DATABASE'].get('NAME')
        postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(
            1,
            15,
            user=user,
            password=password,
            host=host,
            port=port,
            database=database_name
        )
        if (postgreSQL_pool):
            print("Connection pool created successfully")
            return postgreSQL_pool
        return None


class PostgresExcecuteQuery:
    """
    """
    def __get_connection_from_pool(postgreSQL_pool):
        """
        """
        # Use getconn() to Get Connection from connection pool
        ps_connection = postgreSQL_pool.getconn()
        if ps_connection:
            return ps_connection

        return None

    def fetch_data(postgreSQL_pool, query, data=None):
        """
        """
        connection = PostgresExcecuteQuery.__get_connection_from_pool(postgreSQL_pool)
        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        if cursor:
            try:
                cursor.execute(query, data)
                record = cursor.fetchall()
            except Error as e:
                print(e)
            finally:
                # closing database connection.
                cursor.close()
                # Use this method to release the connection object
                # and send back to connection pool
                postgreSQL_pool.putconn(connection)
                return record
        return None


class MysqlDBConnector:
    """
    Singleton class for database connection
    """
    __instance = None

    @classmethod
    def connect_with_pool(cls, app):
        """ 
        static method to get instance
        """
        if not cls.__instance:
            cls.__instance = cls.__start_pool(app)
        return cls.__instance

    @staticmethod
    def __start_pool(app):
        """
        """
        pool_size = 5
        host = app.config['DATABASE'].get('HOST')
        port = app.config['DATABASE'].get('PORT')
        user = app.config['DATABASE'].get('USER')
        password = app.config['DATABASE'].get('PASSWORD')
        database_name = app.config['DATABASE'].get('NAME')
    
        connection_pool = pooling.MySQLConnectionPool(
            pool_name="pynative_pool",
            pool_size=pool_size,
            pool_reset_session=True,
            host=host,
            database=database_name,
            user=user,
            password=password,
            port=port
        )
        return connection_pool


class MysqlExcecuteQuery:
    """
    """
    def __get_connection_from_pool(connection_pool):
        """
        """
        print("Printing connection pool properties ")
        print("Connection Pool Name - ", connection_pool.pool_name)
        print("Connection Pool Size - ", connection_pool.pool_size)

        # Get connection object from a pool
        connection_object = connection_pool.get_connection()
        print(id(connection_pool))
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)
            return connection_object

        return None

    def fetch_data(connection_pool, query, data=None):
        """
        """
        connection = ExcecuteQuery.__get_connection_from_pool(connection_pool)
        cursor = connection.cursor(dictionary=True)
        if cursor:
            try:
                cursor.execute(query, data)
                record = cursor.fetchall()
            except Error as e:
                print(e)
            finally:
                # closing database connection.
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
                return record
        print("error in fetch query")
        return None
