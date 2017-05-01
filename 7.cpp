#include <iostream>
using namespace std;

int prime(int index)
{
    int current = 2;
    int count = 2;
    while(true)
    {
        for(int i = 2; i < current; i++)
        {
            if(current % i == 0)
            {
                break;
            }
            if(i == current - 1)
            {
                if(count % 100 == 0)
                {
                    cout << current << endl;
                }
                count++;
            }
        }
        if(count > index)
        {
            return current;
        }
        else { current++;}
    }
}

int main()
{
    cout << prime(10001);

}
