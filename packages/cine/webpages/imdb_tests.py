from imdb import IMDb
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull"

    def test_0_get_movie(self, pane, **kwargs):
        fb = pane.formbuilder(cols=1)
        fb.remoteSelect(value='^.movie_id',lbl='Movie title', method=self.fake_getMovieId, hasDownArrow=True)

    @public_method
    def fake_getMovieId(self, _querystring=None,**kwargs):
        b=Bag()
        b.setItem('a', None, caption='Antonio', _pkey='a')
        b.setItem('b', None, caption='Barbara', _pkey='b')
        return b,dict()
    
    def test_1_get_movie(self, pane, **kwargs):
        fb = pane.formbuilder(cols=2)
        fb.remoteSelect(value='^.movie_id',lbl='Movie title', method=self.imdb_getMovieId,
                            auxColumns='title,year,kind', selected_cover='.cover', 
                            selected_kind='.kind', selected_year='.year', colspan=2)
        fb.img(src='^.cover', hidden='^.cover?=!#v', width='200px', height='266px', colspan=2)
        fb.textbox('^.year', lbl='Year')
        fb.textbox('^.kind', lbl='Kind')
        fb.div('^.movie_id', lbl='Movie ID: ')

    @public_method
    def imdb_getMovieId(self,_querystring=None,**kwargs):
        ia = IMDb()
        result = Bag()
        movies = ia.search_movie(_querystring)
        for movie in movies:
            if movie.data['kind'] != 'movie':
                continue
            movie_id = movie.movieID
            title=movie.get('title')
            year=str(movie.get('year'))
            kind=movie.get('kind')
            result.addItem(movie_id, None, title=title, year=year, kind=kind,
                                cover=movie.get('full-size cover url'), _pkey=movie_id,
                                caption='{title} ({year})'.format(title=title, year=year))
        return result,dict(columns='title,year,kind', headers='Titolo,Anno,Tipo')

    def test_2_get_movieData(self, pane, **kwargs):
        fb = pane.formbuilder(cols=2)
        fb.remoteSelect(value='^.movie_id',lbl='Movie title', method=self.imdb_getMovieId,
                            auxColumns='title,year,kind', selected_cover='.cover', colspan=2)
        fb.img(src='^.cover', hidden='^.cover?=!#v', width='200px', height='266px', colspan=2)
    #    fb.button('Get Movie Data', action='FIRE getMovieData')
        fb.dataRpc('.movie_data', self.imdb_getMovieData, movie_id='^.movie_id')
        fb.tree(storepath='.movie_data')

    @public_method
    def imdb_getMovieData(self, movie_id=None):
        ia = IMDb()
        movie = ia.get_movie(movie_id)
        result = Bag(movie.asXML())['movie']
        return result