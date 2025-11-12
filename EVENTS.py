using System;

class GuessTheNumber
{
    static void Main()
    {
        Random rnd = new Random();
        int target = rnd.Next(1, 101); // Random number between 1-100
        int guess = 0;
        int tries = 0;

        Console.WriteLine("Welcome to Guess The Number!");
        Console.WriteLine("I'm thinking of a number between 1 and 100.");

        while (guess != target)
        {
            Console.Write("Enter your guess: ");
            string input = Console.ReadLine();

            if (!int.TryParse(input, out guess))
            {
                Console.WriteLine("That's not a valid number!");
                continue;
            }

            tries++;

            if (guess < target)
                Console.WriteLine("Higher!");
            else if (guess > target)
                Console.WriteLine("Lower!");
            else
                Console.WriteLine($"Congrats! You guessed it in {tries} tries!");
        }
    }
}
