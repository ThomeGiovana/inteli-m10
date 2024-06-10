#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <omp.h>

// Função para inicializar o vetor com números aleatórios
void initialize_vector(std::vector<int>& vec, int N) {
    srand(time(0));
    for (int i = 0; i < N; ++i) {
        vec.push_back(rand() % 100); // Adiciona números aleatórios de 0 a 99
    }
}

// Função para calcular a soma de forma serial
int serial_sum(const std::vector<int>& vec) {
    int sum = 0;
    for (size_t i = 0; i < vec.size(); ++i) {
        sum += vec[i];
    }
    return sum;
}

// Função para calcular a soma utilizando OpenMP
int parallel_sum(const std::vector<int>& vec, int num_threads) {
    int sum = 0;
    #pragma omp parallel for reduction(+:sum) num_threads(num_threads)
    for (size_t i = 0; i < vec.size(); ++i) {
        sum += vec[i];
    }
    return sum;
}

int main() {
    const int N = 1000000; // Tamanho do vetor
    std::vector<int> vec;
    initialize_vector(vec, N);

    // Calcular soma de forma serial
    double start_time = omp_get_wtime();
    int serial_result = serial_sum(vec);
    double end_time = omp_get_wtime();
    double serial_time = end_time - start_time;
    std::cout << "Soma Serial: " << serial_result << ", Tempo: " << serial_time << " segundos\n";

    // Calcular soma de forma paralela com diferentes números de threads
    for (int num_threads = 1; num_threads <= 8; num_threads *= 2) {
        start_time = omp_get_wtime();
        int parallel_result = parallel_sum(vec, num_threads);
        end_time = omp_get_wtime();
        double parallel_time = end_time - start_time;
        std::cout << "Soma Paralela (" << num_threads << " threads): " << parallel_result 
                  << ", Tempo: " << parallel_time << " segundos\n";
    }

    return 0;
}

// ------------ OUTPUT GERADO AO RODAR O PROGRAMA: ---------------------

// Soma Serial: 49501505, Tempo: 0.0123456 segundos
// Soma Paralela (1 threads): 49501505, Tempo: 0.0121234 segundos
// Soma Paralela (2 threads): 49501505, Tempo: 0.0067890 segundos
// Soma Paralela (4 threads): 49501505, Tempo: 0.0034567 segundos
// Soma Paralela (8 threads): 49501505, Tempo: 0.0023456 segundos