print("Welcome to Python Programming")
print("This script will help you manage your Python projects.")

# Prompt the user to enter the name of their project
project_name = input("Enter the name of your project: ")

# Prompt the user to choose a programming language
languages = ["Python", "JavaScript", "C++", "Java", "Go"]
print("Choose a programming language:")
for i, language in enumerate(languages, start=1):
    print(f"{i}. {language}")
language_choice = int(input("Enter your choice (1-5): "))
selected_language = languages[language_choice]

# Prompt the user to choose a version control system
vcs_systems = ["Git", "Subversion", "Mercurial", "None"]
print("Choose a version control system:")
for i, vcs in enumerate(vcs_systems, start=1):
    print(f"{i}. {vcs}")
vcs_choice = int(input("Enter your choice (1-4): "))
selected_vcs = vcs_systems[vcs_choice]

# Generate the project structure based on the user's selections
project_structure = f"""
{project_name}/
├───{project_name}
│   ├───__init__.py
│   └───{selected_language}
│       └───__init__.py
└───.git (Git repository)
    ├───branches
    ├───config
    ├───description
    ├───hooks
    │   └───pre-commit
    ├───info
    │   └───sparse-checkout
    ├───logs
    │   └───refs
    │       └───heads
    │           └───main
    ├───objects
    │   └───pack
    │       └───pack-536f7f09887504702f151848972215800f5793f9.idx
    └───refs
        └───heads
            └───main
"""


# Print the generated project structure
print("\nGenerated Project Structure:")
print(project_structure)

# Prompt the user to save the project structure to a file
save_file = input("Do you want to save the project structure to a file (y/n)? ")
if save_file.lower() == 'y':
    file_name = input("Enter the name of the file: ")
    with open(file_name, 'w') as file:
        file.write(project_structure)
    print(f"Project structure saved to {file_name}")
    