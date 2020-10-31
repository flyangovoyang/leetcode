#include<iostream>
#include<vector>
using namespace std;

int binary_search(vector<int> v, int e)
{
    long left = 0, right = v.size() - 1, mid;
    while(left <= right)
    {
        mid = (left + right)/2;
        if(v[mid] == e)
        {
            return mid;
        }
        else if(v[mid] > e)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return -1;
}
