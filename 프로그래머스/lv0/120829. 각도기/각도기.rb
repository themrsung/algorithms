def solution(angle)
    if (angle < 90)
        return 1
    end
    if (angle == 90)
        return 2
    end
    if (angle < 180)
        return 3
    end
    if (angle == 180)
        return 4
    end
end