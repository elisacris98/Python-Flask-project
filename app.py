from Flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('movie', user='postgres', password= '2345', host='localhost', port='5432')

class BaseModel(Model):
    class Meta:
        database = db

class Movie(BaseModel):
    name = CharField()
    genre = CharField()
    year = IntegerField()


db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])


Movie(name='White Chicks', genre='Comedy', year=2004).save()
Movie(name='The Interview', genre='Comedy', year=2014).save()
Movie(name='Spider-man Into the', genre='Sci-fi', year=2018).save()
Movie(name='The Conjuring', genre='Horror', year='2013').save()
Movie(name='Mean Girls', genre='Comedy/Drama', year=2004).save()