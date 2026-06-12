#!/usr/bin/env python3

import requests
import sys
from urllib.parse import urlparse

def verificar_servidor(url):
    """Verifica si un servidor está activo"""
    # Asegurar que la URL tenga http:// si no lo tiene
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    print(f"\n🔍 Verificando: {url}")
    print("-" * 50)
    
    try:
        # Intentar con GET primero
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        print("⏳ Conectando...")
        response = requests.get(url, timeout=10, headers=headers, allow_redirects=True)
        
        # Verificar códigos de éxito
        if response.status_code in [200, 201, 202, 203, 204, 205, 206]:
            print(f"✅ SERVIDOR ACTIVO")
            print(f"📊 Código HTTP: {response.status_code}")
            print(f"⚡ Tiempo respuesta: {response.elapsed.total_seconds():.2f} segundos")
            return True
            
        elif response.status_code in [301, 302, 307, 308]:
            print(f"⚠️ SERVIDOR ACTIVO (Redirección)")
            print(f"📊 Código HTTP: {response.status_code}")
            if 'Location' in response.headers:
                print(f"🔄 Redirige a: {response.headers['Location']}")
            return True
            
        elif response.status_code in [401, 403]:
            print(f"⚠️ SERVIDOR ACTIVO (Requiere autenticación)")
            print(f"📊 Código HTTP: {response.status_code}")
            return True
            
        else:
            print(f"❌ SERVIDOR INACTIVO")
            print(f"📊 Código HTTP: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ SERVIDOR INACTIVO")
        print(f"🔌 Error: No se pudo establecer conexión")
        return False
        
    except requests.exceptions.Timeout:
        print(f"❌ SERVIDOR INACTIVO")
        print(f"⏰ Error: Tiempo de espera agotado (Timeout)")
        return False
        
    except requests.exceptions.SSLError:
        print(f"⚠️ PROBLEMA DE SSL")
        print(f"🔒 Error: Problema con certificado SSL")
        print("💡 Sugerencia: Verifica la URL o intenta con http://")
        return False
        
    except Exception as e:
        print(f"❌ SERVIDOR INACTIVO")
        print(f"❌ Error: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🔍 VERIFICADOR DE SERVIDORES - MODO INTERACTIVO")
    print("=" * 60)
    print("\nEjemplos de formato aceptado:")
    print("  • maxtvapps.pw:80")
    print("  • http://skytvpluzz.xyz:80")
    print("  • https://arestv.vip:443")
    print("  • 192.168.1.1:8080")
    print("-" * 60)
    
    while True:
        print("\n" + "=" * 60)
        servidor = input("🌐 Ingresa la URL del servidor (o 'salir' para terminar): ").strip()
        
        if servidor.lower() in ['salir', 'exit', 'quit', 'q']:
            print("\n👋 ¡Hasta luego!")
            break
        
        if not servidor:
            print("⚠️ Por favor ingresa una URL válida")
            continue
        
        # Verificar el servidor
        resultado = verificar_servidor(servidor)
        
        # Preguntar si quiere verificar otro
        if resultado:
            print("\n✨ El servidor está funcionando correctamente")
        else:
            print("\n💀 El servidor no está respondiendo")
        
        print("\n" + "-" * 60)
        continuar = input("¿Quieres verificar otro servidor? (s/n): ").strip().lower()
        if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
            print("\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
        sys.exit(0)