using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
using System;
using System.Diagnostics;
using System.Collections.Generic;

class RobloxLauncher
{
    static Dictionary<int, string> gameLinks = new Dictionary<int, string>
    {
        { 1, "https://www.roblox.com/games/123456789/Obby-Adventure" },
        { 2, "https://www.roblox.com/games/987654321/Speed-Simulator" },
        { 3, "https://www.roblox.com/games/192837465/Build-A-World" }
    };

    static Dictionary<int, string> gameNames = new Dictionary<int, string>
    {
        { 1, "Obby Adventure" },
        { 2, "Speed Simulator" },
        { 3, "Build-A-World" }
    };

    static void Main()
    {
        Console.Title = "Roblox Game Launcher";
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Welcome to the Roblox Game Launcher!");
        Console.ResetColor();

        while (true)
        {
            Console.WriteLine("\nAvailable Games:");
            foreach (var game in gameNames)
            {
                Console.WriteLine($"{game.Key}. {game.Value}");
            }

            Console.Write("\nEnter the number of the game you want to launch (or 0 to exit): ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int choice))
            {
                if (choice == 0)
                {
                    Console.WriteLine("Exiting launcher. See you next time!");
                    break;
                }
                else if (gameLinks.ContainsKey(choice))
                {
                    Console.WriteLine($"Launching {gameNames[choice]}...");
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = gameLinks[choice],
                        UseShellExecute = true
                    });
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Invalid selection. Please try again.");
                    Console.ResetColor();
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Invalid input. Please enter a number.");
                Console.ResetColor();
            }
        }
    }
}
