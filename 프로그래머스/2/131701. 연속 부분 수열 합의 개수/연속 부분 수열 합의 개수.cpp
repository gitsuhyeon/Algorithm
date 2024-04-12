#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> elements) {
    int answer = 0;
    int n = elements.size();
    vector<int> a = elements;
    vector<int> b = elements;
    int j = 0;
    while(j<n-1){
        j++;
        for (int i=0;i<n;i++){
            int k = i+j;
            if (k >= n)
                k -= n;
            a[i] += elements[k];
        }
        b.insert(b.end(),a.begin(),a.end());
    }
    sort(b.begin(),b.end());
    b.erase(unique(b.begin(),b.end()),b.end());
    answer = b.size();
    return answer;
}
