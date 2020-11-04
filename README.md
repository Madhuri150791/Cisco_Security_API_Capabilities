# Cisco_Security_API_Capabilities
This Repository Aims to demonstrate the real life Problems and Its Solution wrt to Cisco Security Product. The Solution will be based on the REST API and Automation Capabilities Offered By these Product.


1. ManageFTDRules

        Problem Statement:

        Customer has created a new IPS Policy which now needs to be applied to all the rules of given ACP in Cisco FTD. Pain point here is given ACP has 1000+ rules         where this update needs to be performed.

        Solution:

        Cisco FTD offers REST APIs which can be leveraged for above mentioned usecases. Consider the scenario where an engineers is dedicated to just update the             ACLs, rather REST API capability can be leveraged to automate such task and Engineer can then focus on other useful tasks.
        
        Usage:
        
        1. Clone Repo.
        
        git clone https://github.com/Madhuri150791/Cisco_Security_API_Capabilities.git 
        
        2. Run Code.
        
        Move to the working directory.(ManageFTDRules)
        
        python3 GETRules.py
        
        This script is going to create following files:
                - accessrule-sf-policy.txt
        3. Filter the obtained data.
        
        Run the code to filter to obtained data to form the payload for the PUT operation.
        
        python3 Fitlercustom.py
        
        4. Run the code to appened the IPS rules to the accessrules.
        
        python3 POSTRULEwithIPSEnabled.py
        
        


2. ManageISEusingAnsible

        Problem Statement:
        
        Manage ISE day to day Operation like adding Network Device, Internal Users etc using a standard Automation Language which can be spanned to other Network           Device.
        
        Solution:
        
        Customer Network are now moving to utilise Automation capabilities available within Network Devices/Products to avail ease of operation and less human               error. Keeping the same in mind, Ansible is one such automation lanaguage whih can be leveraged as central methodology to managae all Network Device present         in the network. The same can be extended to Cisco ISE which is Identity and Access management solution using in the Enterprise/DC/SP Network.
        This script explores the option to use REST API using Ansible.
        Benefit :
        No need invest on learning curve for new scripting language like Python. Ansible can be used to manage CLI as well as REST API based Devices.
        
        Usage:
        
        Clone th repo.
        
        git clone https://github.com/Madhuri150791/Cisco_Security_API_Capabilities.git
        
        1. Edit ISE_Inventory.txt
        
        Put your ISE node under the group mylabserver.
        
        2. Run the playbook.
        
        ansible-playbook -i ISE-inventory.txt ISE-playbook.yml
        
        Note: PLease make sure you have ansible installed in the local machine from where you are running the ansible.
        
        For more clarification on the code please visit https://www.linkedin.com/pulse/setting-up-ansible-cisco-ise-madhuri-dewangan/
 


Developed By:
Madhuri Dewangan
Consulting Engineer
Cisco Customer Experience
