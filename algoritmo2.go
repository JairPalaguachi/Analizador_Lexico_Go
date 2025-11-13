// Algoritmo 2 - Prueba de Estructuras de Control
// Autor: Javier Gutiérrez (SKEIILATT)
// Descripción: Este algoritmo prueba condicionales, bucles y switch en Go

func calcularPromedio(nota1 int, nota2 int) int {
    return (nota1 + nota2) / 2
}

func evaluarNota(puntos int) string {
    if puntos >= 90 {
        return "Excelente"
    } else if puntos >= 70 {
        return "Bueno"
    }
    return "Regular"
}