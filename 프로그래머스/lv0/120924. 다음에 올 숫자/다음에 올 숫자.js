function solution(common) {
    // if (common[common.length - 1] % common[common.length -2] == 0) {
    //     let power = common[common.length - 1] / common[common.length - 2]
    //     return common[common.length - 1] * power
    // }
    // else {
    //     let delta = common[common.length - 1] - common[common.length - 2]
    //     return common[common.length - 1] + delta
    // }
    
    let delta_1 = common[common.length - 1] - common[common.length - 2]
    let delta_2 = common[common.length - 2] - common[common.length - 3]
    if (delta_1 == delta_2) {
        return common[common.length - 1] + delta_1
    }
    else {
        let power = common[common.length - 1] / common[common.length - 2]
        return common[common.length - 1] * power
    }
}