
using System.Collections.Generic;

// Represents a plant with its growth stages and needs
class Plant
{
    public string Name { get; set; }
    public int GrowthStage { get; set; }
    public int MaxGrowthStage { get; set; }
    public bool IsWatered { get; set; }

    public Plant(string name, int maxGrowth)
    {
        Name = name;
        GrowthStage = 0;
        MaxGrowthStage = maxGrowth;
        IsWatered = false;
    }

    public void Water()
    {
        IsWatered = true;
        Console.WriteLine($"{Name} has been watered.");
    }

    public void Grow()
    {
        if (IsWatered && GrowthStage < MaxGrowthStage)
        {
            GrowthStage++;
            IsWatered = false;
            Console.WriteLine($"{Name} grew to stage {GrowthStage}/{MaxGrowthStage}.");
        }
        else if (!IsWatered)
        {
            Console.WriteLine($"{Name} needs water before it can grow!");
        }
        else
        {
            Console.WriteLine($"{Name} is fully grown!");
        }
    }

    public override string ToString()
    {
        string status = IsWatered ? "watered" : "dry";
        return $"{Name} [{GrowthStage}/{MaxGrowthStage}, {status}]";
    }
}

class PlantsGame
{
    static void Main()
    {
        List<Plant> garden = new List<Plant>
        {
            new Plant("Sunflower", 5),
            new Plant("Tomato", 7),
            new Plant("Rose", 4)
        };

        Console.WriteLine("Welcome to the Plants Game!");
        Console.WriteLine("Available plants:");
        for (int i = 0; i < garden.Count; i++)
        {
            Console.WriteLine($"{i + 1}: {garden[i].Name}");
        }

        while (true)
        {
            Console.WriteLine("\nGarden:");
            for (int i = 0; i < garden.Count; i++)
            {
                Console.WriteLine($"{i + 1}: {garden[i]}");
            }
            Console.Write("Choose a plant by number (or 0 to quit): ");
            if (!int.TryParse(Console.ReadLine(), out int choice) || choice < 0 || choice > garden.Count)
            {
                Console.WriteLine("Invalid choice.");
                continue;
            }
            if (choice == 0) break;

            Plant selected = garden[choice - 1];
            Console.Write("Action for this plant: (1) Water  (2) Grow: ");
            string action = Console.ReadLine();
            if (action == "1") selected.Water();
            else if (action == "2") selected.Grow();
            else Console.WriteLine("Invalid action.");
        }

        Console.WriteLine("Thanks for playing!");
    }
}
