using System;

public class Solution {
    public int solution(int num1, int num2) {
        switch (num1 == num2) {
            case true:
                return 1;
            case false:
                return -1;
        }
        
        return 0;
    }
}