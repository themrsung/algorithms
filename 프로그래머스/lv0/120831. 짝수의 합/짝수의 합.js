function solution(n) {
    let num_list = []
    
    for (let i = 0; i <= n; i++) {
        if (i % 2 == 0) {
            num_list.push(i)
        }
    }
    
    let tally = 0
    for (let i = 0; i < num_list.length; i++) {
        tally += num_list[i]
    }
    
    return tally
}