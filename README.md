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

## About
This is a repository of diverse microservices and applications developed iteratively by a team of computer science students from Auburn University, guided by a Georgia Tech senior developer (Jaehoon Song). This project emphasizes designing architectures that structure applications as a set of independently deployable, loosely coupled components, also known as services. These microservices foster scalability, modularity, and ease of maintenance.


## Project Management Platform
Collaborate and stay updated on project discussions, tasks, and announcements through our Discord channel:

[AUC Discord](https://discord.com/channels/1321901302548136030/1321901303114240126)


## Code Access

The code for this project is hosted on GitHub in this repository. You can explore the source code, contribute, and access different branches as necessary:

[GitHub Repository - AUC](https://github.com/JaehoonSong12/au_cs_suite)


## Documentation

For detailed documentation, including textbook references, project specifications, development guidelines, and usage instructions, please visit our documentation on Google Drive:

[AUC Documentation](https://drive.google.com/drive/folders/1saxYZpeG_U3vsAhd0bCbIjVzMoZWK4RF?usp=sharing)


## Team
- **Software Architect (Tech Lead)**: Jaehoon Song
  - Takes a broader role, overseeing the technical direction of the project, guide developers on how to implement features within the system architecture, and solving algorithmic and archiectural issues.
- **AAAAA**:
  - desc
- **BBBBB**:
  - desc

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
  - [About](#about)
  - [Team](#team)
  - [Features](#features)
  - [Development Approach](#development-approach)
  - [Documentation](#documentation)
  - [Project Management Platform](#project-management-platform)
  - [Code Access](#code-access)
  - [Table of Contents](#table-of-contents)
- [Instructions](#instructions)
  - [Repository Structure](#repository-structure)
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)



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
This is free and unencumbered software released into the public domain.


## Contact
For questions or suggestions, feel free to reach out to manual20151276@gmail.com.



<p align="right">(<a href="#readme-top">back to top</a>)</p>
