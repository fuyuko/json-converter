import json
import csv
import sys

def json_to_csv(json_file_path, csv_file_path, kind_value):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Navigate to the items with the specified kind value
    task_items = []
    for task_list in data.get("items", []):
        if task_list.get("kind") == kind_value:
            task_items.extend(task_list.get("items", []))
    
    if not task_items:
        print(f"No items found with kind: {kind_value}")
        return
    
    # Collect all keys from all items
    keys = set()
    for item in task_items:
        keys.update(item.keys())
    keys = list(keys)

    # Ensure all items have the same keys
    for item in task_items:
        for key in keys:
            if key not in item:
                item[key] = None

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(task_items)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python json_to_csv.py <input_json_file> <output_csv_file> <kind_value>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    csv_file_path = sys.argv[2]
    kind_value = sys.argv[3]

    json_to_csv(json_file_path, csv_file_path, kind_value)
    print(f"Successfully converted {json_file_path} to {csv_file_path} with kind: {kind_value}")