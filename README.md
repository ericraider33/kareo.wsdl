# kareo.wsdl
Kareo API WSDL

Use this DLL to connect to Kareo EMR via their SOAP API.  Documentation can be found here: https://helpme.kareo.com/01_Kareo_PM/12_API_and_Integration

Currently version 2.1 of the API is supported.

## Install
Use Nuget:
```
Install-Package kareo.wsdl -Version 2.1.0
```

## Test Connectivity
Use the following code to verify connectivity.
```
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
```


