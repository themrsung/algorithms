function solution(num) {
    let iterations = 0
    while (iterations < 500 && num > 1) {
        num = (num % 2 == 0) ? num / 2 : num * 3 + 1
        iterations++
    }
    return iterations == 500 ? -1 : iterations
}