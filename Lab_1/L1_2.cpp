#include <iostream>
#include "omp.h"
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[])
{
    if (argc > 1)
    {
        int size = atoi(argv[1]);
        
        double time_for_one_tread;
        double** a = new double* [size];
        double** b = new double* [size];
        double** c = new double* [size];
        
        for (int i = 0; i < size; ++i)
        {
            a[i] = new double[size];
            b[i] = new double[size];
            c[i] = new double[size];
        }
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                a[i][j] = (double(rand()) / RAND_MAX);
                b[i][j] = (double(rand()) / RAND_MAX);
            }
        }
        for (int num = 1; num <= 10; num++)
        {
            for (int i = 0; i < num; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    c[i][j] = 0;
                }
            }
            double exec_start_time = omp_get_wtime();
#pragma omp parallel for num_threads(num)
            for (int k = 0; k < size; k++)
            {
                for (int j = 0; j < size; j++)
                {
                    for (int i = 0; i < size; i++)
                    {
                        c[i][j] = c[i][j] + a[i][k] * b[k][j];
                    }
                }
            }
            double exec_time = (double)(omp_get_wtime() - exec_start_time);
            if (num == 1)
            {
            time_for_one_tread = exec_time;
            }
            double efficiency = time_for_one_tread / exec_time;
            cout << "Number of threads: " << num << "  Execution time (in microseconds): " <<  exec_time << "  Efficiency: " << efficiency << endl;
        }
    }
    else
    {
        cout << "Please input the arguments" << endl;
    }
    return 0;
}