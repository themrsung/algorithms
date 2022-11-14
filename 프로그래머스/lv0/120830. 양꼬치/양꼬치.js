function solution(n, k) {  
    let price = 0
    price += n * 12000
    price += k * 2000
    
    let comp_count = Math.floor(n / 10)
    let comp_price = comp_count * 2000
    
    price -= comp_price
    
    return price
}