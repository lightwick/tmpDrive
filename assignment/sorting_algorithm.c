#include <stdio.h>
#include <stdlib.h>
#define ARR_SIZE 100
// [순차 정렬(Sequential Sort), 버블 정렬(Bubble Sort), 삽입 정렬(Insertion Sort), 선택 정렬(Selection Sort), 병합 정렬(Merge Sort), 퀵 정렬(Quick Sort) ]

void swap(int arr[ARR_SIZE], int idx_1, int idx_2) {
    int tmp = arr[idx_1];
    arr[idx_1] = arr[idx_2];
    arr[idx_2] = tmp;
}

void print_array(int arr[ARR_SIZE]) {
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%d ", arr[i]);
        if ((i + 1) % 10 == 0) printf("\n");
    }
}

void sequential_sort(int arr[ARR_SIZE]) {
}

void bubble_sort(int arr[ARR_SIZE]) {
    for (int i = ARR_SIZE - 1; i >= 1; i--) {
        for (int j = i; j >= 1; j--) {
            if (arr[j - 1] > arr[j]) swap(arr, j - 1, j);
        }
    }
}

void insertion_sort(int arr[ARR_SIZE]) {
}

void selection_sort(int arr[ARR_SIZE]) {
    for (int i = 0; i < ARR_SIZE - 1; i++) {
        int idx = i;
        for (int j = i + 1; j < ARR_SIZE; j++) {
            if (arr[idx] > arr[j]) {
                idx = j;
            }
        }
        swap(arr, i, idx);
    }
}

void merge_sort(int arr[ARR_SIZE]) {
}

void quick_sort(int arr[ARR_SIZE]) {
}

void shuffle(int arr[ARR_SIZE]) {
    // Fisher–Yates shuffle
    // the array index exists: 0 .. ARR_SIZE-1
    for (int i = 0; i < ARR_SIZE - 1; i++) {
        // j is a random number between i and ARR_SIZE-1, inclusive
        int j = rand() % (ARR_SIZE - i) + i;
        swap(arr, i, j);
    }
}

int main() {
    int arr[ARR_SIZE];
    for (int i = 0; i < ARR_SIZE; i++) {
        arr[i] = i + 1;
    }

    shuffle(arr);
    printf("original array:\n");
    print_array(arr);
    printf("\n");

    // TODO use sort and print result
    // selection_sort(arr);
    bubble_sort(arr);

    printf("sorted_array:\n");
    print_array(arr);

    return 0;
}
