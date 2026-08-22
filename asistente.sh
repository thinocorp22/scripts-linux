#!/bin/bash

clear
echo "=========================================="
echo "   ¡Hola! Bienvenido a tu Asistente Personal"
echo "=========================================="
echo ""

# Preguntar el nombre al usuario
read -p "¿Cómo te llamas?: " nombre
echo ""
echo "¡Un gusto saludarte, $nombre!"
echo "------------------------------------------"

# Menú interactivo
echo "Selecciona una opción para ejecutar:"
echo "1) Ver la fecha y hora actual"
echo "2) Ver el espacio libre en tu almacenamiento"
echo "3) Mostrar tu ubicación actual en la terminal"
echo ""

read -p "Escribe el número de tu opción (1, 2 o 3): " opcion

echo ""
echo "------------------------------------------"
case $opcion in
    1)
        echo "📅 La fecha y hora actual es:"
        date
        ;;
    2)
        echo "💾 Estado de tu almacenamiento:"
        df -h .
        ;;
    3)
        echo "📁 Te encuentras actualmente en:"
        pwd
        ;;
    *)
        echo "❌ Opción no válida. ¡Inténtalo de nuevo!"
        ;;
esac
echo "------------------------------------------"
echo "¡Gracias por usar tu asistente, $nombre!"

