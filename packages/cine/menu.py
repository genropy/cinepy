#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch(u"Cineclub")
    auto.thpage(u"Soci", table="cine.socio")
    auto.thpage(u"Recensioni", table="cine.recensione")
    auto.thpage(u"Film", table="cine.film")
    auto.lookups('Tabelle lookup', lookup_manager='cine')

