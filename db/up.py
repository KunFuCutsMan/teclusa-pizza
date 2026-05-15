import sqlite3

# La base de datos está graficada en el archivo "Diagrama Base DatosTECLUSA Pizza.drawio"
# Se puede ver el archivo en https://app.diagrams.net/
if __name__ == "__main__":
    con = sqlite3.connect("./database.db")
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS EstadosOrdenes(
            EstadoOrdenID int PRIMARY KEY,
            Nombre text NOT NULL
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Ordenes(
            OrdenID int PRIMARY KEY,
            FechaCreacion DATETIME NOT NULL,
            EstadoOrdenID int NOT NULL,
            CONSTRAINT fk_Ordenes_EstadosOrdenes
                FOREIGN KEY (EstadoOrdenID)
                REFERENCES EstadosOrdenes(EstadoOrdenID)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS SeccionesMenu(
            SeccionID int PRIMARY KEY,
            Nombre text NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Platillos(
            PlatilloID int PRIMARY KEY,
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