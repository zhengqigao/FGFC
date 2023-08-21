import os
import glob
import yaml

def parse_yaml_file(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data

def generate_html_by_category(profiles, categories):
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Profiles by Category</title>
    <!-- Add Bootstrap CSS link -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
    """

    for category in categories:
        html_content += f'<h2>{category} Category</h2>'
        html_content += '<div class="row">'
        
        category_profiles = [profile for profile in profiles if profile["Mandatory"]["Category"] == category]
        for profile in category_profiles:
            html_content += '<div class="col-md-6">'
            html_content += '<div class="card my-4">'
            html_content += f'<div class="card-body">'
            html_content += f'<h4 class="card-title">{profile["Mandatory"]["First Name"]} {profile["Mandatory"]["Last Name"]}</h4>'
            html_content += f'<p class="card-text">School: {profile["Mandatory"]["Full School Name"]}</p>'
            html_content += f'<p class="card-text">Email: {profile["Mandatory"]["Verify Email"]}</p>'
            html_content += f'<p class="card-text">Short Bio: {profile["Optional"].get("Short Bio", "N/A")}</p>'
            html_content += '</div></div></div>'
        
        html_content += '</div>'
    
    html_content += """    </div>
    <!-- Add Bootstrap JS and jQuery links -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
"""
    return html_content

def main():
    directory_path = "./list/"  # Replace with the actual directory path
    output_html_path = "./html/main.html"  # Change this to your desired output HTML file name
    categories = ['EE', 'CS', 'Math', 'Stat']  # Pre-defined categories

    yaml_files = glob.glob(os.path.join(directory_path, "*.yaml"))
    profiles = []

    for yaml_file in yaml_files:
        profile_data = parse_yaml_file(yaml_file)
        profiles.append(profile_data)

    html_content = generate_html_by_category(profiles, categories)

    with open(output_html_path, "w") as output_file:
        output_file.write(html_content)

if __name__ == "__main__":
    main()
