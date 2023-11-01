from github import Github

# Your GitHub Personal Access Token
access_token = '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'

# Repository information
repo_owner = 'giVINtake'
repo_name = '1'
file_path = 'index.html'
image_name_to_remove = 'a1.jpg'  # Replace with the image name you want to remove

# Create a GitHub instance using your access token
g = Github(access_token)

# Get the repository
repo = g.get_user(repo_owner).get_repo(repo_name)

# Get the contents of the HTML file
file = repo.get_contents(file_path)

# Read the file content
file_content = file.decoded_content.decode('utf-8')

# Split the file content by the specified image name and remove the articles
article_parts = file_content.split(f'<img src="images/achat/{image_name_to_remove}"')
new_content = ''.join(article_parts[0:-1])  # Join all parts except the last one

# Update the file on GitHub
repo.update_file(file.path, f"Remove articles with image {image_name_to_remove}", new_content, file.sha)

print(f"Articles with image {image_name_to_remove} removed from {file_path}")