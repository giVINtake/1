from github import Github
from bs4 import BeautifulSoup

# Your GitHub Personal Access Token
access_token = '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'

# Repository information
repo_owner = 'giVINtake'
repo_name = '1'
file_path = 'index.html'
image_name_to_remove = 'a1.jpg'  # Replace with the image name you want to remove

# Create a GitHub instance using your access token
g = Github(access_token)
repo = g.get_user(repo_owner).get_repo(repo_name)

# Fetch the HTML content from your repository
file_path = "index.html"  # Replace with the actual path
file = repo.get_contents(file_path)
html_content = file.decoded_content.decode("utf-8")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find and remove articles with the image name "a1"
for article in soup.find_all("article"):
    img_tag = article.find("img")
    if img_tag and "a1.jpg" in img_tag.get("src"):
        article.decompose()  # Remove the article

# Update the HTML content
updated_html_content = str(soup)

# Commit and push the changes to GitHub
commit_message = "Remove articles with image name 'a1'"
repo.update_file(file_path, commit_message, updated_html_content, file.sha, branch=branch_name)