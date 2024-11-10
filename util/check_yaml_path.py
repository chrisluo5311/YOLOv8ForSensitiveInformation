import os
import yaml

def check_yaml_file_path(file_path):
    try:
        # Load the YAML file
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)

        # Extract paths from the YAML file
        base_path = config.get('path')
        train_path = config.get('train')
        val_path = config.get('val')
        test_path = config.get('WIDERFACE_train')

        # Combine base path with specific paths
        train_full_path = os.path.join(base_path, train_path) if base_path and train_path else None
        val_full_path = os.path.join(base_path, val_path) if base_path and val_path else None
        test_full_path = os.path.join(base_path, test_path) if base_path and test_path else None

        # Check existence of each path
        results = {}
        for name, path in [('train', train_full_path), ('val', val_full_path), ('WIDERFACE_train', test_full_path)]:
            if path:
                if os.path.isdir(path):
                    results[name] = f"{name} path exists: {path}"
                else:
                    results[name] = f"{name} path does not exist: {path}"
            else:
                results[name] = f"{name} path not defined properly in YAML."

        return results

    except Exception as e:
        return {"error": f"An error occurred: {e}"}

if __name__ == '__main__':
    yaml_file_path = "../WIDERFACE_train/widerface.yaml"
    results = check_yaml_file_path(yaml_file_path)
    for name, result in results.items():
        print(f"{result}")
