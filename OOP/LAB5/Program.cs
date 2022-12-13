using System;
public class B
{
    private int x;
    private int y;
    public B(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    public static bool operator true(B obj)
    {
        return (obj.x > 0 && obj.y > 0);
    }
    public static bool operator false(B obj)
    {
        return (obj.x < 0 || obj.y < 0);
    }
    public static bool operator &(B objA, B objB)
    {
        if (objA.x > 0 && objA.y > 0 && objB.x > 0 && objB.y > 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}


public class Program
{
    public static void Main()
    {
        B objectA = new(1, 1);
        B objectB = new(1, -1);
        if (objectA)
        {
            Console.WriteLine("true");
        }
        else
        {
            Console.WriteLine("false");
        }


        if (objectB)
        {
            Console.WriteLine("true");
        }
        else
        {
            Console.WriteLine("false");
        }

        if (objectB & objectA)
        {
            Console.WriteLine("true");
        }
        else
        {
            Console.WriteLine("false");
        }
    }
}
