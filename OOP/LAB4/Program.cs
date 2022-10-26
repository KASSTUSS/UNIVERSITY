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
    int[] array2 = new int[] { 1,2,3,4,5 };
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
    public int[] Array2
    {
        get { return array2; }
    }
    public int this[int index]
    {
        get
        {
            return arr[index];
        }
        set
        {
            arr[index] = value;
        }        
    }
    public int this[double index]
    {
        get
        {
            return array2[(int)index];
        }
        set
        {
            array2[(int)index] = value;
        }
    }
    
}
public class C<T>
{
    public static string message = "Static";
    private T[] arr = new T[5];
    public T this[int index]
    {
        get
        {
            return arr[index];
        }
        set
        {
            arr[index] = value;
        }
    }
}
public class Program
{
    public static void Main()
    {
        B ObjectB = new B(5);
        for (int i = 0; i < ObjectB.ARR.Length; i++)
        {
            Console.WriteLine(ObjectB[i]);
        }
        for (float i = 0; i < ObjectB.Array2.Length; i++)
        {
            Console.WriteLine(ObjectB[i]);
        }
        C<string> str_obj = new C<string>();
        C<int> int_obj = new C<int>();

        for (int i = 0; i < 3; i++)
        {
            str_obj[i] = Convert.ToString(i) + " num";
        }
        for (int i = 0; i < 3; i++)
        {
            int_obj[i] = i;
        }
        Console.WriteLine(C<int>.message);
        Console.WriteLine("Массив строк");
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine(str_obj[i]);
        }
        Console.WriteLine("Массив чисел");
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine(int_obj[i]);
        }
    }
}