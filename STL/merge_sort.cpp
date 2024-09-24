#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    // Create temporary vectors for left and right halves
    std::vector<int> leftVec(arr.begin() + left, arr.begin() + mid + 1);
    std::vector<int> rightVec(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0; // Initial index of first sub-array
    int j = 0; // Initial index of second sub-array
    int k = left; // Initial index of merged sub-array

    // Merge the temp arrays back into arr[left..right]
    while (i < leftVec.size() && j < rightVec.size()) {
        if (leftVec[i] <= rightVec[j]) {
            arr[k] = leftVec[i];
            i++;
        } else {
            arr[k] = rightVec[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of leftVec, if any
    while (i < leftVec.size()) {
        arr[k] = leftVec[i];
        i++;
        k++;
    }

    // Copy the remaining elements of rightVec, if any
    while (j < rightVec.size()) {
        arr[k] = rightVec[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        // Find the middle point
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}

int main() {
    std::vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

    std::cout << "Original array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    mergeSort(arr, 0, arr.size() - 1);

    std::cout << "Sorted array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    
    std::cout << std::endl;

    return 0;
}