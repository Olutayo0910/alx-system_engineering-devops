# 0x09. Web Infrastructure Design

This project involves the design and implementation of a web infrastructure for hosting the website www.foobar.com. We will create two distinct infrastructure setups: one with a focus on distribution and redundancy and the other emphasizing security and monitoring.

# 0. Simple Web Stack

This project involves designing a straightforward web infrastructure consisting of a single server with a LAMP stack to host the website www.foobar.com. The following components are utilized:

- **1 Server:** The core of the web infrastructure.
- **1 Web Server (Nginx):** Handles incoming HTTP requests.
- **1 Application Server:** Executes server-side code to generate dynamic content.
- **1 Application Codebase:** Houses the code that powers the web application.
- **1 Database (MySQL):** Stores and manages data.
- **1 Domain Name (foobar.com):** Configured with a www record pointing to the server's IP address (e.g., 8.8.8.8).

### Specifics

- **What is a server?**
  - A server is a powerful computer designed to provide services, data, or resources to other computers over a network. In this setup, it is the fundamental element of our web infrastructure.

- **Role of the Domain Name**
  - The domain name, "foobar.com," acts as a human-readable address that maps to the server's IP address. It simplifies user access by replacing the need to remember an IP address.

- **Type of DNS Record for www.foobar.com**
  - The DNS record for "www" in www.foobar.com is a CNAME (Canonical Name) record, directing requests to the same IP address as "foobar.com."

- **Role of the Web Server (Nginx)**
  - Nginx serves as the entry point for web traffic, handling incoming HTTP requests and routing them to the application server.

- **Role of the Application Server**
  - The application server executes server-side code from the application codebase to generate dynamic content. It also interacts with the MySQL database for data retrieval or storage.

- **Role of the Database (MySQL)**
  - MySQL is responsible for storing and managing data required by the web application. It includes user data, content, and more.
  
- **Server Communication with User's Computer**
  - The server communicates with the user's computer via the HTTP protocol. When a user requests www.foobar.com, the server responds with the website content displayed in the user's web browser.

### Issues

- **Single Point of Failure (SPOF):**
  - The infrastructure has a single server, making it vulnerable to downtime in the event of server hardware failure or other issues. A redundant or load-balanced server setup would enhance reliability.

- **Downtime during Maintenance:**
  - Deploying new code or making changes may require restarting the web server, resulting in temporary downtime. Mitigate this through load balancing and redundancy.

- **Scalability Limitations:**
  - The infrastructure may struggle to handle significant increases in incoming traffic. Scaling horizontally (adding more servers) or vertically (upgrading server resources) is necessary to accommodate traffic spikes effectively.

# 1. Distributed Web Infrastructure

This project focuses on designing a distributed web infrastructure that enhances redundancy and scalability. The infrastructure is intended to host the website www.foobar.com and comprises the following components:

- **2 Servers:** To distribute incoming web traffic, ensuring redundancy.
- **1 Web Server (Nginx):** Manages incoming HTTP requests.
- **1 Application Server:** Executes server-side code.
- **1 Load Balancer (HAproxy):** Distributes incoming traffic evenly between the two servers.
- **1 Set of Application Files (Codebase):** Contains the web application's code.
- **1 Database (MySQL):** Stores and manages data.

### Specifics

- **For Every Additional Element, Why You Are Adding It**
  - Each additional element serves a specific purpose, such as enhancing redundancy, load distribution, and scalability.

- **Distribution Algorithm for Load Balancer**
  - The load balancer is configured with a Round Robin algorithm, which distributes traffic evenly between the two servers in a cyclical manner.

- **Active-Active Setup**
  - The infrastructure is designed as an Active-Active setup, meaning both servers actively handle incoming requests.

- **How a Database Primary-Replica (Master-Slave) Cluster Works**
  - The database is structured as a Primary-Replica (Master-Slave) cluster. The Primary node handles write operations (e.g., INSERT, UPDATE), while the Replica node serves read operations (e.g., SELECT).

### Issues

- **Single Points of Failure (SPOF)**
  - Despite the redundancy, there can still be SPOFs, such as the load balancer or database.
- **Security Issues (No Firewall, No HTTPS)**
  - Lack of a firewall poses security risks, and the absence of HTTPS may compromise data privacy.
- **No Monitoring**
  - The infrastructure currently lacks monitoring, making it challenging to track server health and performance in real-time.


# 2. Secured and Monitored Web Infrastructure

This project focuses on designing a secured and monitored web infrastructure that hosts the website www.foobar.com. The infrastructure is intended to ensure security, encrypted traffic, and real-time monitoring, and it comprises the following components:

- **3 Firewalls:** Enhance security by restricting unauthorized access.
- **1 SSL Certificate:** Enables serving www.foobar.com over HTTPS, ensuring encrypted traffic.
- **3 Monitoring Clients:** Collect data for monitoring server health and performance.

### Specifics

- **For Every Additional Element, Why You Are Adding It**
  - Each additional element serves a specific purpose: firewalls enhance security, SSL ensures encrypted traffic, and monitoring clients collect data for real-time monitoring.

- **What Are Firewalls For**
  - Firewalls restrict unauthorized access and protect the infrastructure from external threats.

- **Why Is the Traffic Served Over HTTPS**
  - Implementing HTTPS ensures that web traffic is secured and encrypted, safeguarding data privacy and security.

- **What Monitoring Is Used For**
  - Monitoring is utilized to track server health, performance, and promptly detect issues in real-time.

- **How the Monitoring Tool Is Collecting Data**
  - Monitoring tools, such as Sumo Logic, collect data through agents or clients installed on servers.

- **Explain What to Do If You Want to Monitor Your Web Server QPS**
  - To monitor web server Queries Per Second (QPS), configure the monitoring tools to collect and analyze request counts.

### Issues

- **Why Terminating SSL at the Load Balancer Level Is an Issue**
  - Terminating SSL at the load balancer level might expose unencrypted traffic within the internal network.

- **Why Having Only One MySQL Server Capable of Accepting Writes Is an Issue**
  - A single MySQL server capable of accepting writes can become a single point of failure.

- **Why Having Servers with All the Same Components (Database, Web Server, and Application Server) Might Be a Problem**
  - Uniform server components may lead to a lack of diversity in the infrastructure and potential vulnerabilities if one component fails.
