using System;

public class A
{
    public  int a, b; // поля класса

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
        this.a = 10;
        this.b = 5;
    }
}

public class B : A
{
    public int d;

    public B(int a, int b, int d) : base(a, b)
    {
        this.d = d;
    }
    public B() : this(10, 5, 2)
    {
        this.d = 2;
    }

    public float C2
    {
        get
        {
            int temp = 0;
            for(int i = 0; i < this.d; i++)
                temp += this.C;

            return temp;
        }
    }

    class Program
    {
        public static void Main()
        {
            A MyObject = new A(2, 3);

            B ObjectB1 = new B();
            B ObjectB2 = new B(2, 3, 5);
            Console.WriteLine("Object     \t a \t | \t b \t | \t d \t |");
            Console.WriteLine("----------------------------------------------------------");
            Console.WriteLine(string.Format("ObjectB1 \t {0} \t | \t {1} \t | \t {2} \t |",
                                            ObjectB1.a, ObjectB1.b, ObjectB1.d));
            Console.WriteLine("----------------------------------------------------------");
            Console.WriteLine(string.Format("ObjectB2 \t {0} \t | \t {1} \t | \t {2} \t |\n",
                                            ObjectB2.a, ObjectB2.b, ObjectB2.d));

            Console.WriteLine(string.Format("ObjectA:\n\n\tC result: {0}\n\n",
                                            MyObject.C));

            Console.WriteLine(string.Format("ObjectB1:\n\n\tC result: {0}\n\tC1 result: {1}\n\n",
                                            ObjectB1.C, ObjectB1.C2));

            Console.WriteLine(string.Format("ObjectB2:\n\n\tC result: {0}\n\tC1 result: {1}\n\n",
                                            ObjectB2.C, ObjectB2.C2));

            Console.WriteLine("\n\n\n\n\nClick the Enter to close the window...");
            Console.ReadLine();
        }
    }
}