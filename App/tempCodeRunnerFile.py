    tabla0.add_row(["Movie",Movie_count])
    tabla0.add_row(["TV SHOW",TV_count])
    print(tabla0)
    tabla1 = PrettyTable()
    tabla1.field_names = ["type", "title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
    tabla1._max_width = {"cast":30,"description":10,"listed_in":15}
    tabla1.hrules = ALL
    if lt.size(titles) >= 6:
        first3 = lt.subList(titles, 1, 3)
        last3 = lt.subList(titles, lt.size(titles)-2, 3)

        for title in lt.iterator(first3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])

        for title in lt.iterator(last3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    else:
        for title in lt.iterator(titles):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    print(tabla1)
def printreq8(control,N):
    toplist,actorsize = controller.ActorsTop(control,N)
    print("Hay " + str(actorsize)+" actores.")
    print("Top",N,"actores con más participaciones:")
    tabla1 = PrettyTable()
    tabla1.field_names = ["actor","count","top_listed_in"]
    tabla2 = PrettyTable()
    tabla2.field_names = ["actor","content_type"]
    tabla2._max_width = {"content_type":30}
    tabla3 = PrettyTable()
    tabla3.field_names = ["actor","colaborations"]
    tabla3._max_width = {"colaborations":120}
    tabla1.hrules = ALL
    tabla2.hrules = ALL
    tabla3.hrules = ALL
    str_actores = ""
    for i in lt.iterator(toplist):
        name,colaborations,stream_show_tvCount,max_genre,size = i
        tabla1.add_row([name,size,max_genre[0]])
        tabla2.add_row([name,stream_show_tvCount])
        for actores in range (1, lt.size(colaborations)+1):
            x = lt.getElement(colaborations, actores)
            if x.strip() != "":
                if actores == lt.size(colaborations):
                    str_actores += x + "."
                else:
                    str_actores += x + ","
        tabla3.add_row([name,str_actores])
        str_actores = ""
    print(tabla1)
    print(tabla2)
    print(tabla3) 
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista de las películas estrenadas en un periodo de tiempo")
    print("3- Lista de programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido por país")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el top de géneros con