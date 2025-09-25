import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Obtener todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables = cursor.fetchall()

print("=== TODAS LAS TABLAS EN LA BASE DE DATOS ===")
for table in tables:
    table_name = table[0]
    print(f"📋 {table_name}")
    
print("\n=== VERIFICANDO TABLA SOLICITUDES ===")
try:
    cursor.execute("SELECT COUNT(*) FROM solicitudes_solicitud;")
    count = cursor.fetchone()[0]
    print(f"✅ Tabla 'solicitudes_solicitud' existe")
    print(f"📊 Total de registros: {count}")
    
    if count > 0:
        cursor.execute("SELECT id, nombre_solicitante, tipo_solicitud, fecha_solicitud FROM solicitudes_solicitud ORDER BY fecha_solicitud DESC LIMIT 5;")
        records = cursor.fetchall()
        print("\n🔍 Últimos 5 registros:")
        for record in records:
            print(f"   ID: {record[0]}")
            print(f"   Nombre: {record[1]}")  
            print(f"   Tipo: {record[2]}")
            print(f"   Fecha: {record[3]}")
            print("   ---")
            
except sqlite3.OperationalError as e:
    print(f"❌ Error: {e}")

conn.close()