from SimpleProblemSolvingAgent import UndirectedGraph, Graph
##############################################################################
# This file contains the graph of ethiopia and the locations of each city. 
# The graph is used to calculate the distances between cities in ethiopia.
##############################################################################
 # Provided graph of ethiopia - not being used in my implementation
'''
# ethiopia_map is a graph of the cities in ethiopia, with the cost of travel between each pair of cities.
ethiopia_map = UndirectedGraph(dict(
    Addis_Ababa=dict(Ziway=75, Shashemene=140, Adigrat=118),
    Bahir_Dar=dict(Gamo=85, Woliso=101, Gondar=90, Fiche=211),
    Chiro=dict(Dire_Dawa=120, Bale_Robe=146, Woliso=138),
    Dire_Dawa=dict(Meleke=75),
    Entoto=dict(Hawasa=86),
    Fiche=dict(Shashemene=99),
    Hawasa=dict(Gamo=98),
    Jima=dict(Wolaita=92, Nazret=87),
    Kombolcha=dict(Adigrat=111, Meleke=70),
    Omo=dict(Ziway=71, Shashemene=151),
    Woliso=dict(Bale_Robe=97),
    Bale_Robe=dict(Shashemene=80),
    Gamo=dict(Wolaita=142)))
'''

# Calculated distances between cities in ethiopia using the haversine formula
ethiopia_map = UndirectedGraph(dict(
    Addis_Ababa=dict(Ziway=51, Shashemene=223, Adigrat=49),
    Bahir_Dar=dict(Gamo=54, Woliso=109, Gondar=59, Fiche=181),
    Chiro=dict(Dire_Dawa=96, Bale_Robe=97, Woliso=103),
    Dire_Dawa=dict(Meleke=38),
    Entoto=dict(Hawasa=89),
    Fiche=dict(Shashemene=64),
    Hawasa=dict(Gamo=103),
    Jima=dict(Wolaita=58, Nazret=95),
    Kombolcha=dict(Adigrat=54, Meleke=95),
    Omo=dict(Ziway=56, Shashemene=220),
    Woliso=dict(Bale_Robe=48),
    Bale_Robe=dict(Shashemene=80),
    Gamo=dict(Wolaita=230)))

# The locations (latitude/longitude) of each city in the map
ethiopia_map.locations = dict(
    Addis_Ababa=(46.1866, 21.3123), Bahir_Dar=(44.4268, 26.1025), Chiro=(44.3302, 23.7949),
    Dire_Dawa=(44.6369, 22.6597), Entoto=(44.0613, 28.6310), Fiche=(45.8416, 24.9731),
    Gondar=(43.9037, 25.9699), Hawasa=(44.6893, 27.9457), Jima=(47.1585, 27.6014),
    Kombolcha=(45.6910, 21.9035), Meleke=(44.9052, 22.3673), Nazret=(46.9759, 26.3819),
    Omo=(47.0465, 21.9189), Woliso=(44.8565, 24.8692), Bale_Robe=(45.0997, 24.3693),
    Shashemene=(45.8035, 24.1450), Adigrat=(45.7489, 21.2087), Gamo=(44.7181, 26.6453),
    Wolaita=(46.6407, 27.7276), Ziway=(46.6225, 21.5174))