using System;

public class A
{
    public int a, b; // поля класса

    public int C // свойство - умножение
    {
        get
        {
            return a *= b;
        }
    }
    public A(int a, int b)
    {
        this.a = a;
        this.b = b;
    }
    public A()
    {
        this.a = 5;
        this.b = 3;
    }
}

public class B : A
{
    private int[] arr;
    public int d;

    public B(int a, int b, int d) : base(a, b)
    {
        this.d = d;
    }
     public B()
    {
        this.a = 5;
        this.b = 3;
        this.d = 2;
    }
    public B(int a) : this(a, 3, 2)
    {
        arr = new int[a];
        for (int i = 0; i < a; i++)
        {
            arr[i] = C2 * i;
        }
    }

    public int C2
    {
        get
        {
            int temp = 0;
            for (int i = 0; i < this.d; i++)
                temp += this.C;

            return temp;
        }
    }
    public int[] ARR
    {
        get { return arr; }
    }
}
public class Program
{
    public static void Main()
    {
        B ObjectB = new B(5);
        foreach (float i in ObjectB.ARR) Console.WriteLine(i);
    }
}
