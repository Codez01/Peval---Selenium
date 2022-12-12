
I am delighted to introduce Peval, a new venture that aims to assess the front-end and back-end performance of any website from the customer's perspective. Peval not only evaluates the primary website URL, but also every valid URL on the page, providing a comprehensive customer experience.

Some key features of Peval include ->
The use of Selenium technology to process the website and all customer clicks
Fast site processing with a threads division algorithm that expedites report generation
A complete CI/CD plan that keeps the backend and website's code up to date using GitHub actions
Setup of the entire project using Terraform (with code included)
REST API implementation for easy report generation via email 
Free website hosting using S3, Lambda as the backend with payment only for each report generation
Scalability and the ability to be scaled to multiple AWS regions for multi-regional customer experience reports
Connection to a domain and route53 hosted zone.

##For more information, please visit Peval's website at peval.cf. You can see an example of a Peval site report at


Technologies Used

![image](https://user-images.githubusercontent.com/80861363/207076609-b1a8fb08-6fa5-419c-b584-90a9fe04fce6.png)


Peval's serverless design offers significant cost savings compared to traditional EC2-based projects, which often require the use of load balancers, VPCs, elastic IPs, health checkers, EKS, ECS, and more. Peval provides valuable performance evaluations without the excessive costs associated with other solutions.

Note that the calculations are done using AWS calculator


PEVAL COST ESTIMATION:

Calculations are done considering 10000 requests per month

REST API GATEWAY:
10,000 requests x 1 unit multiplier = 10,000 total REST API requests
Tiered price for: 10000 requests
10000 requests x 0.0000035000 USD = 0.03 USD
Total tier cost = 0.0350 USD (REST API requests)
Tiered price total for REST API requests: 0.035 USD
0 USD per hour x 730 hours in a month = 0.00 USD for cache memory
Dedicated cache memory total price: 0.00 USD
REST API cost (monthly): 0.04 USD

LAMBDA: For free tier 1M requests are free per month / without the free tier :

10,000 requests x 40,000 ms x 0.001 ms to sec conversion factor = 400,000.00 total compute (seconds)
2 GB x 400,000.00 seconds = 800,000.00 total compute (GB-s)
Tiered price for: 800000.00 GB-s
800000 GB-s x 0.0000166667 USD = 13.33 USD
Total tier cost = 13.3334 USD (monthly compute charges)
10,000 requests x 0.0000002 USD = 0.00 USD (monthly request charges)
0.50 GB - 0.5 GB (no additional charge) = 0.00 GB billable ephemeral storage per function
Lambda costs - Without Free Tier (monthly): 13.33 USD

S3 BUCKET:

Tiered price for: 2 GB
2 GB x 0.0230000000 USD = 0.05 USD
Total tier cost = 0.0460 USD (S3 Standard storage cost)
10,000 PUT requests for S3 Standard Storage x 0.000005 USD per request = 0.05 USD (S3 Standard PUT requests cost)
10,000 GET requests in a month x 0.0000004 USD per request = 0.004 USD (S3 Standard GET requests cost)
0.046 USD + 0.004 USD + 0.05 USD = 0.10 USD (Total S3 Standard Storage, data requests, S3 select cost)
S3 Standard cost (monthly): 0.10 USD

Route53:

1 x 0.5000000000 USD = 0.50 USD
Total tier cost = 0.50 USD (Hosted Zone cost)
4 records x 0.0015 USD per record = 0.01 USD (RRset records cost)
0.50 USD + 0.01 USD = 0.51 Total Hosted Zones and RRset records cost
Total Hosted Zones & RRset records cost: 0.51 USD
1 million queries x 1000000 multiplier for million = 1,000,000.00 Standard queries in million
Tiered price for: 1000000.00 Standard queries
1000000 Standard queries x 0.0000004000 USD = 0.40 USD
Total tier cost = 0.40 USD (Standard queries cost)
1 million queries x 1000000 multiplier for million = 1,000,000.00 billable IP-based routing queries
Tiered price for: 1000000.00 IP-based routing queries
1000000 IP-based routing queries x 0.0000008000 USD = 0.80 USD
Total tier cost = 0.80 USD (IP-based routing queries cost)
0.51 USD + 0.40 USD + 0.80 USD = 1.71 USD
Route53 Hosted Zone cost (monthly): 1.71 USD

GITHUB ACTIONS CI/CD PLAN:

Each Execution takes approximately 40 seconds depending on the size of the project, the free plan provides 2000 minutes per month
2000 Mins / 40 seconds = 3000 CI Uploads which are pretty much enough for a month, since the project is already ready.
GITHUB ACTIONS cost (monthly): 0.00 USD

FREENOM DOMAIN:

FREENOM DOMAIN cost / Year: 0.00 USD

SSL CERTIFICATE WITH CLOUDFLARE:
SSL CERTIFICATE WITH CLOUDFLARE as a part of the free plan cost: 0.00 USD


------------------------------------------------------
Approximate Total Cost Per Month : 15.18 USD 
------------------------------------------------------


What if we wanted to implement the project with EC2?

Calculations are done considering 10000 requests per month

2 EC2 with 4 CPUs and 8 GB of RAM (1 for computations and one for the website):

2 instances x 0.0643 USD x 730 hours in month = 93.88 USD (monthly instance savings cost)
Amazon EC2 Instance Savings Plans instances (monthly): 93.88 USD

ELASTIC LOAD BALANCER: 

1 load balancers x 0.0225 USD per hour x 730 hours in a month = 16.43 USD
Application Load Balancer fixed hourly charges (monthly): 16.43 USD

ELASTIC IP X2:

2 EIPs per instance - 1 free EIP = 1.00 EIPs after first free EIP
Max (1.00 EIPs, 0 ) = 1.00 billable EIPs per instance
1.00 billable EIPs x 2 instances = 2.00 Total EIPs
2.00 total EIPs x 730 hours = 1,460.00 hours/month (each EIP is attached to an EC2 instance)
1,460.00 hours/month (EIPs are attached) x 0.005 USD = 7.30 USD (EIPs attached cost)
Elastic IP cost (monthly): 7.30 USD

Route53:

1 x 0.5000000000 USD = 0.50 USD
Total tier cost = 0.50 USD (Hosted Zone cost)
4 records x 0.0015 USD per record = 0.01 USD (RRset records cost)
0.50 USD + 0.01 USD = 0.51 Total Hosted Zones and RRset records cost
Total Hosted Zones & RRset records cost: 0.51 USD
1 million queries x 1000000 multiplier for million = 1,000,000.00 Standard queries in million
Tiered price for: 1000000.00 Standard queries
1000000 Standard queries x 0.0000004000 USD = 0.40 USD
Total tier cost = 0.40 USD (Standard queries cost)
1 million queries x 1000000 multiplier for million = 1,000,000.00 billable IP-based routing queries
Tiered price for: 1000000.00 IP-based routing queries
1000000 IP-based routing queries x 0.0000008000 USD = 0.80 USD
Total tier cost = 0.80 USD (IP-based routing queries cost)
0.51 USD + 0.40 USD + 0.80 USD = 1.71 USD
Route53 Hosted Zone cost (monthly): 1.71 USD

VPC NAT GATEWAY:

730 hours in a month x 0.045 USD = 32.85 USD (Gateway usage hourly cost)
1 NAT Gateways x 32.85 USD = 32.85 USD (Total NAT Gateway usage and data processing cost)
Total NAT Gateway usage and data processing cost (monthly): 32.85 USD

REST API GATEWAY:

10,000 requests x 1 unit multiplier = 10,000 total REST API requests
Tiered price for: 10000 requests
10000 requests x 0.0000035000 USD = 0.03 USD
Total tier cost = 0.0350 USD (REST API requests)
Tiered price total for REST API requests: 0.035 USD
0 USD per hour x 730 hours in a month = 0.00 USD for cache memory
Dedicated cache memory total price: 0.00 USD
REST API cost (monthly): 0.04 USD

-------------------------------------------------------
Approximate Total Cost Per Month : 152.21 USD 
-------------------------------------------------------

##Peval costs 1000% less than an EC2 oriented project.
