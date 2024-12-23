import json
import requests

def unlock_trophies(deployment_id, json_file, auth_token):
    try:
        # Load the JSON file
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Extract achievements for the given deployment ID
        achievements = []
        for product_id, product_data in data.items():
            if not isinstance(product_data, dict):  # Check if product_data is a dictionary
                # print(f"Skipping invalid product data for product ID '{product_id}': {product_data}")
                continue

            achievements_list = product_data.get("achievements", [])
            if achievements_list is None:
                # print(f"No achievements found for product ID '{product_id}'")
                continue

            for ach in achievements_list:
                if not isinstance(ach, dict):
                    print(f"Skipping invalid achievement entry for product ID '{product_id}': {ach}")
                    continue

                ach_data = ach.get("achievement")
                if isinstance(ach_data, dict) and ach_data.get("deploymentId") == deployment_id:
                    achievements.append(ach_data)

        if not achievements:
            print(f"No achievements found for Deployment ID '{deployment_id}'.")
            return

        # Write only the "name" values of achievements to a text file
        output_file = "achievements.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            for achievement in achievements:
                trophy_name = achievement.get("name")
                if trophy_name:
                    file.write(trophy_name + '\n')

        print(f"Achievement names written to {output_file}")

        # Unlock each achievement
        for achievement in achievements:
            trophy_name = achievement.get("name")
            if not trophy_name:
                continue

            # Construct the URL and payload
            url = f"https://api.epicgames.dev/stats/v1/{deployment_id}/achievements/{sandbox_id}/unlock"
            headers = {
                "Authorization": f"Bearer {auth_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            payload = json.dumps([trophy_name])

            # Make the POST request to unlock the achievement
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                print(f"Successfully unlocked achievement: {trophy_name}")
            else:
                print(f"Failed to unlock achievement: {trophy_name}. "
                      f"Status code: {response.status_code}, Response: {response.text}")

    except FileNotFoundError:
        print(f"File '{json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{json_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
sandbox_id = ""  # Replace with your sandbox ID
deployment_id = "c4763f236d08423eb47b4c3008779c84" # Replace with your deployment ID
json_file = "trophies.json"  # Replace with the path to your JSON file
auth_token = ""  # Replace with your valid Bearer token

unlock_trophies(deployment_id, json_file, auth_token)
