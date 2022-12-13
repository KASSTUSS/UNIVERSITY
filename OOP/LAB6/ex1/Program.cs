using System;
using System.Collections.Generic;

namespace lab6
{
    public class Human
    {
        private string lastname;
        private int birth_year;
        private string status;

        public Human(string lastname,
                     int birth_year,
                     string status)
        {
            this.lastname = lastname;
            this.birth_year = birth_year;
            this.status = status;
        }
        public Human() : this("noname", 0, "noname")
        {
            this.lastname = "noname";
            this.birth_year = 0;
            this.status = "noname";
        }
        public string GSlastname
        {
            get { return lastname; }
            set { lastname = value; }
        }
        public int GSbirth_year
        {
            get { return birth_year; }
            set { birth_year = value; }
        }
        public string GSstatus
        {
            get { return status; }
            set { status = value; }
        }
        public virtual void Info()
        {
            DateTime d = DateTime.Now;
            Console.WriteLine("Возраст: " + (Convert.ToInt32(d.Year) - GSbirth_year));
        }
        public void About()
        {
            Console.WriteLine("");
            Console.WriteLine("Фамилия: " + GSlastname);
            Console.WriteLine("Год рождения: " + GSbirth_year);
            Info();
            Console.WriteLine("Статус: " + GSstatus);
        }
    }

    public class Student : Human
    {
        private int math_mark;
        private int phys_mark;
        private int hist_mark;

        public Student(string lastname,
                       int birth_year,
                       string status,
                       int math_ball,
                       int phys_ball,
                       int hist_ball) : base(lastname, birth_year, status)
        {
            this.math_mark = math_mark;
            this.phys_mark = phys_mark;
            this.hist_mark = hist_mark;
        }
        public int GSmath_mark
        {
            get { return math_mark; }
            set { math_mark = value; }
        }
        public int GSphys_mark
        {
            get { return phys_mark; }
            set { phys_mark = value; }
        }
        public int GShist_mark
        {
            get { return hist_mark; }
            set { hist_mark = value; }
        }
        public float AverageMark()
        {
            float sum_marks = GSmath_mark + GSphys_mark + GShist_mark;
            float average = sum_marks / 3;
            return average;
        }
        public override void Info()
        {
            int[] marks = new int[] { GSmath_mark, GSphys_mark, GShist_mark };
            int max_mark = 0;
            for (int i = 0; i < 3; i++)
            {
                if (marks[i] > max_mark) max_mark = marks[i];
            }
            Console.WriteLine("Максимальная оценка: " + max_mark);
        }
    }

    class AgeSort : IComparer<Human>
    {
        public int Compare(Human first, Human second)
        {
            if (first.GSbirth_year > second.GSbirth_year)
            {
                return 1;
            }
            else if (first.GSbirth_year < second.GSbirth_year)
            {
                return -1;
            }
            else
            {
                return 0;
            }
        }
    }

    class LnameSort : IComparer<Human>
    {
        public int Compare(Human first, Human second)
        {
            if (Convert.ToInt32(first.GSlastname[0]) > Convert.ToInt32(second.GSlastname[0]))
            {
                return 1;
            }
            else if (Convert.ToInt32(first.GSlastname[0]) < Convert.ToInt32(second.GSlastname[0]))
            {
                return -1;
            }
            else
            {
                return 0;
            }
        }
    }

    public class Program
    {
        public static void Main()
        {
            Human
                person1 = new Human("Умнов", 2002, "Студент"),
                person2 = new Human("Прогуляев", 2001, "Студент"),
                person3 = new Human("Незнаев", 2004, "Студент"),
                person4 = new Human("Тригонометров", 1985, "Преподаватель"),
                person5 = new Human("Чвалов", 2003, "Студент");

            Human[] people = new Human[] { person1, person2, person3, person4, person5 };
            Array.Sort(people, new AgeSort());

            foreach (Human p in people)
            {
                Console.WriteLine("{0} - {1}", p.GSlastname, p.GSbirth_year);
            }
            Console.WriteLine("");

            Array.Sort(people, new LnameSort());
            foreach (Human p in people)
            {
                Console.WriteLine("{0} - {1}", p.GSlastname, p.GSbirth_year);
            }
            foreach (Human p in people)
            {
                p.About();
            }
        }
    }
}
