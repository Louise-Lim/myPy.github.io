from flask import Flask, render_template_string
import csv

app = Flask(__name__)

# Function to read and process Table 1
def read_table1_data():
    table1_data = {}
    with open('Table_Input.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header
        for row in reader:
            index, value = row
            table1_data[index] = int(value)
    return table1_data

# Function to calculate Table 2 values
def calculate_table2_data(table1_data):
    table2_data = {
        'Alpha': table1_data['A5'] + table1_data['A20'],
        'Beta': table1_data['A15'] // table1_data['A7'],
        'Charlie': table1_data['A13'] * table1_data['A12']
    }
    return table2_data

# HTML template to display tables
html_template = """
<h2>Table 1:</h2>
<table border="1">
  <tr>
    <th>Index #</th>
    <th>Value</th>
  </tr>
  {% for index, value in table1_data.items() %}
    <tr>
      <td>{{ index }}</td>
      <td>{{ value }}</td>
    </tr>
  {% endfor %}
</table>

<h2>Table 2:</h2>
<table border="1">
  <tr>
    <th>Category</th>
    <th>Value</th>
  </tr>
  {% for category, value in table2_data.items() %}
    <tr>
      <td>{{ category }}</td>
      <td>{{ value }}</td>
    </tr>
  {% endfor %}
</table>
"""

@app.route('/')
def display_tables():
    # Retrieve Table 1 data and calculate Table 2 data
    table1_data = read_table1_data()
    table2_data = calculate_table2_data(table1_data)
    return render_template_string(html_template, table1_data=table1_data, table2_data=table2_data)

if __name__ == '__main__':
    app.run()
