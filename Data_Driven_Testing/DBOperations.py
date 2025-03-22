# insertion,update,delete

from selenium import webdriver
import mysql.connector

# establish connection to database -
# extract connection details

con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="mydb")

