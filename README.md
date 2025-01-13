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
-->

<!---------------------------------------------------------------------- @usage (end_of_proof)
<div style="text-align: right;">&#11035;</div> 
------------------------------------------------------------------------>

<!---------------------------------------------------------------------- @usage (end_of_section) 
<br /><br /><br />

---

Your paragraphs...

<p align="right">(<a href="#readme-top">back to top</a>)</p>
------------------------------------------------------------------------>

<!---------------------------------------------------------------------- @usage (image_hyperlink) 
<div align="center">
    <img src="images/fluid.webp"/>
</div>
------------------------------------------------------------------------>

<!---------------------------------------------------------------------- @usage (video_hyperlink) 
<div align="center">
    <video width="640" height="360" controls>
        <source src="videos/UX_research.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
------------------------------------------------------------------------>

<!---------------------------------------------------------------------- @usage (url_hyperlink)
[url_title](URL)
------------------------------------------------------------------------>

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
    - [Instructions: Frontend (React)](#instructions-frontend-react)
    - [Instructions: Backend (Python)](#instructions-backend-python)
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
/python-package1
   /...
/python-package2
   /...
/jvm-module1
   /src
      /main
         /java
         /kotlin
         /...
      /test
         /java
         /kotlin
         /...
/jvm-module2
   /src
      /main
         /java
         /kotlin
         /...
      /test
         /java
         /kotlin
         /...
/nodejs-app
   /public
      /css
      /js
      /images
      /...
   /src
      /routes
      /controllers
      /models
      /...
   /tests
      /unit
      /integration
      /...
   package.json
   app.js
README.md
```

The repository structure is arranged to incorporate Python packages, JVM modules, and Node.js components while ensuring modularity and organization.  

- Python packages, such as `/python-package1` and `/python-package2`, are configured as independent units, with specific functionalities assigned to each directory.  

- JVM modules, including `/jvm-module1` and `/jvm-module2`, are structured to align with Gradle module conventions.  
  - Within these, `/src/main/` directories are utilized for primary source code, which is categorized by programming language (e.g., Java, Kotlin).  
  - Corresponding tests are organized under `/src/test/`, ensuring a clear separation between implementation and validation.  

- The Node.js application is designed to be consistent in static assets, logic, and configurations.  
  - The `/public` directory is employed for storing static assets, such as CSS, JavaScript, and images.  
  - The `/src` directory is responsible for the application’s core logic, structured into subdirectories for routes, react components, and so on ...  
  - The `package.json` file is included to define package dependencies, while `app.js` serves as the entry point for application execution.  

This configuration supports projects involving multiple programming languages and frameworks, increasing maintainability and scalability.



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

- **Frontend:** A React-powered responsive web client that works on multiple devices without requiring any software installation.  
- **Backend:** A Python-powered server responsible for handling file storage, photo editing, and metadata management.  
- **Cloud Storage:** Photos and session data are stored on scalable platforms like Amazon S3 or Google Cloud.  
- **QR Code Integration:** Unique QR codes link users directly to their photo sessions.

This architecture ensures that users have a consistent and efficient experience while making it easy to maintain and expand the system.


### Instructions: Frontend (React)

The GPB frontend is powered by Node.js and is designed to handle all client-side responsibilities. Follow these steps to set up and run the frontend:

1. **Ensure Node.js and NPM are Installed**  
   The script checks for the required packages, including `web-vitals`, `axios`, and `tailwindcss`. If any of these packages are missing, they will be installed automatically.

2. **Install Dependencies**  
   Check and install the required dependencies using npm:
```bash
# Check if web-vitals is installed
if ! npm list web-vitals > /dev/null 2>&1; then
  npm install web-vitals                            # Performance monitoring
fi

# Check if axios is installed
if ! npm list axios > /dev/null 2>&1; then
  npm install axios                                 # HTTP requests
fi

# Check if tailwindcss is installed
if ! npm list tailwindcss > /dev/null 2>&1; then
  npm install -D tailwindcss postcss autoprefixer   # CSS Styling framework
  npx tailwindcss init
fi
```

3. **Build the Frontend**  
   Install all the required npm packages and build the project:
```bash
npm install
npm run build
```
4. **Run the Frontend**  
   Start the frontend server using npm:
```bash
npm start
```

By following these steps, the GPB frontend can be configured, built, and executed to support the system's user interface (frontend functional requirements).


### Instructions: Backend (Python)

The GPB backend is powered by Python and is designed to handle all server-side responsibilities. Follow these steps to set up and run the backend:

1. **Ensure Python is Installed**  
   The script checks for `python3` or `python`. If neither is installed, you will need to install Python before proceeding.

2. **Install Dependencies**  
   Required tools and libraries, including `poetry`, `tox`, and `pipreqs`, are automatically checked and installed if missing:
```bash
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
    PIP_CMD=pip
else
    echo -e "\033[0;33Python is not installed. Please install Python and try again.\033[0m"
    exit 1
fi

if ! command -v poetry &>/dev/null; then
    echo -e "\033[0;33mpoetry is not installed. Installing...\033[0m"
    $PIP_CMD install poetry
fi

if ! command -v tox &>/dev/null; then
    echo -e "\033[0;33mtox is not installed. Installing...\033[0m"
    $PIP_CMD install tox
fi

if ! command -v pipreqs &>/dev/null; then
    echo -e "\033[0;33mpipreqs is not installed. Installing...\033[0m"
    $PIP_CMD install pipreqs
fi
```

3. **Initialize the Environment**  
   Generate dependencies, manage them with `poetry`, and install additional tools:
```bash
pipreqs . --ignore "ext/" --force    # Generate dependencies
poetry add $(cat requirements.txt)   # Add dependencies to Poetry
poetry run pip install python-multipart
rm requirements.txt                  # Clean up
```

4. **Build the Backend**  
   Compile the backend into a distributable format using `poetry` and `pyinstaller`:
```bash
poetry build
poetry run pyinstaller --onefile cli.py
```

5. **Run the Server**  
   Start the backend server using standalone-executable in `dist/cli`. Optionally, start the backend server using `poetry`:
```bash
poetry run cli_gpb_server
```

By following these steps, the GPB backend can be configured, built, and executed to support the system's backend functionalities.

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
