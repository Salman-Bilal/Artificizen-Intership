"""
Question: 1: Write a hash_password() and verify_password() utility using passlib. Test them in isolation before wiring into routes. 

"""


import sys
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")


def hash_password(passwrod: str) -> str:

    return pwd_context.hash(passwrod)

def verify_password(plainpassword: str, hashpassword: str) -> bool:

    return pwd_context.verify(plainpassword, hashpassword)

if __name__ == "__main__":
    print("=" * 60)
    print("STARTING PASSWORD SECURITY TESTS")
    print("=" * 60)

    print("\nExecuting Test Case 1: Checking Hash Generation...")
    raw_password = "MySuperSecretSecure123!"
    secure_hash = hash_password(raw_password)

    print(f" Plain Password : {raw_password}")
    print(f" Generated Password : {secure_hash}")

    assert secure_hash != raw_password, "Fail: Hash is identical to plain text!"
    assert secure_hash.startswith("$2b$"), "Fail: Not a valid bcrypt hash signature!"
    print("Success: Hash was generated and matches the bcrypt standard structure.")

    print("\nExecuting Test Case 2: Verification of Correct Password...")
    is_valid_match = verify_password(raw_password, secure_hash)
    print(f"Verification Result: {is_valid_match}")
    assert is_valid_match is True, "Fail: The correct password failed verification!"
    print("Success: Correct password successfully verified against the hash.")

    print("\nExecuting Test Case 3: Rejection of Incorrect Password...")
    wrong_password = "NotTheRightPassword"
    is_invalid_match = verify_password(wrong_password, secure_hash)
    print(f"Verification Result: {is_invalid_match}")
    assert is_invalid_match is False, "Fail: An incorrect password was validated!"
    print("✅ Success: Incorrect password correctly rejected.")

    # Test Case 4: Unique Hash Generation (Salt Verification)
    print("\nExecuting Test Case 4: Unique Salts Check...")
    another_hash = hash_password(raw_password)
    print(f" Hash 1: {secure_hash}")
    print(f" Hash 2: {another_hash}")
    assert secure_hash != another_hash, "Fail: Identical passwords generated identical hashes! Salt is missing."
    print("Success: Identical passwords yielded unique hashes (Salting works!).")

    print("\n" + "=" * 60)
    print("ALL PASSWORD SECURITY TESTS PASSED")
    print("=" * 60)