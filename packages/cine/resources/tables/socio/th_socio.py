#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        anag = r.columnset('anag', name='DATI PERSONALI', color='white', font_weight='bold', background='darkblue')
        anag.fieldcell('nome', width='12em')
        anag.fieldcell('cognome', width='12em')
        anag.fieldcell('nickname')
        anag.fieldcell('data_nascita')
        anag.fieldcell('email', width='18em')
        anag.fieldcell('provincia', text_align='center')
        cine = r.columnset('cine', name='GUSTI CINEMATOGRAFICI', color='white', font_weight='bold', background='darkgreen')
        cine.fieldcell('n_recensioni')
        cine.fieldcell('generi_preferiti', width='20em')
        cine.fieldcell('titolo_film_preferito', width='auto')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record',height='180px')
        top.contentPane(region='right',padding='10px').img(src='^.immagine',
                crop_height='150px',
                crop_width='150px',
                crop_border='2px dotted silver',
                crop_rounded=6, edit=True,
                placeholder=True,
                upload_folder='site:socio/avatars',
                upload_filename='=#FORM.record.nickname')

        fb = top.contentPane(region='center').div(width='95%').formbuilder(cols=2, border_spacing='4px', 
                                                            fld_width='100%', colswidth='auto', width='100%')
        fb.field('nome')
        fb.field('cognome')
        fb.field('nickname')
        fb.field('data_nascita')
        fb.field('email')
        fb.field('provincia')
        fb.field('comune_id')
        fb.field('film_id')
        fb.field('generi_preferiti', tag='checkboxtext', colspan=2, table='cine.genere', cols=2, popup=True)
        fb.field('bio', colspan=2, height='40px')
        
        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@recensioni')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
