using System;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        int x;
        Stopwatch stopwatch = new Stopwatch();

        Console.WriteLine("Start!");

        stopwatch.Start();
        for (int i = 1; i <= 1000000; i++)
        {
            x = i;
            while (true)
            {
                if (x <= 1)
                {
                    break;
                }
                else if (x % 2 == 1)
                {
                    x = 3 * x + 1;
                }
                else if (x % 2 == 0)
                {
                    x /= 2;
                }
            }
        }

        stopwatch.Stop();
        Console.WriteLine("End! This took " + (double)stopwatch.ElapsedMilliseconds / 1000 + "seconds!");
    }
}
