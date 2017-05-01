public class seven
{
    static int prime(int index)
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
                        System.out.println(current);
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

    public static void main(String[] args)
    {
        System.out.println(prime(10001));
    }
}
