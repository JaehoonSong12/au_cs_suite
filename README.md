<!-- 
 @requires
 1. VSCode extension: Markdown Preview Enhanced
 2. Shortcut: 'Ctrl' + 'Shift' + 'V'
 3. Split: Drag to right (->)

 @requires
 1. VSCode extension: Markdown All in One
 2. `File` > `Preferences` > `Keyboard Shortcuts`
 3. toggle code span > `Ctrl + '`
 4. toggle code block > `Ctrl + Shift + '`

 @usage
 1. End of Proof (Q.E.D.): <div style="text-align: right;">&#11035;</div>
 2. End of Each Section: 

     <br /><br /><br />

     ---



     <p align="right">(<a href="#readme-top">back to top</a>)</p>

 3. ![image_title_](images/imagefile.png)
 4. [url_title](URL)
 -->
<!-- Anchor Tag (Object) for "back to top" -->
<a id="readme-top"></a> 




# AU-CS Suite (AUC)

This is a repository of diverse microservices and applications developed iteratively by a team of computer science students from Auburn University, guided by a Georgia Tech senior developer (Jaehoon Song). This project emphasizes designing architectures that structure applications as a set of independently deployable, loosely coupled components, also known as services. These microservices foster scalability, modularity, and ease of maintenance.


## Project Management Platform
Collaborate and stay updated on project discussions, tasks, and announcements through our Discord channel:

