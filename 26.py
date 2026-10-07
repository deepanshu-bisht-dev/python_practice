# Password Strength Meter
import string

COMMON = {"123456", "password", "qwerty", "admin", "letmein", "welcome", "abc123"}
SEQUENCES = ["abcdefghijklmnopqrstuvwxyz", "qwertyuiop", "0123456789"]

def has_sequence(pw, length=4):
    pw = pw.lower()
    for seq in SEQUENCES:
        for i in range(len(seq) - length + 1):
            chunk = seq[i:i + length]
            if chunk in pw or chunk[::-1] in pw:
                return chunk
    return None

def has_repeats(pw, n=3):
    for i in range(len(pw) - n + 1):
        if len(set(pw[i:i + n])) == 1:
            return pw[i:i + n]
    return None

def check_password(pw):
    score, tips = 0, []

    # Length (max 30)
    score += min(len(pw), 15) * 2
    if len(pw) < 12:
        tips.append("Use 12 or more characters")

    # Variety (max 40)
    checks = [
        (any(c.islower() for c in pw), "lowercase letter"),
        (any(c.isupper() for c in pw), "uppercase letter"),
        (any(c.isdigit() for c in pw), "digit"),
        (any(c in string.punctuation for c in pw), "special character"),
    ]
    for ok, name in checks:
        if ok:
            score += 10
        else:
            tips.append(f"Add a {name}")

    # Bonus for unique characters (max 30)
    score += min(len(set(pw)), 15) * 2

    # Penalties
    if pw.lower() in COMMON:
        score = min(score, 10)
        tips.append("This is a very common password")
    seq = has_sequence(pw)
    if seq:
        score -= 15
        tips.append(f'Avoid sequence "{seq}"')
    rep = has_repeats(pw)
    if rep:
        score -= 10
        tips.append(f'Avoid repeated characters "{rep}"')

    score = max(0, min(100, score))
    level = "Weak" if score < 40 else "Medium" if score < 70 else "Strong"
    return score, level, tips

if __name__ == "__main__":
    while True:
        pw = input("\nEnter password (or 'q' to quit): ")
        if pw.lower() == "q":
            break
        score, level, tips = check_password(pw)
        print(f"Score: {score}/100 ({level})")
        for t in tips:
            print("  - " + t)