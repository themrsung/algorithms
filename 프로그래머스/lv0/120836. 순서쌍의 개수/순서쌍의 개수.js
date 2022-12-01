function solution(n) {
    let cnt = 0
    for(let i = 0; i < n; i++) {
        const isSSS = (n % (i + 1) == 0)
        if (isSSS) {
            cnt++
        }
    }
    
    return cnt
}