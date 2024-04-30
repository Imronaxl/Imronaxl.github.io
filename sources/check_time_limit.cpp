#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <unistd.h>
#include <sys/resource.h>
#include <sys/wait.h>

using namespace std;
using namespace chrono;

void sum_positive_numbers(const vector<int>& arr) {
    int total = 0;
    for (int num : arr) {
        if (num > 0) {
            total += num;
        }
    }
}

int main() {
    ifstream inputFile("input.txt"); // Открываем файл для чтения
    int n;
    inputFile >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        inputFile >> arr[i];
    }
    inputFile.close(); // Закрываем файл

    pid_t child_pid = fork();
    if (child_pid == 0) {
        // Child process
        struct rlimit rl;
        getrlimit(RLIMIT_CPU, &rl);
        rl.rlim_cur = 1;  // Устанавливаем ограничение времени на 1 секунду
        setrlimit(RLIMIT_CPU, &rl);

        sum_positive_numbers(arr);
        exit(0);
    } else {
        // Parent process
        int status;
        waitpid(child_pid, &status, 0);

        if (WIFSIGNALED(status) && WTERMSIG(status) == SIGXCPU) {
            cout << "Time limit exceeded" << endl;
        }
    }

    return 0;
}