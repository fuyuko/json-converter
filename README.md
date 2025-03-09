# JSON to CSV Converter

This Python script converts a JSON file to a CSV file, allowing you to specify a `kind` value to filter the items to be exported.

**Disclaimer: This script is generated using GitHub Copilot.**

## Usage

To use this script, run the following command:

```sh
python json_to_csv.py <input_json_file> <output_csv_file> <kind_value>
```

## Example Usage

### convert an exported json file from to a csv file as a list of tasks

* Specify the kind name "tasks#tasks" 
* See https://support.google.com/tasks/answer/10017961?hl=en on how to export Google Tasks

```sh
python json_to_csv.py google_tasks.json output.csv "tasks#tasks"