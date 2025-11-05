# src/Shared/create_users.py
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import bcrypt
from sqlalchemy import text
from src.Shared.mysql import SessionLocal

def create_demo_users():
    # Contraseñas personalizadas
    passwords = {
        'enfermero_demo': 'enfermero123',
        'paciente_demo': 'paciente123',
        'director_demo': 'director123'
    }
    
    db = SessionLocal()
    
    try:
        print("Conexión exitosa a la base de datos")
        
        db.execute(text("""
            DELETE FROM User 
            WHERE username IN ('enfermero_demo', 'paciente_demo', 'director_demo')
        """))
        
        # Generar hashes
        hashes = {}
        for username, password in passwords.items():
            hashes[username] = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Insertar usuarios
        db.execute(text(f"""
            INSERT INTO User (username, password, role, name, lastname, groupIdGroup)
            VALUES 
                ('enfermero_demo', '{hashes["enfermero_demo"]}', 'enfermero', 'María', 'González', 1),
                ('paciente_demo', '{hashes["paciente_demo"]}', 'paciente', 'Juan', 'Pérez', 1),
                ('director_demo', '{hashes["director_demo"]}', 'director', 'Carlos', 'Ramírez', 1)
        """))
        
        db.commit()
        
        
    except Exception as e:
        db.rollback()
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()
        print("Conexión cerrada a la base de datos")

if __name__ == "__main__":
    create_demo_users()