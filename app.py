import fact
import streamlit as st
def main():
  st.title("Factorial")
  number=st.number_input("Enter number",
                         min_value=0,
                         max_value=999)
  if st.button("Calculate"):
    value=fact.fac(number)
    st.write(f"The factorial of {number} is {value}")
if __name__=="__main__":
  main()