# main.py

from register import Register

def main():
    r0 = Register("R0")
    r0.set(42)
    print(f"{r0.name} = {r0.get()}")

if __name__ == "__main__":
    main()
