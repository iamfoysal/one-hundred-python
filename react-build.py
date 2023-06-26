import os
import subprocess

def create_react_project(project_name):
    os.makedirs(project_name)
    os.chdir(project_name)

    subprocess.run(['npx', 'create-react-app', '.'])
    os.makedirs('src/components')
    os.makedirs('src/styles')
    create_component('SampleComponent')
    print('React project created successfully!')

def create_component(component_name):
    component_filename = f'src/components/{component_name}.js'
    with open(component_filename, 'w') as file:
        file.write(
            f"import React from 'react';\n\n"
            f"const {component_name} = () => {{\n"
            f"    return (\n"
            f"        <div>\n"
            f"            <h1>Hello This Project Built by using Foysal Python Script</h1>\n"
            f"        </div>\n"
            f"    );\n"
            f"}};\n\n"
            f"export default {component_name};\n"
        )

    style_filename = f'src/styles/{component_name}.css'
    with open(style_filename, 'w') as file:
        file.write(
            f".{component_name.lower()} {{\n"
            f"    /* Add your styles here */\n"
            f"}}\n"
        )
    update_app_js(component_name)
    print(f'Component "{component_name}" created successfully!')

def update_app_js(component_name):
    app_js_filename = 'src/App.js'
    with open(app_js_filename, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith('import logo from \'./logo.svg\';'):
            lines.insert(i + 1, f"import {component_name} from './components/{component_name}';\n")
            lines.insert(i + 2, f"import './styles/{component_name}.css';\n")
            lines[i] = line.replace('logo', "logo")
         
           
    for i, line in enumerate(lines):
        if line.strip() == '<header className="App-header">':
            lines.insert(i + 1, f"        <{component_name} />\n")
            lines[i] = line.replace('App-header', f"{component_name.lower()}-header")

    with open(app_js_filename, 'w') as file:
        file.writelines(lines)

    print(f'Updated {app_js_filename} to include "{component_name}".')

project_name = input('Enter project name: ')
create_react_project(project_name)
