import urllib.request
import urllib.parse
import json
import uuid
import sys

def test_database_integration():
    base_url = "http://localhost:8001/api/users"
    
    # Insert a user
    email = f"test_{uuid.uuid4()}@example.com"
    post_url = f"{base_url}?email={urllib.parse.quote(email)}"
    
    try:
        req = urllib.request.Request(post_url, method="POST")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            assert data["email"] == email
            print("Successfully created user")
    except Exception as e:
        print(f"Failed to create user: {e}")
        sys.exit(1)
        
    # Fetch users
    try:
        with urllib.request.urlopen(base_url) as response:
            users = json.loads(response.read().decode())
            assert len(users) >= 1
            assert any(u["email"] == email for u in users)
            print("Successfully fetched users and found the new user!")
    except Exception as e:
        print(f"Failed to fetch users: {e}")
        sys.exit(1)
        
    print("Database integration verification passed!")

if __name__ == "__main__":
    test_database_integration()
