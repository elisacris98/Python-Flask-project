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

app = Flask(__name__)

@app.route('/movie/', methods=['GET', 'POST'])
@app.route('/movie/<id>', methods=['GET','PUT','DELTE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Movie.get(Movie.id == id)))
        else:
            movie_list = []
            for movie in Movie.select():
                movie_list.append(model_to_dict(movie))
            return jsonify(movie_list)
    

    if request.method == 'PUT':
        body = request.get_json()
        Movie.update(body).where(Movie.id == id).execute()
        return "Movie" + str(id) + " has been updated."
    

    if request.method == 'POST':
        new_movie = dict_to_model(Movie, request.get.json())
        new_movie.save()
        return jsonify({"success": True})
    
    if request.method == 'DELETE':
        Movie.delete().where(Movie.id == id).execute()
        return "Movie" + str(id) + "deleted"
    


app.run(debug=True, port=5000)