from lxml import objectify
import folium as fm

main = objectify.parse('London_division_2500-150.xml')

print(main.ObjectData)

m = fm.Map([50.854457, 4.377184], zoom_start=5, tiles='cartodbpositron')