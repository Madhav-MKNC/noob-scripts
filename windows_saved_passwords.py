import subprocess


def get_output(cmd):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        return result
    else:
        raise Exception(f"Command failed: {result.stderr}")


profiles = [line.split(":")[1].strip() for line in get_output("netsh wlan show profiles").stdout.split('\n') if "All User Profile" in line]

for profile in profiles:
    cmd = f'netsh wlan show profile name="{profile}" key=clear'
    result = get_output(cmd)
    if result.returncode == 0:
        print(f"--- {profile} ---")

        # Split the output into lines
        lines = result.stdout.splitlines()
        
        try:
            for line in lines:
                # Check if 'Key Content' is in the line (case insensitive)
                if "key content" in line.lower():
                    # Extract the password
                    password = line.split(':')[1].strip()

                    # Print the formatted output
                    print(f"SSID: {profile}")
                    print(f"Password: {password}")
                    print()
                    break  # Assuming only one line with 'Key Content'
            else:
                print(f"No password found for {profile}\n")
        except Exception as e:
            print(f"Error processing profile {profile}: {e}\n")
    else:
        print(f"Error occurred with profile {profile}: {result.stderr}\n")


