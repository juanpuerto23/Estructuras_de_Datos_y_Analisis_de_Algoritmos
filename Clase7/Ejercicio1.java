import java.util.*;

class Punto 
{
    int x, y;
    Punto(int x, int y) 
    {
        this.x = x;
        this.y = y;
    }
}

public class Ejercicio1 {

    public static double distancia(Punto p1, Punto p2) 
    {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }

    public static List<Punto> cercaniaMasCercana(List<Punto> puntos) 
    {
        if (puntos.size() <= 3) 
        {
            return fuerzaBruta(puntos);
        }

        List<Punto> puntosOrdenadosX = new ArrayList<>(puntos);
        List<Punto> puntosOrdenadosY = new ArrayList<>(puntos);
        Collections.sort(puntosOrdenadosX, Comparator.comparingInt(p -> p.x));
        Collections.sort(puntosOrdenadosY, Comparator.comparingInt(p -> p.y));

        List<Punto> cercanosIzquierda = cercaniaMasCercana(puntosOrdenadosX.subList(0, puntos.size() / 2));
        List<Punto> cercanosDerecha = cercaniaMasCercana(puntosOrdenadosX.subList(puntos.size() / 2, puntos.size()));

        double d = Math.min(distancia(cercanosIzquierda.get(0), cercanosIzquierda.get(1)),
                            distancia(cercanosDerecha.get(0), cercanosDerecha.get(1)));

        List<Punto> cercanos = (distancia(cercanosIzquierda.get(0), cercanosIzquierda.get(1)) < 
                                distancia(cercanosDerecha.get(0), cercanosDerecha.get(1))) ? cercanosIzquierda : cercanosDerecha;

        List<Punto> puntosEnRango = new ArrayList<>();
        int puntoMedioX = puntosOrdenadosX.get(puntos.size() / 2).x;

        for (Punto p : puntosOrdenadosY) 
        {
            if (Math.abs(p.x - puntoMedioX) < d) 
            {
                puntosEnRango.add(p);
            }
        }

        for (int i = 0; i < puntosEnRango.size(); i++) {
            for (int j = i + 1; j < Math.min(i + 8, puntosEnRango.size()); j++) {
                double distanciaActual = distancia(puntosEnRango.get(i), puntosEnRango.get(j));
                if (distanciaActual < d) {
                    d = distanciaActual;
                    cercanos = new ArrayList<>();
                    cercanos.add(puntosEnRango.get(i));
                    cercanos.add(puntosEnRango.get(j));
                }
            }
        }

        return cercanos;
    }

    public static List<Punto> fuerzaBruta(List<Punto> puntos) {
        List<Punto> mejorPar = new ArrayList<>();
        double mejorDistancia = Double.MAX_VALUE;

        for (int i = 0; i < puntos.size(); i++) {
            for (int j = i + 1; j < puntos.size(); j++) {
                double d = distancia(puntos.get(i), puntos.get(j));
                if (d < mejorDistancia) {
                    mejorDistancia = d;
                    mejorPar.clear();
                    mejorPar.add(puntos.get(i));
                    mejorPar.add(puntos.get(j));
                }
            }
        }

        return mejorPar;
    }

    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese cuántos pares de coordenadas desea registrar: ");
        int numPares = scanner.nextInt();

        List<Punto> listaPuntos = new ArrayList<>();

        for (int i = 0; i < numPares; i++) 
        {
            System.out.print("Ingrese la coordenada x del punto " + (i+1) + ": ");
            int x = scanner.nextInt();

            System.out.print("Ingrese la coordenada y del punto " + (i+1) + ": ");
            int y = scanner.nextInt();

            listaPuntos.add(new Punto(x, y));
        }

        long tiempoInicial = System.currentTimeMillis();
        List<Punto> paresCercanos = cercaniaMasCercana(listaPuntos);
        long tiempoFinal = System.currentTimeMillis();

        double tiempoTranscurrido = (tiempoFinal - tiempoInicial) / 1000.0;

        System.out.println("Los puntos más cercanos son (" + paresCercanos.get(0).x + ", " + paresCercanos.get(0).y + ") y (" + paresCercanos.get(1).x + ", " + paresCercanos.get(1).y + ")");
        System.out.println("La distancia mínima es: " + distancia(paresCercanos.get(0), paresCercanos.get(1)));
        System.out.println("Tiempo transcurrido: " + String.format("%.6f", tiempoTranscurrido) + " segundos");
    
    }
}