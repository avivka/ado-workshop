# ADO-workshop

## Lab Navigation

1. aka.ms/lod
2. Sign in -> Microsoft Account -> Login with a Microsoft Account
3. Accept 'Let this app access your info'
4. Select your country
5. WorkshopPlus -> My Training -> Redeem Training Key -> Enter the key that was verbaly shared in class
6. Under 'Labs' click on 'Launch'
7. Login to your end station using the username and password at the 'Credentials' tab
   1. Use the 'T' sign to to type the text straight to your prompt
8. Follow the guidance at the 'Lab Manual' instructions:
   1. Follow Until Module 2: Projects, Lab 1: Projects Exercise 2: Manage Projects, Skip it and go straight to Exercise 3: Project Security
   2. Follow Module 2 Exercise 3 and Exercise 4, Skip Exercise 5 and Exercise 6
   3. Skip Lab 2: PartsUnlimited Lab Setup entirely and continue to Module 3: Azure Repos with Git, Lab 1: Getting Started with Git, Exercise 1: Configuring Azure Repos Lab Environment
   4. Instead of following Module 3: Azure Repos using Git (and Module 3 (Alternative): Git with GitHub), import this repo using the following guide:
      1. At CustomerPortal Project, go to Repos -> Files and Import this repository - The clone URL is https://github.com/avivka/ado-workshop.git and import.
      2. Under Set up build -> Choose 'Existing Azure Pipelines YAML file' and start by choosing simple_pipeline.yaml as the initial pipeline
   5. At this point, you may choose if you want to continue with the Lab (Starting from Module 4: Azure Pipelines, Lab 1: Configuring CI/CD Pipelines, Exercise 1: Configuring CI/CD Pipelines as Code With YAML in Azure DevOps) or to setup the agent on top of your mac or using an external linux runner. 

## After 
Switch to the imported Azure Repos repo (that was imported from this very own repo) named after your Azure Project
There, under 'Files', click on 'Set up build', Choose 'Existing Azure Pipelines YAML file' and follow the pipelines creation flow.

Under Files of this imported Create Starter pipeline

