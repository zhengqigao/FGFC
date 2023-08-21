import yaml

# Read the YAML data from the external file
with open("collection.yaml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Sort the data alphabetically by name
sorted_data = sorted(yaml_data.values(), key=lambda person: f"{person['LastName']} {person['FirstName']}")

# Generate HTML content
html_content = f"""
<html>
<head>
<title>Fudan-Graduated Faculty Collection List</title>
<style>
h1 {{
    font-size: 20px;
}}
</style>
</head>
<body>

<h1>Introduction</h1>
<p>This list functions as a bridge, connecting both older and newer generations of Fudan students engaged in research. While Fudan University undoubtedly boasts prestige, we must also acknowledge its shortcomings when compared to top universities like Tsinghua. Consider the disparity in the number of Fudan graduates working in world-class universities compared to those from Tsinghua. Through this list, our aspiration is to help upcoming generations of Fudan students seeking research opportunities establish meaningful connections with their senior Fudan alumni. We believe that professors who have graduated from Fudan would be inclined to provide assistance and offer internship opportunities upon receiving an email from a current Fudan student with a high GPA.</p>

<p><strong>We are actively expanding the list.</strong> The individuals considered here meet two criteria: (i) they completed their bachelor's, master's, or PhD studies at Fudan University, and (ii) they are currently professors at universities other than Fudan. (Note: Fudan students can contact any Fudan professors on campus, so we have chosen not to include them in this list.)</p>

<p>We are seeking a group of volunteers to maintain and update this list. If you are interested, please get in touch with us via email at <a href="mailto:fgfc23.start@gmail.com">fgfc23.start@gmail.com</a>.</p>


<h1>FGFC List</h1>
<p> Each entry is organized in the following format: Name (University, Category) — Research Keywords. Please note that [Category] may not necessarily correspond directly to the individual's department or school name, but rather reflects their research interests. The following list is arranged in alphabetical order.
</p>
<ol>
"""

for person in sorted_data:
    name = f"{person['FirstName']} {person['LastName']}"
    affiliation = person['Affiliation']
    category = person['Category']
    webpage = person['Webpage']
    research_key = person.get('ResearchKey', '')  # Get the ResearchKey if present, or use an empty string

    item = f"<li><a href='{webpage}'>{name}</a> ({affiliation}, {category}) --- {research_key}</li>"
    html_content += item

html_content += """
</ol>

<h1>Acknowledgement</h1>
<p>This list is contributed by many Fudan alumnis.
</p>

<h1>Feedback</h1>

<p>If you encounter any missing professor information or wish to contribute, please consider creating a <a href="https://github.com/zhengqigao/FGFC" target="_blank">pull request</a> on our GitHub repository by updating the collection.yaml file. Alternatively, you can contact us via email at <a href="mailto:fgfc23.start@gmail.com">fgfc23.start@gmail.com</a>. In your email, please provide all the necessary fields required for a new entry. You can refer to the <a href="https://github.com/zhengqigao/FGFC/collection.yaml" target="_blank">collection.yaml</a> to understand the required information. We welcome professor information from all domains. Additionally, we value any suggestions or comments you may have.</p>



</body>
</html>
"""

# Write the HTML content to an "index.html" file
with open("index.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
