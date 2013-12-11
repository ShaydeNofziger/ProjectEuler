using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Problem2
{
    class Program
    {
        static void Main(string[] args)
        {
            int prev = 1;
            int curr = 1;
            int sum = 0;
            int next = 2;

            while (curr < 4000000)
            {
                if ((curr % 2) == 0)
                {
                    sum += curr;
                }
                prev = curr;
                curr = next;
                next = prev + curr;
            }
            Console.Write("Sum of even ints in Fib Seq: {0}", sum);
            Console.ReadKey();
        }
    }
}
