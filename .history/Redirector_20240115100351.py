import pandas as pd

def generate_redirect_rules(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, usecols=['SLUG', 'NEW'])

    with open(output_file, 'w') as f:
        for index, row in df.iterrows():
            # Remove trailing slash from SLUG and NEW if present
            slug = row['SLUG'].rstrip('/')
            new_url = row['NEW'].rstrip('/')
            
            # Construct the redirect rule
            rule = f"""
        <rule name="Redirect Rule {index + 1}" stopProcessing="true">
          <match url="^updates/{slug}/?$" />
          <action type="Redirect" redirectType="Permanent" url="{new_url}" />
        </rule>
"""
            # Write the rule to the file
            f.write(rule)

# Usage
generate_redirect_rules('webconfigrules.xlsx', 'redirect_rules.txt')
