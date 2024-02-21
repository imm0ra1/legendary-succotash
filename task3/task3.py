#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def fill_report(values, tests):
    report = tests.copy()

    def fill_values(node):
        if 'id' in node:
            node_id = node['id']
            if node_id in values:
                node['value'] = values[node_id]
        if 'tests' in node:
            for child_node in node['tests']:
                fill_values(child_node)

    fill_values(report)
    return report

def main(values_file, tests_file, report_file):
    with open(values_file, 'r') as f:
        values_data = json.load(f)

    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    report_data = fill_report(values_data, tests_data)

    with open(report_file, 'w') as f:
        json.dump(report_data, f, indent=2)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Использование: python program.py <values_file> <tests_file> <report_file>")
        sys.exit(1)

    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    main(values_file_path, tests_file_path, report_file_path)

