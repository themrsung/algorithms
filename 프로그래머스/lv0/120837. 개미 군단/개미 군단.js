function solution(hp) {
    let leftover = 0
    let general_count = Math.floor(hp / 5)
    leftover = hp % 5
    
    let sergeant_count = Math.floor(leftover / 3)
    leftover = leftover % 3
    
    let worker_count = leftover
    
    return general_count + sergeant_count + worker_count
}