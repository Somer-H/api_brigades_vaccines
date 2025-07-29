import time
import jwt
from dotenv import load_dotenv
load_dotenv()
import os 
secret_key = os.getenv('SECRET_KEY')
def generateToken(username: str, role: str) -> str:
        payload = {
            "username": username,
            "role": role,
            "exp": time.time() + 3600  
        }
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token

def validateToken(token: str, expected_roles: list = None):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
        if expected_roles:
            if not isinstance(decoded, dict):
             return False, {"error": "Token inválido (estructura incorrecta)"}
            role = decoded.get("role")
            if not isinstance(role, str):
             return False, {"error": "Claim 'role' inválido o ausente"}
            print(role)
            if role not in expected_roles:
             return False, {"error": "Rol no autorizado"}
        return True, decoded
    except jwt.ExpiredSignatureError:
        return False, {"error": "Token expirado"}
    except jwt.InvalidTokenError:
        return False, {"error": "Token inválido"}
import time
import jwt
from dotenv import load_dotenv
load_dotenv()
import os 
secret_key = os.getenv('SECRET_KEY')
def generateToken(username: str, role: str) -> str:
        payload = {
            "username": username,
            "role": role,
            "exp": time.time() + 3600  
        }
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token

def validateToken(token: str, expected_roles: list = None):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
        if expected_roles:
            if not isinstance(decoded, dict):
             return False, {"error": "Token inválido (estructura incorrecta)"}
            role = decoded.get("role")
            if not isinstance(role, str):
             return False, {"error": "Claim 'role' inválido o ausente"}
            print(role)
            if role not in expected_roles:
             return False, {"error": "Rol no autorizado"}
        return True, decoded
    except jwt.ExpiredSignatureError:
        return False, {"error": "Token expirado"}
    except jwt.InvalidTokenError:
        return False, {"error": "Token inválido"}
