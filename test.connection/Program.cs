using System;
using System.ServiceModel;
using kareo.wsdl.KareoServices;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            BasicHttpsBinding binding = new BasicHttpsBinding();
            EndpointAddress endpointAddress = new EndpointAddress("https://webservice.kareo.com/services/soap/2.1/KareoServices.svc");
            KareoServicesClient client = new KareoServicesClient(binding, endpointAddress);
            using (client)
            {
                RequestHeader requestHeader = new RequestHeader
                {
                    User = "xxx", 
                    Password = "yyyy", 
                    CustomerKey = "1234"
                };
                GetProvidersResp resp = client.GetProviders(new GetProvidersReq { RequestHeader = requestHeader });
                Console.WriteLine("Found {0} providers", resp.Providers.Length);
                foreach (ProviderData provider in resp.Providers)
                {
                    Console.WriteLine("Provider = {0} {1}", provider.FirstName, provider.LastName);
                }
                Console.WriteLine(resp);
            }
            
            Console.WriteLine("Hello World!");
        }
    }
}