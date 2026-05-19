from conn import con

# La base de datos está graficada en el archivo "Diagrama Base DatosTECLUSA Pizza.drawio"
# Se puede ver el archivo en https://app.diagrams.net/
if __name__ == "__main__":
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS EstadosOrdenes(
            EstadoOrdenID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre text NOT NULL
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Ordenes(
            OrdenID INTEGER PRIMARY KEY AUTOINCREMENT,
            Notas text NOT NULL,
            FechaCreacion DATETIME NOT NULL,
            EstadoOrdenID int NOT NULL,
            CONSTRAINT fk_Ordenes_EstadosOrdenes
                FOREIGN KEY (EstadoOrdenID)
                REFERENCES EstadosOrdenes(EstadoOrdenID)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS SeccionesMenu(
            SeccionID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre text NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Platillos(
            PlatilloID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre text NOT NULL,
            Descripcion text NOT NULL,
            Precio int NOT NULL,
            SeccionID int,
            CONSTRAINT fk_Platillos_SeccionesMenu
                FOREIGN KEY (SeccionID)
                REFERENCES SeccionesMenu(SeccionID),
            CONSTRAINT chk_Platillos_PrecioPositivo
                CHECK( Precio > 0 )
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS PlatillosOrdenes(
            PlatilloID int,
            OrdenID int,
            Cantidad int,
            CONSTRAINT PK_PlatillosOrdenes
                PRIMARY KEY (PlatilloID, OrdenID),
            CONSTRAINT fk_PlatillosOrdenes_Platillos
                FOREIGN KEY (PlatilloID)
                REFERENCES Platillos(PlatilloID),
            CONSTRAINT fk_PlatillosOrdenes_Ordenes
                FOREIGN KEY (OrdenID)
                REFERENCES Platillos(OrdenID),
            CONSTRAINT chk_PlatillosOrdenes_CantidadPositiva
                CHECK( Cantidad > 0 )
        )
    """)

    cur.executemany("INSERT INTO EstadosOrdenes VALUES(?, ?)",[
        (1, "En espera"),
        (2, "En Proceso"),
        (3, "Lista"),
        (4, "Entregada"),
        (5, "Cancelada"),
    ])
    con.commit()

    cur.executemany("INSERT INTO SeccionesMenu VALUES(?, ?)", [
        (1, "Platos Principales"),
        (2, "Entradas"),
        (3, "Aperititos"),
        (4, "Bebidas"),
    ])
    con.commit()