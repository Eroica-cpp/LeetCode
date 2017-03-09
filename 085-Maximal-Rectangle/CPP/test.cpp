#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int n = 5;
    vector<int> H(n, n);
    for (int i = 0; i < H.size(); i ++)
        cout << H[i] << endl;

    return 0;
}