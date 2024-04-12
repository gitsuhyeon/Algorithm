import java.util.List;
import java.util.LinkedList;
import java.util.Collections;

class Solution {
    public int solution(int n) {
        int answer = 0;
        int cmp1 = Integer.bitCount(n);
        while (true){
            n +=1;
            int cmp2 = Integer.bitCount(n);
            if (cmp1 == cmp2)
                return n;
            }
    }
}