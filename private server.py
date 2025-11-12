using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

public class PrivateServer
{
    private TcpListener listener;
    private bool isRunning = false;
    private readonly int port;

    public PrivateServer(int port)
    {
        this.port = port;
        listener = new TcpListener(IPAddress.Any, port);
    }

    public void Start()
    {
        listener.Start();
        isRunning = true;
        Console.WriteLine($"🧠 Private server started on port {port}");

        while (isRunning)
        {
            if (listener.Pending())
            {
                TcpClient client = listener.AcceptTcpClient();
                ThreadPool.QueueUserWorkItem(HandleClient, client);
            }
            Thread.Sleep(100); // reduce CPU usage
        }
    }

    private void HandleClient(object obj)
    {
        TcpClient client = (TcpClient)obj;
        NetworkStream stream = client.GetStream();

        byte[] buffer = new byte[1024];
        int byteCount = stream.Read(buffer, 0, buffer.Length);
        string request = Encoding.UTF8.GetString(buffer, 0, byteCount);

        Console.WriteLine($"📡 Received: {request}");

        string response = $"🔒 Server received: {request}";
        byte[] responseBytes = Encoding.UTF8.GetBytes(response);
        stream.Write(responseBytes, 0, responseBytes.Length);

        client.Close();
    }

    public void Stop()
    {
        isRunning = false;
        listener.Stop();
        Console.WriteLine("🛑 Server stopped.");
    }
}
