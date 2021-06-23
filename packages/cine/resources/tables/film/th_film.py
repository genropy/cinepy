#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('imdb_id')
        r.fieldcell('titolo')
        r.fieldcell('trama')
        r.fieldcell('anno')
        r.fieldcell('genere')
        r.fieldcell('regista')

    def th_order(self):
        return 'imdb_id'

    def th_query(self):
        return dict(column='titolo', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('imdb_id')
        fb.field('titolo')
        fb.field('dati')
        fb.field('cover_url')
        fb.field('trama')
        fb.field('anno')
        fb.field('genere')
        fb.field('regista')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
