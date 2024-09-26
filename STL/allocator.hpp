#include <iostream>
#include <memory>
#include <limits>
#include <cstddef>

template <typename T>
class Allocator {
public:
    using value_type = T;

    Allocator() noexcept {}

    template <typename U>
    Allocator(const Allocator<U>&) noexcept {}

    T* allocate(std::size_t n) {
        if (n > std::numeric_limits<std::size_t>::max() / sizeof(T)) {
            throw std::bad_alloc();
        }
        if (auto p = static_cast<T*>(std::malloc(n * sizeof(T)))) {
            return p;
        }
        throw std::bad_alloc();
    }

    void deallocate(T* p, std::size_t) noexcept {
        std::free(p);
    }

    template <typename U, typename... Args>
    void construct(U* p, Args&&... args) {
        new (p) U(std::forward<Args>(args)...);
    }

    template <typename U>
    void destroy(U* p) {
        p->~U();
    }

    template <typename U>
    struct rebind {
        using other = CustomAllocator<U>;
    };

    bool operator==(const Allocator& other) const noexcept {
        return true; // Can add state comparison if needed
    }

    bool operator!=(const Allocator& other) const noexcept {
        return !(*this == other);
    }
};

// Example of using the Allocator
int main() {
    Allocator<int> allocator;

    // Allocate memory for 5 integers
    int* arr = allocator.allocate(5);

    // Construct integers in allocated memory
    for (int i = 0; i < 5; ++i) {
        allocator.construct(&arr[i], i + 1); // Initialize with 1, 2, 3, 4, 5
    }

    // Print the integers
    for (int i = 0; i < 5; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // Destroy the integers
    for (int i = 0; i < 5; ++i) {
        allocator.destroy(&arr[i]);
    }

    // Deallocate memory
    allocator.deallocate(arr, 5);

    return 0;
}