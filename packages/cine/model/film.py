# encoding: utf-8
from imdb import IMDb

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('film', pkey='imdb_id', 
                        name_long='Film', 
                        name_plural='Film', caption_field='titolo')
        self.sysFields(tbl, id=False)
        tbl.column('imdb_id', size=':7', name_long='id IMDB')
        tbl.column('titolo', name_long='Titolo film', name_short='Titolo')
        tbl.column('dati', dtype='X', name_long='Dati film')
        tbl.column('cover_url', name_long='Cover url')
        tbl.column('anno', dtype='L', name_long='Anno')
        tbl.column('genere', name_long='Genere')
        tbl.column('regista', name_long='Regista')
        tbl.column('trama', name_long='Trama')
        tbl.column('imdb_rating', dtype='N', name_long='IMDB Rating')
        tbl.column('cast', dtype='X', name_long='Cast')