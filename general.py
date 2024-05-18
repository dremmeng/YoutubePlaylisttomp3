import os

#Each Playlist Url is it's own seperate project (folder)

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create downloaded files (if not created)
def create_data_files(project_name, base_url, file_name):
    file_name = os.path.join(project_name,file_name+".txt")
    if not os.path.isfile(file_name):
        write_file(file_name, base_url)

# Create a new file
def write_file(path, data):
    with open(path, 'w') as g:
        g.write(data)



# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")

