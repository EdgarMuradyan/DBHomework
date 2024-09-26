#include <iostream>
#include "allocator.hpp"
#include <memory>
#include <stdexcept>
#include <utility>

template <typename T>
class MyVector {
public:
    using value_type = T;
    using allocator_type = Allocator;

    MyVector(size_t initial_capacity = 2)
        : capacity_(initial_capacity), size_(0) {
        data_ = allocator_.allocate(capacity_);
    }

    ~MyVector() {
        clear();
        allocator_.deallocate(data_, capacity_);
    }

    void push_back(const T& value) {
        if (size_ >= capacity_) {
            resize(capacity_ * 2);
        }
        allocator_.construct(&data_[size_], value);
        ++size_;
    }

    void pop_back() {
        if (size_ > 0) {
            allocator_.destroy(&data_[--size_]);
        }
    }

    T& operator[](size_t index) {
        if (index >= size_) throw std::out_of_range("Index out of range");
        return data_[index];
    }

    size_t size() const {
        return size_;
    }

    size_t capacity() const {
        return capacity_;
    }

    void clear() {
        for (size_t i = 0; i < size_; ++i) {
            allocator_.destroy(&data_[i]);
        }
        size_ = 0;
    }

private:
    void resize(size_t new_capacity) {
        T* new_data = allocator_.allocate(new_capacity);
        size_t copy_size = size_;

        for (size_t i = 0; i < copy_size; ++i) {
            allocator_.construct(&new_data[i], std::move(data_[i])); // Move-construct
            allocator_.destroy(&data_[i]); // Destroy old element
        }

        allocator_.deallocate(data_, capacity_);
        data_ = new_data;
        capacity_ = new_capacity;
    }

    Allocator allocator_;
    T* data_;
    size_t size_;
    size_t capacity_;
};

// Example usage of MyVector
int main() {
    MyVector<int> vec;

    for (int i = 0; i < 10; ++i) {
        vec.push_back(i);
    }

    std::cout << "Vector contents: ";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;

    vec.pop_back(); // Remove the last element

    std::cout << "After pop_back: ";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;

    vec.clear(); // Clear the vector

    std::cout << "After clear, size: " << vec.size() << std::endl;

    return 0;
}