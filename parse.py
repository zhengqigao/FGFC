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
<p>This list functions as a bridge, linking both older and newer generations of Fudan students engaged in research. While Fudan University unquestionably boasts prestige, we must also recognize its shortcomings when compared to those top universities (e.g., Tsinghua) --- Just contemplate the discrepancy in the number of Fudan graduates working in world-class universities compared to those from Tsinghua. Through this list, our aspiration is for forthcoming generations of Fudan students seeking research opportunities to establish meaningful connections with their senior Fudan alumni. We believe that professors who have graduated from Fudan would be inclined to provide assistance and offer internship opportunities upon receiving an email from a current Fudan student with a high GPA.
</p>

<h1>FGFC List</h1>
<p> Each entry is organized in the following format: Name (University, Category) — Research Keywords. Please note that [Category] may not necessarily correspond directly to the individual's department or school name, but rather reflects their research interests. The following list is arranged in alphabetical order.
</p>
<ol>
"""

for key, person in yaml_data.items():
    name = f"{person['FirstName']} {person['LastName']}"
    affiliation = person['Affiliation']
    category = person['Category']
    webpage = person['Webpage']
    research_key = person.get('ResearchKey', '')  # Get the ResearchKey if present, or use an empty string

    item = f"<li><a href='{webpage}'>{name}</a> ({affiliation}, {category}) --- {research_key}</li>"
    html_content += item

html_content += """
</ol>

<h1>Contributors</h1>
<p>This list is contributed by: 
<a href="https://zhengqigao.github.io/">Zhengqi Gao</a>,
<a href="https://hanruiwang.me/">Hanrui Wang</a>,
<a href="https://mingrany.github.io/">Mingran Yang</a>,
</p>

<h1>Feedback</h1>
<p>
If you come across any missing professor information, kindly proceed to create a pull request on <a href="https://github.com/zhengqigao/FGFC">our GitHub repo</a>, or feel free to reach out to us via email at <a href="mailto:fgfc23.start@gmail.com">fgfc23.start@gmail.com</a>. We welcome any suggestions or comments.
</p>


</body>
</html>
"""

# Write the HTML content to an "index.html" file
with open("index.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
