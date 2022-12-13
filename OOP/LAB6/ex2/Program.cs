using System;
using System.Collections;

namespace lab6
{
    public interface GeometricFigure
    {
        double Area { get; }
        string Info(int num);
    }

    public class ArrOfFigures : IEnumerable
    {
        string[] figures;
        public ArrOfFigures(string[] gf)
        {
            figures = gf;
        }
        IEnumerator IEnumerable.GetEnumerator()
        {
            return figures.GetEnumerator();
        }
    }

    public class Square : GeometricFigure
    {
        private int side;
        public Square(int side)
        {
            this.side = side;
        }
        public int Side
        {
            get { return side; }
        }
        public double Area
        {
            get { return Side * Side; }
        }
        public int Perimetr
        {
            get { return 4 * Side; }
        }
        public string Info(int num)
        {
            string num_figure = "Квадрат " + num + "\n\n";
            string s = "Сторона квадрата: " + Side + "\n";
            string p = "Периметр квадрата: " + Perimetr + "\n";
            string a = "Площадь квадрата: " + Area + "\n";
            return "\n" + num_figure + s + p + a;
        }
    }

    public class Circle : GeometricFigure
    {
        private int radius;
        private string color;
        public Circle(int radius, string color)
        {
            this.radius = radius;
            this.color = color;
        }
        public int Radius
        {
            get { return radius; }
        }
        public string Color
        {
            get { return color; }
        }
        public double Area
        {
            get { return 3.14 * radius * radius; }
        }
        public string Info(int num)
        {
            string num_figure = "Круг " + num + "\n\n";
            string r = "Радиус круга: " + Radius + "\n";
            string c = "Цвет круга: " + Color + "\n";
            string a = "Площадь круга: " + Area + "\n";
            return "\n"+ num_figure + r + c + a;
        }
    }

    public class Program
    {
        public static void Main()
        {
            Square figure1 = new Square(10);
            Square figure2 = new Square(13);
            Circle figure3 = new Circle(15, "blue");
            Circle figure4 = new Circle(3, "white");
            string div = "----------------------------";
            string[] figures = new string[] {figure1.Info(1), div,
                                         figure2.Info(2), div,
                                         figure3.Info(1),div,
                                         figure4.Info(2)};

            ArrOfFigures arr = new ArrOfFigures(figures);
            foreach (string a in arr)
            {
                Console.WriteLine(a);
            }
        }
    }
}
