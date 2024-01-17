import pandas as pd

def generate_rewrite_map(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, usecols=['SLUG', 'NEW'])

    with open(output_file, 'w') as f:
        # Write the opening tags
        f.write('<rewriteMaps>\n')
        f.write('  <rewriteMap name="Redirects">\n')

        for index, row in df.iterrows():
            # Ensure SLUG is a string and construct the key
            slug = '/updates/' + str(row['SLUG']).strip('/')
            slug2 = '/updates/' + str(row['SLUG']).strip('/') +'/'
            
            # Ensure correct URL format in NEW, ensuring no double slashes
            new_url = row['NEW'].replace('//', '/').replace('http:/', 'http://').replace('https:/', 'https://')
            
            # Construct the add entry
            add_entry = f'    <add key="{slug}" value="{new_url}" />\n'
            add_entry2 = f'    <add key="{slug2}" value="{new_url}" />\n'
            
            # Write the add entry to the file
            f.write(add_entry)
            f.write(add_entry2)

        # Write the closing tags
        f.write('  </rewriteMap>\n')
        f.write('</rewriteMaps>\n')

# Usage
generate_rewrite_map('webconfigrules.xlsx', 'rewritemaps.config')
