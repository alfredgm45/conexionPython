from htmldom import htmldom


dom = htmldom.HtmlDom("file:///opt/siog/taecjaa/AcquisitionData.html")
# #/opt/siog/taecjaa/AcquisitionData.html
dom = dom.createDom()

# tablas = dom.find("table")

# etiqueta  = list(tablas[0].find("td[align=center]"))

# lista = []

# for i in etiqueta:
# 	if i!=etiqueta[2] and i!=etiqueta[3]:
		
# 		lista.append(i.text().strip("\n"))


# print(lista)



