function solution(slice, n) {
    let pizzas = 0
    for (let i = 0; i < n; i++) {
        if (i % slice == 0) {
            pizzas++
        }
    }
    return pizzas
}