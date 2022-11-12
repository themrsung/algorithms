function solution(num_list) {
    let even_count = 0
    let odd_count = 0
    
    for (let i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2 == 0) {
            even_count++
        }
    }
    
    odd_count = num_list.length - even_count
    
    return [even_count, odd_count]
}