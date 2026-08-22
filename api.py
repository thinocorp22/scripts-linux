from flask import Flask, jsonify, request
import re
import random
import string

app = Flask(__name__)

# 1. Ruta principal de la API de Seguridad
@app.route('/')
def home():
    return jsonify({
        "sistema": "API de Ciberseguridad - El Rincón de las Esquinas",
        "autor": "thinocorp22",
        "estado": "Protegido y Activo",
        "endpoints_disponibles": [
            "/api/security/check-password?pwd=TU_CONTRASEÑA",
            "/api/security/generate-password",
            "/api/security/audit-info"
        ]
    })

# 2. Endpoint para evaluar la seguridad de una contraseña
@app.route('/api/security/check-password', methods=['GET'])
def check_password():
    password = request.args.get('pwd', '')
    
    if not password:
        return jsonify({"error": "Por favor provee una contraseña usando el parámetro ?pwd=tu_password"}), 400

    # Criterios de seguridad
    longitud = len(password) >= 8
    tiene_mayus = bool(re.search(r'[A-Z]', password))
    tiene_minus = bool(re.search(r'[a-z]', password))
    tiene_num = bool(re.search(r'[0-9]', password))
    tiene_especial = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    puntaje = sum([longitud, tiene_mayus, tiene_minus, tiene_num, tiene_especial])
    
    nivel = "Débil"
    if puntaje >= 4:
        nivel = "Fuerte"
    elif puntaje == 3:
        nivel = "Moderada"

    return jsonify({
        "password_evaluada": password,
        "nivel_seguridad": nivel,
        "puntaje": f"{puntaje}/5",
        "recomendaciones": {
            "longitud_minima_8": longitud,
            "contiene_mayusculas": tiene_mayus,
            "contiene_minusculas": tiene_minus,
            "contiene_numeros": tiene_num,
            "contiene_caracteres_especiales": tiene_especial
        }
    })

# 3. Endpoint para generar una contraseña segura automáticamente
@app.route('/api/security/generate-password', methods=['GET'])
def generate_password():
    longitud = int(request.args.get('length', 12))
    if longitud < 8:
        longitud = 8 # Mínimo recomendado por seguridad

    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd_segura = "".join(random.choice(caracteres) for _ in range(longitud))

    return jsonify({
        "longitud": longitud,
        "password_generada": pwd_segura,
        "aviso": "Guarda esta contraseña en un lugar seguro."
    })

# 4. Información de buenas prácticas defensivas
@app.route('/api/security/audit-info', methods=['GET'])
def audit_info():
    return jsonify({
        "buenas_practicas_defensivas": [
            "Usa autenticación de dos factores (2FA) en todos tus servicios.",
            "Evita reutilizar contraseñas en diferentes plataformas.",
            "Mantén tus dependencias y herramientas (como Termux y paquetes) actualizadas.",
            "Implementa HTTPS y cabeceras de seguridad en tus despliegues web."
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

