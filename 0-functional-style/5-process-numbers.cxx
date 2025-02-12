#include <iostream>
#include <vector>
#include <ranges>
#include <numeric>

int processNumbers(const std::vector<int>& numbers) {
    auto filtered = numbers | std::views::filter([](int x) { return x % 2 != 0; })
                             | std::views::transform([](int x) { return x * x; });

    return std::accumulate(filtered.begin(), filtered.end(), 0);
}

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result = processNumbers(numbers);

    std::cout << "Processed result: " << result << std::endl;
    return 0;
}