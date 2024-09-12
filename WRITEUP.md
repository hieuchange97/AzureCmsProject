# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.
## Azure VM vs App Service Comparison
| Criteria      | Azure Virtual Machine                                                                                                                                      | Azure App Service                                                                                                                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Costs         | Higher costs due to VM size, storage, networking, and maintenance. Requires managing OS licensing.                                                        | Lower costs with pay-as-you-go model, includes auto-scaling, load balancing, and reduced operational expenses.                     |
| Scalability   | Manual scaling or custom automation needed, slower and limited by VM size and management capacity.                                                        | Automatic scaling based on demand, highly scalable with easy management of scaling policies.                                       |
| Availability  | High availability achievable with manual configuration (availability sets, zones), requires management.                                                   | Built-in high availability with managed uptime, automatic failover, and regional redundancy.                                       |
| Workflow      | Complex workflow with environment setup, OS configuration, and maintenance. Suitable for custom requirements.                                             | Simplified workflow with quick deployment, integrated CI/CD, and minimal maintenance. Ideal for standard CMS setups.               |
Base on above comparable between App Services and Virtual Machines, I will choose App Services for my application on production environments.
But with this project for practice purposes I will choose Virtual Machines, because It's easier for me to debug, fix some issues in project.
The project needs to be installed some others packages on the OS also, example: unixodbc, so the VM is the best choice for me
to do it and fix errors faster.
Virtual Machines suitable for develop environment and for the application is not stable and have some problems.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
The project has many issues relates to the python package dependencies, pythons version required, the OS module to connect with Azure SQL server.
I choose VM to trace and fix the error step by step:
1. Try to install python module dependencies with python3.9. (Because the requirements.txt file is not correct for all python versions)
2. Set some secret to environment variables and start the application
3. Fix error missing sql driver in OS
4. Fix error the IP connect to Azure SQL server can not connect to Azure SQL server (Add IP address to Allowed list)
5. Run application

Test my application via https://40.81.22.150:5555