import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("./database.db")
    cur = con.cursor()

    # cur.execute("ALTER TABLE PlatillosOrdenes DROP PRIMARY KEY")
    # cur.execute("ALTER TABLE PlatillosOrdenes DROP CONSTRAINT fk_PlatillosOrdenes_Platillos")
    # cur.execute("ALTER TABLE PlatillosOrdenes DROP CONSTRAINT fk_PlatillosOrdenes_Ordenes")
    # cur.execute("ALTER TABLE PlatillosOrdenes DROP CONSTRAINT chk_PlatillosOrdenes_CantidadPositiva")
    cur.execute("DROP TABLE IF EXISTS PlatillosOrdenes")

    # cur.execute("ALTER TABLE Platillos DROP PRIMARY KEY")
    # cur.execute("ALTER TABLE Platillos DROP CONSTRAINT fk_Platillos_SeccionesMenu")
    # cur.execute("ALTER TABLE Platillos DROP CONSTRAINT chk_Platillos_PrecioPositivo")
    cur.execute("DROP TABLE IF EXISTS Platillos")

    cur.execute("DROP TABLE IF EXISTS SeccionesMenu")

    # cur.execute("ALTER TABLE Ordenes DROP PRIMARY KEY")
    # cur.execute("ALTER TABLE Ordenes DROP CONSTRAINT fk_Ordenes_EstadosOrdenes")
    cur.execute("DROP TABLE IF EXISTS Ordenes")

    cur.execute("DROP TABLE IF EXISTS EstadosOrdenes")