[Discord Server - AUC](https://discord.com/channels/1321901302548136030/1321901303114240126)


## Code Access

The code for this project is hosted on GitHub in this repository. You can explore the source code, contribute, and access different branches as necessary:

[GitHub Repository - AUC](https://github.com/JaehoonSong12/au_cs_suite)


## Documentation

For detailed documentation, including textbook references, project specifications, development guidelines, and usage instructions, please visit our documentation on Google Drive:

[Google Documentation - AUC](https://drive.google.com/drive/folders/1saxYZpeG_U3vsAhd0bCbIjVzMoZWK4RF?usp=sharing)


## Team
- **Software Architect (Tech Lead)**: Jaehoon Song
  - Takes a broader role, overseeing the technical direction of the project, guide developers on how to implement features within the system architecture, and solving algorithmic and archiectural issues.
  - **Member Contact**: manual20151276@gmail.com (JaehoonSong12)

- **AI/Aiga/UI/UX**: Sowon Lim
  - My role is AI/Aiga/UI/UX. I am willingly committed to supporting other areas whenever needed as well. Additionally, I can take full responsibility for business aspects and am confident in handling them flawlessly! After the development phase, you can trust me with everything, including managing profits fairly. Even if we base our software development on an existing photo booth, I want to aim to create the best version by incorporating our unique ideas and making it truly exceptional.
  - **Member Contact**: sowonlim0210@gmail.com (wish)

- **Networking and Security**: Subeen Kim
  - Ensures secure operations and efficient networking for the GPB system. Focused on designing and implementing robust security features and seamless user workflows.
  - **Member Contact**: [selline0824@gmail.com](Subeen)


## Features
- **Microservice Architecture**: Applications are structured as independent, deployable components to ensure flexibility and scalability.
- **Iterative Development**: Continuous improvement through regular development cycles.
- **Collaboration Focus**: Team-oriented workflows using GitHub for version control, issue tracking, and collaborative coding.
- **Diverse Applications**: A range of services addressing different use cases, unified under a shared repository.

## Development Approach
1. **Iterative Cycles**: Development occurs in sprints, with each cycle refining functionality and addressing feedback.
2. **Service Modularity**: Each microservice is self-contained, facilitating independent deployment and updates.
3. **Collaboration and Learning**: Encouraging mentorship, code reviews, and shared learning among the team.








## Table of Contents
- [AU-CS Suite (AUC)](#au-cs-suite-auc)
  - [Project Management Platform](#project-management-platform)
  - [Code Access](#code-access)
  - [Documentation](#documentation)
  - [Team](#team)
  - [Features](#features)
  - [Development Approach](#development-approach)
  - [Table of Contents](#table-of-contents)
- [Instructions](#instructions)
  - [Repository Structure](#repository-structure)
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
- [Service #1: Global Photo Booth (GPB)](#service-1-global-photo-booth-gpb)
  - [System Architecture](#system-architecture)
  - [Programming Language, Libraries, and Framework](#programming-language-libraries-and-framework)
    - [Backend: API Management](#backend-api-management)
    - [Backend: File and Image Processing](#backend-file-and-image-processing)
    - [Backend: QR Code Management](#backend-qr-code-management)
    - [Frontend: Web Server](#frontend-web-server)
  - [Networking and Security](#networking-and-security)
    - [File Management](#file-management)
    - [QR Code Workflow](#qr-code-workflow)
    - [Cloud Storage](#cloud-storage)
    - [Hosting Setup](#hosting-setup)
    - [Security Features](#security-features)
  - [Additional Details](#additional-details)
    - [Scalability](#scalability)
    - [Maintenance](#maintenance)
    - [UX (User Experience)](#ux-user-experience)



<p align="right">(<a href="#readme-top">back to top</a>)</p>






<br /><br /><br />

---



# Instructions



## Repository Structure
```plaintext
/src
   /main
      /java
      /kotlin
      /python
      /...
   /tests
      /java
      /kotlin
      /python
      /...
README.md
```

The repository uses a Gradle-style directory structure. Each language-specific folder under `src` can have its own execution points, such as `cli` for command-line interfaces and `gui` for graphical user interfaces. Testing directories for each language are located under `tests`.

## Getting Started
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/au-cs-suite.git
   cd au-cs-suite
   ```
2. **Navigate to a Language or Execution Point**
   ```bash
   cd src/language-1/cli
   ```
3. **Run the Service**
   Refer to the specific microservice documentation for setup and execution instructions.

## Contributing
We welcome contributions! If you would like to suggest improvements, please submit a pull request, or open an issue.
1. **Fork the Repository**
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m "Description of changes"
   ```
4. **Push to Your Fork and Create a Pull Request**


## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


## Contact
For questions or suggestions, feel free to reach out to manual20151276@gmail.com.



<p align="right">(<a href="#readme-top">back to top</a>)</p>






<br /><br /><br />

---



# Service #1: Global Photo Booth (GPB)

The **Global Photo Booth** (GPB), also known as *Snap & Share*, offers a fun and accessible photo booth experience for users worldwide. It combines mobile technology, customizable photo features, and local collaborations, enabling users to capture and share moments easily. Core features include QR codes for direct access, in-store booths, and a mobile-friendly web app. By partnering with local events and personalities, the service also provides unique photo frames and themes to engage different communities.



## System Architecture

The GPB system is built on a **client-server architecture** that separates the roles of the frontend and backend for better organization and future scalability. Here’s a breakdown of the system's key components:

- **Frontend:** A responsive web client that works on multiple devices without requiring any software installation.  
- **Backend:** A Python-powered server responsible for handling file storage, photo editing, and metadata management.  
- **Cloud Storage:** Photos and session data are stored on scalable platforms like Amazon S3 or Google Cloud.  
- **QR Code Integration:** Unique QR codes link users directly to their photo sessions.

This architecture ensures that users have a consistent and efficient experience while making it easy to maintain and expand the system.

---

## Programming Language, Libraries, and Framework

To ensure the Global Photo Booth (GPB) system is both reliable and efficient, we have carefully selected a variety of tools and libraries to handle the different components of the backend and frontend. Each choice was made with the goal of maintaining flexibility, scalability, and ease of use for both developers and end-users.

The core technologies for development are chosen as follows.

- **Python** is used for the *backend* because it is well-suited for handling files, processing images, and managing data.
- **JavaScript**, along with **HTML** and **CSS**, is used for creating the web-based *frontend* interface.

### Backend: API Management
For the backend, effective communication between the frontend and the server is critical. To achieve this, we use the following tools:

- **FastAPI**: A lightweight and fast framework for building RESTful APIs. It allows for seamless interaction between the backend and the frontend, ensuring responsive and efficient data exchange.

### Backend: File and Image Processing

Another crucial aspect of the GPB system is its ability to process and edit images efficiently. These libraries help manage photo-related tasks:

- **Pillow**: A simple yet powerful library that handles basic photo editing tasks like cropping, resizing, and adding filters to photos.
- **OpenCV**: A more advanced library for high-level image manipulation, such as object detection or detailed photo enhancements, offering flexibility for more complex processing needs.
- **Celery**: A task management tool that allows the backend to handle multiple photo-processing tasks in the background, ensuring smooth performance even during high usage.




### Backend: QR Code Management

For an easy and accessible user experience, QR codes are generated to link users to their photo sessions. This tool is essential for smooth integration between physical photo booths and the web platform:

- **qrcode**: A straightforward Python library used to generate unique QR codes for each session, allowing users to quickly access and manage their photos.


### Frontend: Web Server
The frontend uses modern web technologies to deliver a smooth and interactive user experience:
- **Dynamic Web Interface:** _React.js_ to build a responsive and dynamic user interface.  
- **Core Web Development:**  _HTML5, CSS3, and JavaScript_ for creating an intuitive, cross-platform web application.  

This classification ensures each backend role is addressed effectively, and the tools fit the specific tasks they are designed to handle.

---

## Networking and Security

The GPB system prioritizes simple workflows and secure operations for users. Below are key aspects of its design:

### File Management
The backend handles file uploads, metadata, and photo editing, while the frontend focuses on presenting these files in an easy-to-navigate interface.

### QR Code Workflow
The QR code integration simplifies the user experience:
1. The backend generates a unique QR code for each photo session.  
2. Users scan the QR code to access their session on the web application.  
3. Photos can be downloaded or shared directly from the app.  

### Cloud Storage
Photos and metadata are stored in reliable cloud services like *Amazon S3* or *Google Cloud Storage*. These services allow the system to expand as more users join.

### Hosting Setup
The system is deployed using a clear separation of services:
- The **frontend server** hosts the responsive web app, handling user interactions.  
- The **backend server** manages file processing, metadata, and QR code generation.  
- Cloud platforms like *AWS*, *Google Cloud*, or *DigitalOcean* provide scalable hosting.  

### Security Features
To protect user data and maintain trust, the system includes the following measures:
- **Data Encryption:** All photos and sensitive data are encrypted using *AES* before storage.  
- **Secure Communication:** Communication between users and the system is protected using *HTTPS*.  
- **Authentication:** *JSON Web Tokens (JWT)* are used to secure user sessions.  
- **Privacy Compliance:** The system follows global data protection rules to maintain user privacy.

These measures ensure a safe and reliable service for all users.

---

## Additional Details

The design of the GPB system includes practical features to ensure it remains efficient and user-friendly.

### Scalability
The architecture can easily handle more users by leveraging cloud storage and separating the frontend and backend roles. This setup allows for smooth expansion without major changes to the system.

### Maintenance
With its modular structure, the system is easy to maintain. Developers can work on the frontend or backend independently, reducing the risk of downtime during updates.

### UX (User Experience)
The web application is optimized for all devices, from smartphones to desktops. QR codes simplify the workflow, making it easy for users to access, manage, and share their photos.


<p align="right">(<a href="#readme-top">back to top</a>)</p>
