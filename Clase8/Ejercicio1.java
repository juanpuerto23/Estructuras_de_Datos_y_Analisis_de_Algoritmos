public class Ejercicio1 {

    static final int TAMANO_TABLERO = 8; 
    static int[] solucion = new int[TAMANO_TABLERO]; // Representa el tablero de ajedrez (8x8)

    // Función para imprimir la solución
    static void imprimirTablero() {
        for (int fila = 0; fila < TAMANO_TABLERO; fila++) {
            for (int columna = 0; columna < TAMANO_TABLERO; columna++) {
                if (solucion[fila] == columna)
                    System.out.print(" Q "); // Q representa una reina
                else
                    System.out.print(" - ");
            }
            System.out.println();
        }
        System.out.println();
    }

    // Función para verificar si es seguro colocar la reina en la posición (fila, columna)
    static boolean PosicionSegura(int fila, int columna) {
        int i, j;

        // Verificar la columna en la misma fila
        for (i = 0; i < fila; i++)
            if (solucion[i] == columna)
                return false;

        // Verificar la diagonal superior izquierda
        for (i = fila, j = columna; i >= 0 && j >= 0; i--, j--)
            if (solucion[i] == j)
                return false;

        // Verificar la diagonal superior derecha
        for (i = fila, j = columna; i >= 0 && j < TAMANO_TABLERO; i--, j++)
            if (solucion[i] == j)
                return false;

        return true;
    }

    // Función recursiva para resolver el problema de las N reinas
    static void resolver(int fila) {
        if (fila == TAMANO_TABLERO) {
            imprimirTablero();
            return;
        }

        for (int columna = 0; columna < TAMANO_TABLERO; columna++) {
            if (PosicionSegura(fila, columna)) {
                solucion[fila] = columna;
                resolver(fila + 1);
                solucion[fila] = -1; // Deshacer la elección si no lleva a una solución
            }
        }
    }

    public static void main(String[] args) {
        // Inicializar la solución
        for (int i = 0; i < TAMANO_TABLERO; i++) {
            solucion[i] = -1;
        }

        resolver(0);
    }
}
