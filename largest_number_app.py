import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    
    a = st.number_input("Enter the first number:", step=1)
    b = st.number_input("Enter the second number:", step=1)
    c = st.number_input("Enter the third number:", step=1)
    
    if st.button("Find Largest"):
        largest = find_largest(a, b, c)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
