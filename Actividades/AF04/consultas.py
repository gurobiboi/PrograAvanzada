def buscar_info_artista(plataforma, artista_seleccionado):
    for genero in plataforma.hijos:
        for artista in genero.hijos:
            if artista.valor == artista_seleccionado:
                for album in artista.hijos:
                    print(f"Álbum: {album.valor}, {len(album.hijos)} cancion(es)")


def buscar_mejor_plataforma(genero, plataformas):
    num_canciones = {}
    for plataforma in plataformas:
        num_canciones[plataforma] = 0
        for genero_plat in plataforma.raiz.hijos:
            if genero == genero_plat.valor:
                for artista in genero_plat.hijos:
                    for album in artista.hijos:
                        num_canciones[plataforma] += len(album.hijos)
                break
    return max(num_canciones, key=num_canciones.get)
            


def buscar_artistas_parecidos(nombre_cancion, plataforma):
    lista_artistas = []
    genero_cancion = ""
    for genero in plataforma.hijos:
        for artista in genero.hijos:
            for album in artista.hijos:
                for cancion in album.hijos:
                    if cancion.valor.lower() == nombre_cancion.lower():
                        genero_cancion = cancion.padre.padre.padre.valor
                        break
    if genero_cancion == "":
        print("No existe aquella cancion en esta plataforma!")
        return None
    else:
        for genero in plataforma.hijos:
            if genero.valor == genero_cancion:
                for artista in genero.hijos:
                    lista_artistas.append(artista.valor)
        return lista_artistas
def crear_playlist(plataforma, genero_seleccionado, conceptos_canciones):
    playlist = []
    for genero in plataforma.hijos:
        if genero.valor == genero_seleccionado:
            for artista in genero.hijos:
                for album in artista.hijos:
                    for cancion in album.hijos:
                        tiene_concepto = False
                        for concepto in conceptos_canciones:
                            if concepto.lower() in cancion.valor.lower():
                                tiene_concepto = True
                        if tiene_concepto:
                            playlist.append(cancion.valor)
    return playlist
