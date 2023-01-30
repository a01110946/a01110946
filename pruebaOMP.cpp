#include <iostream>
#include <omp.h>

#define N 1000
# define chunk 100
# define mostrar 100

void imprimeArreglo(float *d);

int main()
{
    std::cout << "Sumando arreglos en paralelo!\n";
    float a[N], b[N], c[N];
    int i;
    
    for (i = 0; i < N; i++)  // Inicializar los arreglos a y b con valores
    {
        a[i] = i * 20;
        b[i] = (i - 5) * 2 ;
    }
    int pedazos = chunk;
    
    #pragma omp parallel for shared(a, b, c, pedazos) private(i) schedule(static, pedazos)  // Sumar los elementos de los arreglos a y b y asignarlos al arreglo c
    for (i = 0; i < N; i++)
        c[i] = a[i] + b[i];

    std::cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo a: " << std::endl;
    imprimeArreglo(a);
    std::cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo b: " << std::endl;
    imprimeArreglo(b);
    std::cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo c: " << std::endl;
    imprimeArreglo(c);
}

void imprimeArreglo(float* d)  // Imprimir los elementos del arreglo c
{
    for (int x = 0; x < mostrar; x++)
        std::cout << d[x] << " - ";
    std::cout << std::endl;
}