fun processNumbers(numbers: List<Int>): Int {
    return numbers
        .filter { it % 2 != 0 }  // Keep only odd numbers
        .map { it * it }         // Square each number
        .sum()                   // Sum them up
}

fun main() {
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    val result = processNumbers(numbers)
    println("Processed result: $result")
}