
# CSRF Vulnerability Demonstration (CWE-352)

## Overview
This demonstrates a Cross-Site Request Forgery (CSRF) vulnerability in a Flask application. CSRF attacks trick authenticated users into unknowingly performing actions, here shown by allowing an unauthorized user deletion.

### Simulated Nature of This Demonstration
This simulation is intentionally simple and operates under an unrealistic setup where both the vulnerable application and the exploit page are hosted on the same domain (`127.0.0.1`) but different ports. Realistically, the vulnerable application and the exploit page would be hosted on entirely separate domains. This limitation arises due to the constraints of the available Linux server environment, as described below.

## Files
- `app.py`: Flask application with CSRF vulnerability.
- `exploit.html`: Simulates the CSRF attack.
- `templates/login.html`: Login page.
- `templates/admin.html`: Admin panel for user management.

## Prerequisites
- Python 3.x
- Flask (`pip install Flask`)

## Setup and Running the Application
1. **Install Flask**:
   ```bash
   pip install Flask
   ```

2. **Start the Flask App**:
   ```bash
   python app.py
   ```
   - Access at: `http://127.0.0.1:5000/`

3. **Log in**:
   - Visit `http://127.0.0.1:5000/login` and log in as `admin` or other users.

## Running the CSRF Exploit
1. **Host `exploit.html`**:
   - In the directory with `exploit.html`, run:
     ```bash
     python3 -m http.server 8000
     ```
   - Access `exploit.html` at `http://127.0.0.1:8000/exploit.html`.

2. **Trigger the Attack**:
   - Log in as `admin` on the Flask app.
   - Open `http://127.0.0.1:8000/exploit.html` to simulate the attack.

3. **Verify**:
   - Return to `/admin` in Flask. Refresh the page or log out and then log back in. If `user1` is missing, the exploit succeeded.

## Efforts to Create a Realistic Simulation
In a real-world scenario, CSRF attacks would involve two distinct domains—for instance, the vulnerable application hosted on `http://vulnerable-app.com` and the exploit page hosted on `http://malicious-site.com`. We explored multiple approaches to recreate such a realistic setup, including:

1. **Using `ngrok`**:
   - We tried exposing the Flask application and the exploit page through `ngrok`, assigning them different public URLs to simulate separate domains. The attack simulation worked successfully.

2. **Using Docker**:
   - We used Docker to host the Flask app and exploit page in isolated containers with distinct hostnames, simulating different domains. This also successfully demonstrated the vulnerability.

3. **Modifying the `hosts` File**:
   - By modifying the `hosts` file, we assigned custom domain names (e.g., `flask.local` and `exploit.local`) to each service. This approach was functional and demonstrated the attack.

### Limitations on University Linux Servers
While these approaches worked well in a local or personal setup, constraints on the university Linux servers (such as lack of `sudo` permissions or Docker installation) prevented us from translating this into a realistic, fully replicable setup on those servers. As a result, the final demonstration operates under a simplified configuration with both services running on the same domain but different ports.

## Project Dependencies
- Flask
