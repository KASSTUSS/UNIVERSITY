using System;

public class A
{
    private int
                    a = 10,
                    b = 5; // поля класса

    public float c // свойство - умножение
    {
        get
        {
            return a *= b;
        }
    }
}

public class A1
{
    private int
                    a = 10,
                    b = 5; // поля класса

    public float c // свойство - вычитание
    {
        get
        {
            return a -= b;
        }
    }
}

public class Program
{
    public static void Main()
    {
        A a = new A0();
        A1 b = new A1();

        Console.WriteLine(a.c);
        Console.WriteLine(b.c);
    }
}
